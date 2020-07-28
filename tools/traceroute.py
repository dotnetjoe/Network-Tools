from scapy.all import *


PACKET_TYPE = "echo-request"
TTL_EXCEED = 11
PACKET_VERBOSE = 0


def get_ip_from_packet(packet):
    return packet[IP].src


def reach_host(response_packet):
    return response_packet[ICMP].type != TTL_EXCEED


def seconds_to_ms(seconds):
    return seconds / 60 * 1000


def hop(address, ttl, timeout):
    my_packet = IP(dst=address, ttl=ttl) / ICMP(type=PACKET_TYPE)
    return sr1(my_packet, timeout=timeout, verbose=PACKET_VERBOSE)


def print_status_message(success, ttl, response_time=None, ip=None):
    if success:
        response_ms_time = seconds_to_ms(response_time)
        message = f"{ttl})  {response_ms_time} ms {ip}"
    else:
        message = f"{ttl}) Request Time Out."

    print(message)


def trace(host, max_hops=30, timeout=5, verbose=True):
    """
        Perform trace to the given host.
        :param host: host to trace.
        :param max_hops: (optional) maximum number of hops to search for target. default=None
        :param timeout: (optional) wait timeout seconds for each reply. default=5
        :param verbose: (optional) print output. default=True
        :return: list of the hops
        :rtype: list
    """

    ttl = 1
    stations = []

    while ttl <= max_hops:
        start_time = time.time()
        response_packet = hop(host, ttl, timeout)
        final_time = time.time() - start_time

        if response_packet:
            ip = get_ip_from_packet(response_packet)
            stations.append(ip)

            if verbose:
                print_status_message(True, ttl, final_time, ip)
            if reach_host(response_packet):
                break
        else:
            stations.append(None)

            if verbose:
                print_status_message(False, ttl)
        ttl += 1

    return stations
