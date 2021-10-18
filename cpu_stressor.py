#!/bin/python3

import statistics
import sys
import time

INTERVAL = 2

NCPU_PER_NODE = 80


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


# Return the maximum counter per second
def warmup():
    cpu_counter = 0

    time_start = time.time()
    while (time.time() < time_start + 5):
        cpu_counter += 1

    return int(cpu_counter / 5)


# Return the influenced computation power
def simulate_cpuload(util, max_counter):
    assert (0 <= util <= 100)

    cpu_counter = 0

    for i in range(INTERVAL):
        time_start = time.time()
        time.sleep(1.0 * (100 - util) / 100)
        while time.time() < time_start + 1:
            cpu_counter += 1

    return cpu_counter / (max_counter * INTERVAL * util / 100)


def do_simulate(q, max_counter):
    degradation = []
    while True:
        load = q.get()
        if load < 0:
            break
        d = simulate_cpuload(load, max_counter)
        degradation.append(d)
    print(statistics.mean(degradation))


# if len(sys.argv) != 2:
#     print("Usage: python3 %s [machine_id (m_1932,m_1933,m_1934,m_1935)]" %
#           (sys.argv[0]))
#     exit(1)

# this_machine_id = sys.argv[1]


def read_util(this_machine_id):
    data = []
    high = 0
    fac = 1.8
    time_fac = 6

    with open("scripts/machine_usage_short.csv", "r") as f:
        line = f.readline()
        cpu_before = 0
        before = 0
        i = 0
        while len(line) > 0:
            array = line.split(",")
            machine_id = array[0]
            if not machine_id == this_machine_id:
                line = f.readline()
                continue

            # get CPU utilization
            cpu_util_percent = int(int(array[2]) * fac)
            if cpu_util_percent > 100:
                cpu_util_percent = 100

            # get elapse time
            now = int(array[1])
            elapse = int((now - before) / 10)
            if elapse >= time_fac:
                elapse = elapse / time_fac
            else:
                elapse = 1
            if elapse > 20:
                elapse = 20

            # go to data
            if before != 0:
                data.append((cpu_before, int(elapse)))
                if cpu_before > 70:
                    high = high + 1
            cpu_before = cpu_util_percent
            before = now

            line = f.readline()
    cpu_data = []
    max_i = 500
    i = 0
    total_time = 0
    exit_flag = False
    for k in data:
        for j in range(k[1]):
            # print(str(i) + ": " + str(k[0]))
            # print(str(k[0]))
            cpu_data.append(k[0])
            i = i + 1
            total_time = total_time + 1
            if i > max_i:
                exit_flag = True
                break
        if exit_flag:
            break
    # print("total time %ds = %fmin" % (total_time * INTERVAL, INTERVAL * total_time / 60.0))
    return cpu_data


data1 = read_util("m_1932")
data2 = read_util("m_1934")

violation_load = 80

data = [data1, data2]


def average(arr):
    return sum(arr) / len(arr) if len(arr) else 0


def find_busiest_node(t):
    busiest = -1
    busiest_load = -1.0

    for i in range(len(data)):
        if busiest_load < data[i][t]:
            busiest_load = data[i][t]
            busiest = i

    cpu5 = 0
    if t >= 5:
        cpu5 = average(data[busiest][t - 4:t + 1])

    cpu15 = 0
    if t >= 15:
        cpu15 = average(data[busiest][t - 14:t + 1])

    if busiest_load > violation_load:
        if busiest_load >= cpu5 >= \
                cpu15:
            print("Found node %d busy with %d" % (busiest, busiest_load))
            # print("Busy %s" % str(self.nodes[busiest].utils[-1]))
            return busiest, busiest_load
    return -1, -1


# new
def find_idlest_node(t):
    idlest = -1
    idlest_load = sys.float_info.max

    for i in range(len(data)):
        if idlest_load > data[i][t]:
            idlest_load = data[i][t]
            idlest = i

    print("Found node %d idle with %d" % (idlest, idlest_load))
    # print("Idle %s" % str(self.nodes[idlest].utils[-1]))
    return idlest, idlest_load


def try_migrate(t):
    print("-----------------")
    print("t = %d" % t)
    src, src_load = find_busiest_node(t)
    if src == -1:
        return

    dst, dst_load = find_idlest_node(t)
    if dst is not src:
        # vm0 = self.select_next_vm_from_node(src)
        # if vm0 is None:
        #     print("No migratable VMs found on Node%d" % src)
        #     return
        vm_load = 100 * 2 / NCPU_PER_NODE

        i = 0
        while dst_load + i * vm_load <= src_load:
            i = i + 1
        i = i - 1
        print("%d VMs needed to be migrated from %d to %d" % (i, src, dst))

        # j = 0
        # while vm0 is not None and i is not 0:
        #     j = j + 1
        #     i = i - 1
        #     print("VM%d migrating from %d to %d" % (vm0.vmid, src, dst))
        #     print("%s--------------- Migration Start --------------%s"
        #         % (bcolors.WARNING, bcolors.DEFAULT))
        #     self.migrate(vm0.vmid, src, dst)
        #     vm0 = self.select_next_vm_from_node(src)
        #
        # print("src_load %f dst_load %f vm %f" %
        #       (src_load, dst_load, j * vm_load))


for i in range(len(data[0])):
    try_migrate(i)

# max_counter = warmup()
# qlist = []
# plist = []
# for i in range(os.cpu_count()):
#     q = Queue()
#     qlist.append(q)
#     p = Process(target=do_simulate, args=(q, max_counter))
#     plist.append(p)

# for p in plist:
#     p.start()

# cnt = 0
# for util in cpu_data:
#     cnt += 1
#     print("Simulate %d%%" % util)
#     for i in range(os.cpu_count()):
#         qlist[i].put(util)

#     time.sleep(INTERVAL)

# for i in range(os.cpu_count()):
#     qlist[i].put(-1)


# for p in plist:
#     p.join()


# os.system('sudo /mnt/snake0/killer.sh')
