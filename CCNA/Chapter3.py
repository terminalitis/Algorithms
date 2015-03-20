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
	"\n"\
	"\n"\






