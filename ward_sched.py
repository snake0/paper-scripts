#!/usr/bin/python3

# The ward scheduler pings all nodes periodically for cpu and mem utilization
# info. It also sends a command to dst for VM migration.

import random
import socket
import struct
import sys
import time
import xml.etree.ElementTree as ET

YANNI_MIGRATE = 0x38
YANNI_PING = 0x78
# Hard code here...
NCPU_PER_NODE = 16

violation_load = 80


class bcolors:
    DEFAULT = '\033[39m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class vm:
    def __init__(self, vmid):
        self.vmid = vmid
        # must start to run in node 0
        self.current_node = 0
        self.in_mig = False
        self.cores = 0
        self.mem = 0
        self.mig_dst = -1

    def __str__(self):
        return "VM %d with %s cores and %s memory" % (self.vmid, self.cores,
                                                      self.mem)


class util:
    def __init__(self, cpu1, cpu5, cpu15, mem):
        self.cpu1 = cpu1
        self.cpu5 = cpu5
        self.cpu15 = cpu15
        self.mem = mem

    def __str__(self):
        # return "cpu1 %1.2f cpu5 %1.2f cpu15 %1.2f" % \
        #        (self.cpu1, self.cpu5, self.cpu15)
        return "cpu1 %1.2f" % (self.cpu1)


class ward:
    def __init__(self):
        self.nodes = []  # node_config list
        self.vms = []
        self.src = 0
        self.dst = 1

    def ping(self, target):
        assert target < len(self.nodes)
        pingvm = None
        old_mig_status = None

        for v in self.vms:
            if v.in_mig:
                # only 1 vm could be in migration
                pingvm = v
                old_mig_status = v.in_mig
                break

        self.nodes[target].ping(pingvm)
        if pingvm is not None and old_mig_status and not pingvm.in_mig:
            pingvm.current_node = pingvm.mig_dst
            pingvm.mig_dst = -1
            print("Migration of VM %d done." % pingvm.vmid)

    def migrate(self, vmid, src, dst):
        assert src < len(self.nodes)
        assert dst < len(self.nodes)

        if self.vms[vmid].in_mig:
            print("VM%d in migration" % vmid)
            return False

        self.vms[vmid].in_mig = True
        self.vms[vmid].mig_dst = dst

        print("Prepare to migrate VM%d from %d to %d." % (vmid, src, dst))
        try:
            self.nodes[dst].migrate(vmid, src)
        except IOError:
            print("%sMigration from %d to %d fails%s" % (bcolors.FAIL, src,
                                                         dst, bcolors.DEFAULT))
            return False
        else:
            return True

    # new
    def find_busiest_node(self):
        busiest = -1
        busiest_load = -1.0

        for i in range(len(self.nodes)):
            n = self.nodes[i]
            if busiest_load < n.utils[-1].cpu1:
                busiest_load = n.utils[-1].cpu1
                busiest = i

        if busiest_load > violation_load:
            print("Found node %d busy" % busiest)
            print("Busy %s" % str(self.nodes[busiest].utils[-1]))
            return busiest, busiest_load
        else:
            return -1, -1

    # new
    def find_idlest_node(self):
        idlest = -1
        idlest_load = sys.float_info.max

        for i in range(len(self.nodes)):
            n = self.nodes[i]
            if idlest_load > n.utils[-1].cpu1:
                idlest_load = n.utils[-1].cpu1
                idlest = i

        print("Found node %d idle" % idlest)
        print("Idle %s" % str(self.nodes[idlest].utils[-1]))
        return idlest, idlest_load

    # old
    # TODO
    def pick_next_busy(self):
        for i in range(len(self.nodes)):
            n = self.nodes[i]

            if n.utils[-1].cpu1 > 0.7 and \
                    n.utils[-1].cpu1 >= n.utils[-1].cpu5 >= n.utils[-1].cpu15:
                return i
        return -1

    # old
    # TODO
    def pick_next_idle(self, vm):
        # idle_threshold about 0.25
        idle_threshold = vm.cores / NCPU_PER_NODE
        for i in range(len(self.nodes)):
            n = self.nodes[i]

            if (n.utils[-1].cpu1 <= idle_threshold and
                    n.utils[-1].cpu5 <= idle_threshold and
                    n.utils[-1].cpu15 <= idle_threshold):
                print("Found node %d idle" % i)
                print("Idle %s" % str(n.utils[-1]))
                return i
        return -1

    # old
    # Random selection
    def select_next_vm(self):
        return self.vms[int(random.randint(0, len(self.vms) - 1))]

    # new
    def select_next_vm_from_node(self, node):
        candidates = []
        for vm in self.vms:
            if vm.current_node == node and not vm.in_mig:
                candidates.append(vm)
        if len(candidates) == 0:
            return None
        else:
            return candidates[int(random.randint(0, len(candidates) - 1))]

    def flip(self):
        print("Src Dst flipped")
        temp = self.src
        self.src = self.dst
        self.dst = temp

    # new
    def try_migrate(self):
        src, src_load = self.find_busiest_node()
        if src is -1:
            return

        dst, dst_load = self.find_idlest_node()
        if dst is not src:
            vm = self.select_next_vm_from_node(src)
            if vm is None:
                return
            if dst_load + (100.0 * vm.cores / NCPU_PER_NODE) < src_load:
                print("dst_load %f src_load %f vm %f" % \
                      (dst_load, src_load, (100.0 * vm.cores / NCPU_PER_NODE)))
                self.migrate(vm.vmid, src, dst)
        # vm = self.select_next_vm()
        # print("Attempting to migrate VM%d" % vm.vmid)

        # if self.migrate(vm.vmid, self.src, self.dst):
        #     self.flip()

    def run(self):
        while True:
            for i in range(len(self.nodes)):
                self.ping(i)

            # src, dst = self.pick_next_busy(), self.pick_next_idle(vm)
            # if 0 <= src != dst >= 0:
            #     self.migrate(vm.vmid, src, dst)

            self.try_migrate()

            time.sleep(1)

    def __str__(self):
        s = ''
        for n in self.nodes:
            s += str(n) + "\n"
        return s


