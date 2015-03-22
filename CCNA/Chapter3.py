print	"VLSM = Variable Length Subnet Masking\n"\
	"----\n"\
	"VLSM is important to modern IP networks because it allows us to identify each subnet by its mask number.\n"\
	"A routing protocol must be able to *advertise the mask for each subnet in the routing update* to support VLSM.\n"\
	"\n"\
	"DEFINITION= The capability to apply more than one subnet mask to a given class of addresses throughout a routed system.\n"\
	"Classful Protocols  ==	RIPv1 = Do not include subnet mask of advertised networks in their routing updates. Therefore cannot know of multiple mask length existence.\n"\
	"Classless Protocols ==	EIGRP, OSPF, RIPv2, IS-IS, BGP = includes the subnet mask during network advertisement of routing updates, therefore can publish\n"\
	"		        a level of detail that can support Variable Length Subnet Masking.\n"\
	"VLSM Push = The need for making networks the right size.\n"\
	"Subnetting logically creates appropriately sized networks, but the catch is that it cannot advertise the existence of multiple mask networks within the same system.\n"\
	"Routing Protocols cannot support this without VLSM. Can't com both /26 + /30 networks in same sys.\n"\
	"Prior to VLSM routing protocols, only one subnet mask within a sys.\n"\
	"\n"\
	"DEFINITION:\n"\
	"VLSM has the capability to apply more than one subnet mask to a given class of addresses throughout a routed system.\n"\
	"\nTWO MAIN ADVANTAGES TO VLSM:\n"\
	"1.) It makes network addressing more efficient.\n"\
	"2.) It provides the capability to perform route summarization.\n"\
	"**MUST KNOW THESE FOR EXAM\n"\
	"In point-to-point links, use /30 masks for 2 hosts [one on each end]\n"\
	"W/O VLSM, /26 masks for all networks, so point-point would result in 60 wasted IPs\n"\
	"W/ VLSM, /30 for point-point and /26 for actual networks\n"\
	"Efficient Addressing: Making networks the right size without depleting the limited address space / limiting future growth.\n"\
	"False: It is impossible to subnet a subnet.\n"\
	"How does VLSM make IP Addressing more efficient?\n"\
	"D: By allowing a routed system to include subnets of different mask lengths to suit requirements.\n"\

