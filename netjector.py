#!/usr/bin/env python

import subprocess
import sys
sys.path.insert(0, '/root/Projects/Project-Netjector/Netjector/Sources')
from networking import *
from cli import *
import signal


def signal_handler(sig, frame):
    print("\033[1m\033[38;5;154m")
    subprocess.call("clear",shell=True)        
    print('\n')
    subprocess.call("figlet -t -c -f pagga.tlf -k [+] Thank You for using netjector",shell=True)
    from rich.text import Text
    from rich.console import Console
    console= Console()
    print('\n')
    above = Text.from_ansi("\033[38;5;164m[--]\033[38;5;15m \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \033[38;5;164m[--]")
    About = Text.from_ansi("\033[38;5;164m[--] \033[38;5;45mGet into networks and create backdoors \033[38;5;164m[--]")
    Author= Text.from_ansi("\033[38;5;164m[--]          \033[38;5;45mAuthor: Shrey Bhonsle         \033[38;5;164m[--]")
    Versio= Text.from_ansi("\033[38;5;164m[--]             \033[38;5;45mVersion: 1.0.0             \033[38;5;164m[--]")
    GitHub= Text.from_ansi("\033[38;5;164m[--]   \033[38;5;45mFollow me on Github: \033[38;5;9m@shreybhonsle   \033[38;5;164m[--]")
    Spacer= Text.from_ansi("\033[38;5;164m[--]                                        \033[38;5;164m[--]")
    linked= Text.from_ansi("\033[38;5;164m[--] \033[38;5;45mFollow me on Linked_in: \033[38;5;9m@shrey-bhonsle \033[38;5;164m[--]")
    Divide= Text.from_ansi("\033[38;5;164m[--]\033[38;5;15m________________________________________\033[38;5;164m[--]")
    console.print(above,justify="center")
    console.print(About,justify="center")
    console.print(Author,justify="center")
    console.print(Versio,justify="center")
    console.print(GitHub,justify="center")
    console.print(linked,justify="center")
  

    console.print(Divide,justify="center")
    print("\033[0;0m\n")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

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
            elif Networkchoice == 3:
                main.header()
                
            else:
                break
                
