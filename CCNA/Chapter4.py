# Python 3.4.3
# Algorithms/CCNA/Chapter4.py

print	("Certified Cisco Network Associate\n"\
	 "Chapter 4 - Working with Cisco Equipment\n"\
	)

print	("CramSaver\n"\
	 "1. Local Device Management\n"\
         "C: Console\n"\
         "2. Connect router FastEthernet 0/0 directly to workstation NIC\n"\
         "E: Crossover\n"
        )

print	("Console Port Connection\n"\
         "special Rollover Cable\n"\
         "1:8, 2:7, 3:6, 4:5, 5:4, 6:3, 7:2, 8:1\n"\
         "One End = RJ-45 for console port\n"\
         "Other end = 9-pin serial connector\n"\
         "Terminal Application: HyperTerminal, Procomm, TeraTerm, SecureCRT\n"\
         "Baud Rate: 9600\nData Bits: 8\nParity: None\nStop Bits: 1\nFlow Control: None\n"
        )

print	("Device Memory Locations\n"\
	 "-----------------------\n"\
         "ROM[Read-only]: POST, bootstrap, ROMmon, rxboot microcode\n"\
	 "POST[Power-on self test: basic inventory // hardware test\n"\
	 "Bootstrap: find OS to load\n"\
	 "ROMmon   : min cmd set to xt to TFTP serv & rstr a missing/corrupted IOS image\n"\
	 "Rxboot   : mini-IOS used for IOS restore 4rm TFTP\n"\
	 "~~~~~~~~\n"\
	 "Flash >> store IOS\n"\
	 "Flash >> file storage >> IOS versions >> config backups\n"\
	 "Flash >> SIMM cards >> PCMCIA cards >> USB\n"\
	 "~~~~~~~~\n"\
	 "NVRAM >> nonvolatile RAM >> startup config >> configuration register value\n"\
	 "~~~~~~~~\n"\
	 "RAM   >> dyn learned info storage >> routing tables >> ARP cache >> buffers\n"\
	 "RAM   >> running config >> live IOS image\n"\
	)

print	("IOS Startup Process\n"\
	 "-------------------\n"\
	 "1.] POST RUN = config reg val\n"\
	 "2.] Find IOS\n"\
	 "3.] Load IOS to RAM\n"\
	 "4.] Find Config\n"\
	 "5.] Load config to RAM\n"\
	)

print	("Password Recovery\n"\
	 "-----------------\n"\
	 "0x2142 = skip startup config in NVRAM\n"\
	 "skips password that is stored in startup config\n"\
	 "Connect to console port, start Terminal, power Cycle Router\n"\
	 "when boot begins, hit the Break sequence.\n"\
	 "Ctrl+break, depends on terminal app\n"\
	 


