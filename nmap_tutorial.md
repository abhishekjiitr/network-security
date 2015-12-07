# nmap-tutorial
## Introduction
Network Mapped (Nmap) is a network scanning and host detection tool that is very useful during steps of penetration testing. It is a very powerful tool for network analysis.
It is particularly useful as it can
  * Detect the live hosts on network (host discovery)
  * Detect the open ports on the host (port discovery)
  * Detect the software and the version to the respective port(service discovery)
  * Detect the operating system and hardware address
  * Detect the vulnerability and security holes

## Commands:
Basic Command:
```
nmap target
# nmap target.com
# nmap 192.168.1.1
```
To scan the entire subnet:
```
nmap target/cdir
nmap 192.168.1.1/24
```
To scan multiple targets
```
nmap target1 target2 target3
```
