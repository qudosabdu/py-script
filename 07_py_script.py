# scapy library is used to create packets
# import scapy
# # Create an IP packet
import scapy.all as scapy

# define the destination IP address
target_ip = 'www.google.com'

#craft the IP packet
ip_packet = scapy.IP(dst=target_ip) # create an IP packet with the destination IP address

# send the  AND receive a response
response = scapy.sr1(ip_packet) # send the packet and receive a response

#check if a response was received
if response:
    print(f"Received response from {response.src}")
else:
    print("No response received")
    
    
# The scapy library is used to create an IP packet and send it to the specified destination IP address. The response is then checked to see if a response was received. If a response was received, the source IP address of the response is printed. Otherwise, an error message is printed.
# The scapy library is used to create packets and send them to the network. In this example, an IP packet is created with the destination IP address and sent to the network. The response is then checked to see if a response was received. If a response was received, the source IP address of the response is printed. Otherwise, an error message is printed.
# The scapy library is used to create an IP packet and send it to the specified destination IP address. The response is then checked to see if a response was received. If a response was received, the source IP address of the response is printed. Otherwise, an error message is printed.
