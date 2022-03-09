import subprocess   
import os,time
import re
from rich.console import Console
from cli import *   
main = cli()

class Network():
    def __init__(self):
        c = subprocess.check_output(["ifconfig"],stderr=subprocess.DEVNULL)
        c = c.decode("utf-8")
        pat = re.compile('wlan[0-9]|eth[0-9]')
        op = pat.findall(c)
        interface = {}
        for intrfc in op:
            c = subprocess.check_output(["ifconfig",intrfc],stderr=subprocess.DEVNULL)
            c = c.decode("utf-8")
            intrfc = intrfc
            MACpat = re.compile('\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}')
            IPpat = re.compile('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')
            mac = MACpat.findall(c)
            ips = IPpat.findall(c)
            mac=mac+ips
            interface[intrfc]= mac
        self.interface = interface

    def refreshInterfaces(self):
        c = subprocess.check_output(["ifconfig"],stderr=subprocess.DEVNULL)
        c = c.decode("utf-8")
        pat = re.compile('wlan[0-9]|eth[0-9]')
        op = pat.findall(c)
        interface = {}
        for intrfc in op:
            c = subprocess.check_output(["ifconfig",intrfc],stderr=subprocess.DEVNULL)
            c = c.decode("utf-8")
            intrfc = intrfc
            MACpat = re.compile('\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}')
            IPpat = re.compile('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')
            mac = MACpat.findall(c)
            ips = IPpat.findall(c)
            mac=mac+ips
            interface[intrfc]= mac
        self.interface = interface

    def displayInterface(self):

        import time
        from rich.text import Text
        from rich.live import Live
        from rich.table import Table
        from rich.console import Console
        interface=self.interface
        print("\033[38;5;207m")
        iD=Text.from_ansi("\033[38;5;207mID")
        inter = Text.from_ansi("\033[38;5;207mINTERFACE")
        Mac = Text.from_ansi("\033[38;5;207mMAC")
        IP = Text.from_ansi("\033[38;5;207mIP")
        subnet = Text.from_ansi("\033[38;5;207mSUBNET")
        deflt = Text.from_ansi("\033[38;5;207mDEFAULT GATEWAY")
        CONNECTED = Text.from_ansi("\033[38;5;207mIS CONNECTED")
        table = Table(title="\033[1m\033[38;5;93mLIST OF NETWORK INTERFACES",style="yellow")
        table.add_column(iD,width=12,style="cyan")
        table.add_column(inter,width=12,style="cyan")
        table.add_column(Mac,width=20,style="cyan")
        table.add_column(CONNECTED,width=20,style="cyan")
        table.add_column(IP,width=14,style="cyan")
        table.add_column(subnet,width=20,style="cyan")
        table.add_column(deflt,width=20,style="cyan")
        
        
        Id=0
        console=Console(style="white on blue")  
        from time import sleep
        from rich.console import Console

        console = Console()

        for intrfc in interface:
            main.header()
            Id+=1
            attributes = interface[intrfc]
            isConnected = False
            MAC=attributes[0]
            IP='NA'
            SUBNET='NA'
            defaultGateway='NA'
            if len(attributes) == 4:
                isConnected = True
                IP=attributes[1]
                SUBNET=attributes[2]
                defaultGateway=attributes[3]

            if not(isConnected):
                table.add_row(str(Id),intrfc,MAC,str(isConnected),IP,SUBNET,defaultGateway)
                #print("Interface {} has MAC: {} , IP : {}, SUBNET : {}, DG : {} ".format(intrfc,MAC,IP,SUBNET,defaultGateway))
            else:
                table.add_row(str(Id),intrfc,MAC,str(isConnected),IP,SUBNET,defaultGateway)
                #print("Interface {} has MAC: {}".format(intrfc,MAC))
            console.print(table,justify='center')
            time.sleep(3)
                      
    def changeMacAdd(self,newMac,interface):
        c = subprocess.check_output(["ifconfig",interface],stderr=subprocess.DEVNULL)
        c = c.decode("utf-8")
        pat = re.compile('\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}')
        op = pat.findall(c)
        oldmac = str(op[0])
        subprocess.check_output(["ifconfig",interface,"down"],stderr=subprocess.DEVNULL)
        subprocess.check_output(["ifconfig",interface,"hw","ether",newMac],stderr=subprocess.DEVNULL)
        subprocess.check_output(["ifconfig",interface,"up"],stderr=subprocess.DEVNULL)
        print("\033[38;5;39m\033[1m\n                              MAC address changes successfully from \033[38;5;9m\033[1m{} \033[38;5;39m\033[1m to  \033[38;5;9m\033[1m{}".format(oldmac,newMac))
    
    def showActiceInterfaces(self):
        pass

    def showNetworkOptions(self):
        print("\n\n\033[38;5;13m                         1. Refresh Network Interface")
        print("                         2. Change Mac address of an interface")
        print("                         9. EXIT")

    def showNotesForInt(self):
        from rich.text import Text
        from rich.text import Text
        from rich.console import Console
        console= Console()
        above = Text.from_ansi("\033[38;5;208m[--]\033[38;5;15m \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \033[38;5;208m[--]")
        About = Text.from_ansi("\033[38;5;208m[--]                                            \033[1m     \033[38;5;9mNOTES:                                                \033[38;5;208m[--]")
        Author= Text.from_ansi("\033[38;5;208m[--]     \033[38;5;11m While Changing MAC address use Unicast address, that is first octet should be even               \033[38;5;208m[--]")
        Versio= Text.from_ansi("\033[38;5;208m[--]     \033[38;5;11m While Selecting interface make sure it is not in use, it will be disconnected                    \033[38;5;208m[--]")
        GitHub= Text.from_ansi("\033[38;5;208m[--]     \033[38;5;11m While Making a wordlist limit the alphabet usage, it might overflow the storage                  \033[38;5;208m[--]")
        Spacer= Text.from_ansi("\033[38;5;208m[--]     \033[38;5;11m HASHCAT would work only if you have GPU drivers are installed on your PC                         \033[38;5;208m[--]")
        plaint= Text.from_ansi("\033[38;5;208m[--]     \033[38;5;11m If you are running Ubuntu. Inet-tools will not be installed, install it manually                 \033[38;5;208m[--]")
        Divide= Text.from_ansi("\033[38;5;208m[--]\033[38;5;15m_______________________________________________________________________________________________________\033[38;5;208m[--]")
        console.print(above,justify="center")
        console.print(About,justify="center")
        console.print(Author,justify="center")
        console.print(Versio,justify="center")
        console.print(GitHub,justify="center")
        console.print(Spacer,justify="center")
        console.print(plaint,justify="center")
        console.print(Divide,justify="center")
        

