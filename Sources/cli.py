import subprocess
from rich.progress import Progress
from rich.console import Console
class cli():
    def __init__(self):
        pass
    def header(self):      
        print("\033[1m\033[38;5;154m")
        #print("\033[48;5;236m\033[38;5;231mStack \033[38;5;208mAbuse\033[0;0m")
        subprocess.call("clear",shell=True)        
        subprocess.call("figlet -t -c -f slant.flf -k Netjector",shell=True)
        print("\033[0;0m\n")
    
    def aboutAuthor(self):
        from rich.text import Text
        from rich.console import Console
        console= Console()
        above = Text.from_ansi("\033[38;5;164m[--]\033[38;5;15m \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \033[38;5;164m[--]")
        About = Text.from_ansi("\033[38;5;164m[--] \033[38;5;45mGet into networks and create backdoors \033[38;5;164m[--]")
        Author= Text.from_ansi("\033[38;5;164m[--]          \033[38;5;45mAuthor: Shrey Bhonsle         \033[38;5;164m[--]")
        Versio= Text.from_ansi("\033[38;5;164m[--]             \033[38;5;45mVersion: 1.0.0             \033[38;5;164m[--]")
        GitHub= Text.from_ansi("\033[38;5;164m[--]   \033[38;5;45mFollow me on Github: \033[38;5;9m@shreybhonsle   \033[38;5;164m[--]")
        Spacer= Text.from_ansi("\033[38;5;164m[--]                                        \033[38;5;164m[--]")
        plaint= Text.from_ansi("\033[38;5;164m[--]  \033[38;5;15mSELECT A OPTION AND BEGIN EXPLOITING  \033[38;5;164m[--]")
        Divide= Text.from_ansi("\033[38;5;164m[--]\033[38;5;15m________________________________________\033[38;5;164m[--]")
        console.print(above,justify="center")
        console.print(About,justify="center")
        console.print(Author,justify="center")
        console.print(Versio,justify="center")
        console.print(GitHub,justify="center")
        console.print(Spacer,justify="center")
        console.print(plaint,justify="center")
        console.print(Divide,justify="center")

    def loadmodules(self):
        with Progress() as progress:
            print("\n\n\033[0;0m")
            task1 = progress.add_task("\033[1m\033[38;5;82m[cyan]                                Verifying Metasploit-framework :\033[0;0m", total=10)
            task2 = progress.add_task("\033[1m\033[38;5;82m[cyan]                                Verifying fatrat installation  :\033[0;0m", total=10)
            task3 = progress.add_task("\033[1m\033[38;5;82m[cyan]                                Loading modules                : \033[0;0m", total=10)
            import time
            progress.update(task1, advance=5)
            time.sleep(0.2)
            import os
            progress.update(task1, advance=5)
            time.sleep(1)
    
    def verifyInstallation(self):
        pass

    def showOptions(self):

        print("\n\n\033[38;5;178m                         1. Network Injection and Tools")
        print("                         2. Post Exploitation Attack")
    
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
        