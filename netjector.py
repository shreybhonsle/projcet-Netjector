import subprocess
import sys
sys.path.insert(0, '/root/Projects/Project-Netjector/Netjector/Sources')
from networking import *
from cli import *

main = cli()
main.header()
main.aboutAuthor()  
main.loadmodules()
network = Network()
from rich.console import Console
console = Console()
#Verifying installation 

while True:
    main.header()
    main.aboutAuthor()
    main.showOptions()
    choice=int(input("\n\n                         Enter Your Choice : "))
    if choice == 1: 
        while True: 
            main.header()    
            network.showNotesForInt() 
            network.showNetworkOptions()
            Networkchoice=int(input("\n\n\n                         Enter Your Choice : "))
            if Networkchoice == 1:
                main.header()
                network.refreshInterfaces()
                network.displayInterface()
                time.sleep(5)
            elif Networkchoice == 2:
                main.header()
                network.displayInterface()
                interface = str(input("\033[38;5;190m\033[1m                              Enter the name Interface to change MAC: "))
                mac = str(input("                              Enter the new MAC address: "))
                network.changeMacAdd(mac,interface)
                time.sleep(5)
            else:
                break
                
