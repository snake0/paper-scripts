#!/usr/bin/python3

# The ward scheduler pings all nodes periodically for cpu and mem utilization
# info. It also sends a command to dst for VM migration.

import os
import socket
import struct
import sys
import time
import xml.etree.ElementTree as ET

YANNI_MIGRATE = 0x38
YANNI_PING = 0x78
# Hard code here...
NCPU_PER_NODE = 40

violation_load = 70


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
        return "VM %d on node %d" % (self.vmid, self.current_node)


class util:
    def __init__(self, cpu1, cpu5, cpu15, mem):
        self.cpu1 = cpu1
        self.cpu5 = cpu5
        self.cpu15 = cpu15
        self.mem = mem

    def __str__(self):
        # return "cpu1 %1.2f cpu5 %1.2f cpu15 %1.2f" % \
        #        (self.cpu1, self.cpu5, self.cpu15)
        return "cpus %1.2f  %1.2f  %1.2f" % (self.cpu1, self.cpu5, self.cpu15)


class ward:
    def __init__(self):
        self.nodes = []  # node_config list
        self.vms = []
        self.src = 0
        self.dst = 1
        self.n_mig = 0
        self.migrating = False

    def ping(self, target):
        assert target < len(self.nodes)
        # print("Pinging Node%d" % target)
        pingvm = None
        old_mig_status = None

        for i in range(len(self.vms)):
            v = self.vms[i]
            if v.in_mig and v.mig_dst is target:
                print("Found in mig VM%d from %d to %d" % (v.vmid, v.current_node, target))
                # only 1 vm could be in migration
                pingvm = i
                old_mig_status = v.in_mig
                break

        if pingvm is not None:
            self.nodes[target].ping(self.vms[pingvm])
        else:
            self.nodes[target].ping(None)

        if pingvm is not None and old_mig_status and not self.vms[pingvm].in_mig:
            self.vms[pingvm].current_node = self.vms[pingvm].mig_dst
            self.vms[pingvm].mig_dst = -1
            print("%s--------------- Migration End --------------%s"
                  % (bcolors.WARNING, bcolors.DEFAULT))
            print("Migration of VM %d to %d done." % (self.vms[pingvm].vmid,
                                                      self.vms[pingvm].current_node))
            self.migrating = False
            self.print_all_up_vm()

    def migrate(self, vmid, src, dst):
        assert src < len(self.nodes)
        assert dst < len(self.nodes)

        if self.vms[vmid].in_mig:
            print("VM%d in migration" % vmid)
            return False

        print("%s--------------- Migration Start --------------%s"
              % (bcolors.WARNING, bcolors.DEFAULT))

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
            if busiest_load >= self.nodes[busiest].utils[-1].cpu5 >= \
                    self.nodes[busiest].utils[-1].cpu15:
                print("Found node %d busy" % busiest)
                # print("Busy %s" % str(self.nodes[busiest].utils[-1]))
                return busiest, busiest_load
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
        # print("Idle %s" % str(self.nodes[idlest].utils[-1]))
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
    def pick_next_idle(self, vm0):
        # idle_threshold about 0.25
        idle_threshold = vm0.cores / NCPU_PER_NODE
        for i in range(len(self.nodes)):
            n = self.nodes[i]

            if (n.utils[-1].cpu1 <= idle_threshold and
                    n.utils[-1].cpu5 <= idle_threshold and
                    n.utils[-1].cpu15 <= idle_threshold):
                print("Found node %d idle" % i)
                print("Idle %s" % str(n.utils[-1]))
                return i
        return -1

    def is_vm_up(self, vm0):
        ret = False
        if vm0.in_mig:
            return ret
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            vm_ip = self.nodes[vm0.current_node].ipaddr
            vm_port = 10000 + vm0.current_node * 12 + vm0.vmid
            # print("Connecting to %s:%d" %(vm_ip, vm_port))
            if s.connect_ex((vm_ip, vm_port)) is 0:
                ret = True
                s.shutdown(2)
            s.close()
            return ret

    def print_all_up_vm(self):
        for vm0 in self.vms:
            if self.is_vm_up(vm0):
                print(str(vm0) + " @ " + self.nodes[vm0.current_node].ipaddr)

    # old
    # Random selection
    def select_next_vm(self):
        for vm0 in self.vms:
            if self.is_vm_up(vm0) and not vm0.in_mig:
                return vm0
        return None

    # new
    def select_next_vm_from_node(self, node):
        candidates = []
        for vm0 in self.vms:
            if vm0.current_node == node and not vm0.in_mig:
                candidates.append(vm0)
        if len(candidates) == 0:
            return None
        else:
            for vm0 in candidates:
                if self.is_vm_up(vm0) and not vm0.in_mig:
                    return vm0
            return None

    def flip(self):
        print("Src Dst flipped")
        temp = self.src
        self.src = self.dst
        self.dst = temp

    # new
    def try_migrate(self):
        if self.migrating:
            return
        src, src_load = self.find_busiest_node()
        if src is -1:
            return

        dst, dst_load = self.find_idlest_node()
        if dst is not src:
            vm0 = self.select_next_vm_from_node(src)
            if vm0 is None:
                print("No migratable VMs found on Node%d" % src)
                return
            print("VM%d migrating from %d to %d" % (vm0.vmid, src, dst))
            self.migrate(vm0.vmid, src, dst)
            self.migrating = True

        # src, src_load = self.find_busiest_node()
        # if src is -1:
        #     return

        # dst, dst_load = self.find_idlest_node()
        # if dst is not src:
        #     vm0 = self.select_next_vm_from_node(src)
        #     if vm0 is None:
        #         print("No migratable VMs found on Node%d" % src)
        #         return
        #     vm_load = 100 * vm0.cores / NCPU_PER_NODE

        #     i = 0
        #     while dst_load + i * vm_load <= src_load:
        #         i = i + 1
        #     i = i - 1
        #     print("%d VMs needed to be migrated from %d to %d" % (i, src, dst))

        #     j = 0
        #     while vm0 is not None and i is not 0:
        #         j = j + 1
        #         i = i - 1
        #         print("VM%d migrating from %d to %d" % (vm0.vmid, src, dst))
        #         print("%s--------------- Migration Start --------------%s"
        #             % (bcolors.WARNING, bcolors.DEFAULT))
        #         self.migrate(vm0.vmid, src, dst)
        #         vm0 = self.select_next_vm_from_node(src)

        #     print("src_load %f dst_load %f vm %f" %
        #           (src_load, dst_load, j * vm_load))

        # vm = self.select_next_vm()
        # if vm is None:
        #     return False

        # print("Compressing completed. Waiting for dst vm to run...")
        # if self.n_mig is 0:
        #     pass
        # elif self.n_mig is 1:
        #     time.sleep(50)
        # else:
        #     time.sleep(50)
        # print("Attempting to migrate VM%d" % vm.vmid)

        # if self.migrate(vm.vmid, self.src, self.dst):
        #     self.n_mig = self.n_mig + 1
        #     self.flip()
        #     return True

        # return False

    def run(self):
        while True:
            utils = []
            for i in range(len(self.nodes)):
                self.ping(i)
            for n in self.nodes:
                utils.append("%1.2f" % n.utils[-1].cpu1)
            print(utils)
            self.print_all_up_vm()

            #     utils.append(str(self.nodes[i].utils[-1]))
            # src, dst = self.pick_next_busy(), self.pick_next_idle(vm)
            # if 0 <= src != dst >= 0:
            #     self.migrate(vm.vmid, src, dst)
            # print(utils)

            self.try_migrate()
            # if migrated:
            #     j = j + 1
            #     if j is 5:
            #         break

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

                if len(self.utils) >= 15:
                    avg = 0
                    for u0 in self.utils[-15:]:
                        avg = avg + u0.cpu1
                    avg = avg / 15
                    u.cpu15 = avg

                if len(self.utils) >= 5:
                    avg = 0
                    for u0 in self.utils[-5:]:
                        avg = avg + u0.cpu1
                    avg = avg / 5
                    u.cpu5 = avg
                self.utils.append(u)

        except IOError:
            print("Ping IOError")
            return False
        else:
            self.active = True
            return True

    def migrate(self, vmid, src):
        assert self.active
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.ipaddr, int(self.globalport)))
            s.sendall(struct.pack("iiii", YANNI_MIGRATE, vmid, src, self.no))

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


# os.system("python3 /mnt/snake0/yanni-agent/cpu-monitor.py >& log-cpu.txt")

ward = ward_init("config-main.xml")
ward.run()
os.system("../killer.sh")
