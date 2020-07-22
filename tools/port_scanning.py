from threading import Thread
from networks.utils import wait_for_threads
import collections
import socket

PACKET_TIMEOUT = 2


def print_status_message(port, is_open):
    if is_open:
        message = f"port {port} is open."
    else:
        message = f"port {port} is close."
    print(message)


def port_is_open(target, port, timeout=None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if timeout:
        sock.settimeout(timeout)
    result = sock.connect_ex((target, port))
    return True if result == 0 else False


def scan_port(target, port_number, ports, timeout=None, verbose=True):
    is_open = port_is_open(target, port_number, timeout)
    ports[port_number] = is_open
    if verbose:
        print_status_message(port_number, is_open)


def order_ports(ports):
    return dict(collections.OrderedDict(sorted(ports.items())))


def port_scanning(target, min_port=1, max_port=65536, timeout=None, verbose=True):
    """
        Perform port scanning on the given target.
        :param target: target to scan.
        :param min_port: (optional) the starting port. default=1
        :param max_port: (optional) the ending port. default=65536
        :param timeout: (optional) time in seconds to wait until a response from the target. default=None
        :param verbose: (optional) print output. default=True
        :return: dictionary of ports. e.g: { "22": False, "80": True }
        :rtype: dict
    """

    ports = {}
    scan_threads = []

    for current_port in range(min_port, max_port + 1):
        scan_thread = Thread(target=scan_port, args=(
            target, current_port, ports, timeout, verbose))
        scan_thread.start()
        scan_threads.append(scan_thread)
        current_port += 1
    wait_for_threads(scan_threads)
    return order_ports(ports)
