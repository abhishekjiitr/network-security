# nmap-tutorial
## Introduction
Network Mapped (Nmap) is a network scanning and host detection tool that is very useful during steps of penetration testing. It is a very powerful tool for network analysis.
It is particularly useful as it can
  * Detect the live hosts on network (host discovery)
  * Detect the open ports on the host (port discovery)
  * Detect the software and the version to the respective port(service discovery)
  * Detect the operating system and hardware address
  * Detect the vulnerability and security holes

## Basic Commands:
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
To scan a range of IPs:
```
nmap target-100
# nmap 192.168.1.1-100
```
To see list of report of all hosts scanned, add a -sL parameter:
```
nmap -sL target/cdir
# nmap -sL 192.168.1.1/24
```
To scan specific ports:
```
nmap -p80,21,23 192.168.1.1
```
## nmap scanning techniques
### TCP SYN Scan
```
nmap -sS 192.168.1.1
```

### TCP connect scan
```
nmap -sT 192.168.1.1
```

### UDP Scan
```
nmap -sU 192.168.1.1
```

### Ping Scan
```
nmap -sP 192.168.1.1
```

### Version Detection
```
nmap -sV 192.168.1.1
```

### Idle Scan
```
nmap -sl zombie_host target_host
```

## OS Detection
just pass a paramater -O
```
nmap -O 192.168.1.1
```
pass another parameter -PN to make sure you dont send any ping request to host
```
nmap -O -PN 192.168.1.1
```
