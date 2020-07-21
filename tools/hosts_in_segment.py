from scapy.all import *
from networks.utils import wait_for_threads, host_is_up


def find_host(host, timeout, retry, hosts):
    if host_is_up(host, timeout, retry=retry):
        hosts.append(host)


def get_hosts_in_segment(segment, timeout=7, retry=3):
    """
        Get all hosts inside a given segment.
        :param segment: segment to search on. e.g: 192.168.1.0
        :param timeout: (optional) timeout in seconds for host to reply. default=10
        :param retry: (optional) how many times it will send the ICMP packet if the host doesnt reply. default=3
        :return: list of hosts
        :rtype: list
    """

    list_bytes = segment.split(".")[:3]
    host = ".".join(list_bytes)
    threads_list = []
    hosts = []

    for i in range(1, 256):
        current_host = host + "." + str(i)
        t1 = Thread(target = find_host, args = (current_host, timeout, retry, hosts))
        t1.start()
        threads_list.append(t1)

    wait_for_threads(threads_list)
    return hosts