print 	"Route Summarization\n"\
	"-------------------\n"\
	"Summary for the following range of subnets: 172.20.32.0/24 to 172.20.47.0/24\n"\
	"Ans: 172.20.32.0/20 or 172.20.32.0 255.255.240.0\n"\
	"Why is summarization so important to an efficient routed system?\n"\
	"Summarization reduces the size of route tables, prevents route table instability due to flapping routes, and reduces the size of routing updates.\n"\
	"Subnetting: Process of lengthening the mask to create multiple smaller subnets from a single large network.\n"\
	"Route Summarization == DEFINITION = The Shortening of the mask to include several smaller networks into one larger network address.\n"\
	"As network grows, IP Route Tables become too large for routers to handle efficiently. Slower from congestion, packet drops, crashes.\n"\
	"Central Hub can send routing updates with all subnetsit knows about listed individually or via route summarization, it can send a single line.\n"\
	"Single Line contains 'send anything that starts w/ 192.168.0 to me'\n"\
	"Although both work, scalability is the issue at hand.\n"\
	"Route Summarization takes a set of contiguous networks/subnets and groups them together using a shorter subnet mask.\n"\
	"Advantages: \n1.) Reduces number of route table entries. \n2.)Reduces Router Load/Network Overhead : and \n3.)Hides System Instability behind Summary\n"\
	"Contiguous: 0, 16, 32, 48 // 192, 208, 224, 240 // both sets are contiguous with one within each other, but not with each sets other.\n"\
	"Summarization Guidelines:\n"\
	"1.) Design Networks w/ Summarization in mind. Group Contiguous Subnets together behind a router that will summarize them.\n"\
	"2.) Summarize into the core of your network. Bigger, Faster, Busier Routers. Deals w/ high volume traffic that is meant for all other networks.\n    Do not burden w/ big route tables\n"\
	"3.) Further from the core means the more detailed the routers will be with routing tables for directing traffic to proper destinations.\n"\
	"\n"\
	"Determining Summary Addresses\n"\
	"-----------------------------\n"\
	"Create Summary Addresses == Routing Protocols for Classless Configurations = Manual Process\n"\
	"Create Summary Addresses == Routing Protocols for Classful Configurations  = Auto   Process\n"\
	"For Classful Configs:\n"\
	"Treats any subnet as the classful address. But not that simple.\n"\
	"Summarization is the complete opposite of Subnetting == Supernetting.\n"\
	"Subnet   == lengthen mask by 1 bit = double the network\n"\
	"Supernet == Retract  mask by 1 bit = combine networks into groups that follow the binary increment numbers.\n"\
	"Interesting Octet: The octet in which the range of networks occur.\n"\
	"Where the summarization begins. Arrange int oct in binary form and find the common bits.\n"\
	"Draw the line between the common bits and the ranging bits. Everything to the left must be static, everything to the right can be dynamic.\n"\
	"Summarize by building a subnet mask that puts a 1 under all the common bits in the range and a 0 under everything else. {1L||0R} \n"\
	"Summary = IP Address + Subnet Mask\n"\
	"First Network ID = IP Address\n"\
	"Subnet Mask = Determined by the Boundary Line {1L||0R}\n"\
	"1.) 192.168.1.0/26 192.168.1.128/26\n"\
	"2.) B E F\n"\
	"\n"\
	"IPv6\n"\
	"----\n"\
	"1.] Which are valid IPv6 addresses?\n"\
	"[A, B, C, D, E]\n"\
	"Global Unicast, Unique Local, Link Local, Multicast, Anycast\n"\
	"IPv6 does not broadcast\n"\
	"2.] Valid IPv6 addresses?\n"\
	"All\n"\
	"2001 : 0db8 : 0000 : 0000 : ff00 : 0042 : 8329\n"\
	"2001 : db8 : 0 : 0 : 0 : ff00 : 42 : 8329\n"\
	"2001 : db8 : ff00 : 42 : 8329\n"\
	"0000 : 0000 : 0000 : 0000 : 0000 : 0000 : 0000 : 0001\n"\
	"::1\n"\
	"::192:168:1:1\n"\
	"3.] Valid IOS Command to apply IPv6 address to router interface?\n"\
	"interface fastethernet 1/0 ipv6 address 2001:AB00:00FF:1::/64 eui-64\n"\
	"IPv6 Addresses are 128 bit strings, allowing 3.4 x 10^38 possibilities.\n"\
	"IPv6 Address Allocation\n"\
	"-----------------------\n"\
	"ICANN [Internet Corporation for Assigned Network Numbers] are responsible for dividing up the IPv6 address space.\n"\
	"They do so w/ a better understanding of global demand and the luxury of an obscene amount of quantity to allocate.\n"\
	"1.] In order for an efficient Internet to work well, route summarization so that route tables arent oversized + slow.\n"\
	"2.] Route Summarization works best when every router is responsible for its branch.\n"\
	"3.] As smaller branches get closer to the core, the larger/more capable the router is {hardware-wise}.\n"\
	"4.] Allows a single router to advertise a summary for the yggdrasil.\n"\
	"5.] Ex. Major ISP branches out to smaller/enterprise ISPs.\n"\
	"6.] This way despite many changes beyond the core, the core remains intact/preserved.\n"\
	"\n"\
	"IPv6 Address Notation\n"\
	"---------------------\n"\
	"In binary, 4x longer than IPv4 addr;\n"\
	"Instead of dotted-decimals in four octets;IPv6 == hexadecimal [8 sets:4 chars] seperated by colons.\n"\
	"2201:0FA0:080B:2112:0000:0000:0000:0001\n"\
	"Each char == 4 bits\n"\
	"Several Truncation Methods to shorten address.\n"\
	"1.] Allowed to drop all LEADING 0's [zeroes]\n"\
	"2201:FA0:80B:2112:0:0:0:1\n"\
	"2.] Truncation Method: Condense contiguous groups of all-0 sets by representing them w/ '::'.\n"\
	"2201:FA0:80B:2112::1\n"\
	"3.] Only allowed to use the '::' condensation once per address.\n"\
	"Mask is not represented in hexadecimal characters || Identify the prefix length w/ slash notation.\n"\
	"Slash Notation == Identifies how many bits in network part.\n"\
	"\n"\
	"Types of IPv6 Addresses\n"\
	"-----------------------\n"\
	"Unicast: IPv6 == IPv4 // an IP assigned to a host interface. Source IP Packet or Destination IP Packets. Packet sent to unicast address goes to one host.\n"\
	"Global Unicast: Public, Registered IP Address. Internet routable, globally registered IPs that must be leased from an ISP.\n"\
	"Unique Local: EQV == IPv4 private address. Not registered w/ ISP nor Internet Routable.\n"\
	"Link Local: Every IPv6 interface gives itself a link-local address. Range is FE80::/10 Prefix + last 64-bits in EUI-64 Format.\n"\
	"	     Roughly equivalent to the Automatic Private IP Address [APIPA] range of 169.254.0.0/16\n"\
	"Multicast:  A Single IPv6 multicast address to multiple hosts so that a packet sent to the address may be delivered to all associated hosts at the same time.\n"\
	"	     IPv6 Multicast Addresses all start w/ the prefix FF00::/8\n"\
	"Anycast:    A single address that is assigned to multiple hosts. Similar to a multicast address, but that a packet sent via anycast will be delivered to the closest host. No special prefix\n"\
	"Broadcast:  Does not exist. [N/A]\n"\
	"**KNOW THE IPv6 ADDRESS TYPES**\n"\
	"\n"\
	"IPv6 Address Configuration\n"\
	"--------------------------\n"\
	"IPv6 protocol stack must be installed.\nMust upgrade router IOS to provide IPv6 support.\nAddress Assignment = [1-4 Options]"\
	"Concepts of Stateful vs. Stateless Configuration + EUI-64 address format.\n"\
	"IPv6: Can use DHCP to assign IP Addresses just like in IPv4. Admin must setup server w/ IPv6 scope to hand out addresses.\n"\
	"Minor diff when discovering + assigning, but net result [IPv4 vs IPv6] is the same.\n"\
	"Stateful Addressing: DHCP server keeps track of IPv6 addresses + associated hosts. {State of the Host[DHCP]}\n"\
	"IPv6 Dynamic Addressing = Stateless Autoconfiguration\n"\
	"Feature allows a host to choose + configure an address for itself.\n"\
	"Host --> Wants Address --> Learns what the /64 network prefix is on the local link --> appends MAC address[EUI-64]\n	 ==> generates 128-bit IPv6 address unique to Host.\n"\
	"EUI-64 Format --> 48-bit MAC Address + special pattern [FFFE] --> after first 24 bits (the six OUI chars) --> followed by the remaining 6 hex chars in the host MAC.\n"\
	"IPv6 Rule: 7th Bit in EUI-64 Address MUST BE 1. This is the marker that ensures modification of burned-in MAC address.\n"\
	"EUI-64 Address == </64 net_prefix>:[MAC+{7TH BIT == 1}]\n"\
	"1.] STATIC CONFIGURATION --> Admin assigns static IPv6 addresses to the hosts' NICs. ==> Admin's Responsibility to choose an address that will function + be valid in the hosts' network.\n"\
	"2.] STATIC CONFIGURATION w/ EUI-64 --> Admin manually configures the address w/ local /64 net_prefix + host's MAC[EUI-64] \n"\
	"3.] DYNAMIC CONFIGURATION w/ DHCP to ASSIGN 128-BIT ADDRESS --> Host is set to obtain its Address from DHCP ==> DHCP Server is setup to handout IPv6 addresses from a scope.\n"\
	"4.] DYNAMIC CONFIGURATION w/ STATELESS AUTOCONFIG w/ EUI-64 --> Host obtains address automatically --> DHCP server ( 1 or 0 ) ==> if 1, only informs host of the /64 local net-prefix.\n"\
	"\n"\
	"IPv6 Router Configuration\n"\
	"-------------------------\n"\
	"ios cmd=> interface fastethernet 1/0\n"\
	"ios cmd=> ipv6 address 2001:AB00:00FF:1::/64 eui-64\n"\
	"'eui-64' switch ==> tells router to figure out its own EUI-64 address to follow the /64 prefix provided. w/o it, you need to provide a full 128-bit address... \n"\
	"ios cmd=> show ipv6 interface || 'cmd to verify router config'\n"\
	"\n"\
	"IPv6 Features\n"\
	"-------------\n"\
	"IPsec: Support is built-in [IPv6]. If configured, every packet sent/recv can be protected by IPsec transport for IPv6 hosts.\n"\
	"Mobility: Built-in, but not mandatory as some hosts will not be mobile.\n"\
	"Fixed header size: IPv6 header is fixed @ 40 bytes or 320 bits.\n"\
	"\n"\
	"\n"\
	"\n"\
	"\n"\
	"\n"\
	"\n"\
	"\n"\
	"\n"\
	"\n"\
	"\n"\
	"\n"\
	"\n"\
	"\n"\
	"\n"\
	"\n"\