class node:
    def __init__(self, ipaddr, globalport, no):
        self.ipaddr = ipaddr
        self.globalport = globalport
        self.no = no
        self.utils = []
        self.active = False

    # Build a connection and ask for mem, cpu util, and a vm's mig status
    def ping(self, pingvm):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.ipaddr, int(self.globalport)))

                if pingvm is None:
                    s.sendall(struct.pack("ii", YANNI_PING, ~0))
                else:
                    s.sendall(struct.pack("ii", YANNI_PING, pingvm.vmid))
                rdata = s.recv(17)
                u = util(struct.unpack('f', rdata[0:4])[0],
                         struct.unpack('f', rdata[4:8])[0],
                         struct.unpack('f', rdata[8:12])[0],
                         struct.unpack('f', rdata[12:16])[0])
                if pingvm is not None:
                    pingvm.in_mig = struct.unpack('?', rdata[16:17])[0]
                print("Node %d util %s" % (self.no, str(u)))
                self.utils.append(u)

        except IOError:
            print("Ping IOError")
            return False
        else:
            self.active = True
            return True

    def migrate(self, vmid, src):
        assert self.active
        # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #     s.connect((self.ipaddr, int(self.globalport)))
        #     s.sendall(struct.pack("iiii", YANNI_MIGRATE, vmid, src, self.no))

    def migrate_done(self):
        self.in_mig = False

    def __str__(self):
        return self.ipaddr + ":" + self.globalport


"""
config_file is a XML file
"""


def ward_init(config_file):
    tree = ET.parse(config_file)
    root = tree.getroot()
    w = ward()
    i = 0

    thisvm, appended = None, set()
    for n in root:
        for c in n:
            if c.tag == 'IpAddr':
                ipaddr = c.text
            if c.tag == 'GlobalPort':
                globalport = c.text
            if c.tag == "VM":
                if int(c.attrib["id"]) in appended:
                    continue
                thisvm = vm(int(c.attrib["id"]))
                w.vms.append(thisvm)
                appended.add(thisvm.vmid)
                for config in c:
                    if config.tag == "Smp":
                        thisvm.cores = int(config.text)
                    if config.tag == "Mem":
                        thisvm.mem = config.text
                print(str(thisvm))

        print("IPaddr %s globalport %s" % (ipaddr, globalport))
        w.nodes.append(node(ipaddr, globalport, i))
        i += 1
    return w


ward = ward_init("config.xml")
ward.run()
