# Network Tools

[![License](https://img.shields.io/github/license/adamalston/network-tools?color=black)](LICENSE)

Network tools based around scapy.

## Example Operations

<!-- ### ARP Spoofing

Perform arp spoofing attack on the given target.

```python
>>> import networks
>>> target = "192.168.1.40"
>>> gateway = "192.168.1.1"
>>> networks.arp_spoofing(target, gateway, interval=1, timeout=120)
``` -->

### Segment Hosts

Find hosts inside of a given segment.

```python
>>> import networks
>>> hosts = networks.get_hosts_in_segment("192.168.1.0")
>>> hosts
['192.168.1.1', '192.168.1.40', '192.168.1.23']
```

### Ping

Send ICMP packets to the given host.

```python
>>> import networks
>>> host_up = networks.ping("www.google.com", count=5, ttl=30, timeout=5)
>>> host_up
True
```

### Port Scanning

Perform port scanning on the given target.

```python
>>> import networks
>>> ports = networks.port_scanning("192.168.1.40", min_port=78, max_port=81, timeout=30)
>>> ports
{78: False, 79: False, 80: True, 81: False}
```

### Traceroute

Perform trace to the given host.

```python
>>> import networks
>>> stations = networks.trace("www.google.com", max_hops=20, timeout=5)
>>> stations
['192.168.1.1', '0.0.0.0', None, '172.18.9.214', '172.17.3.118', None, None, '209.85.241.75', '172.217.18.100']
```

---

This repository also contains a work-in-progress reimplementation of scapy ([scanner.py](tools/scanner.py)). [nmap.py](tools/nmap.py) and [nmap_auto.py](tools/nmap_auto.py) delve into the usability of this reimplmentation.

---

Includes contributions from Ben Gabay.