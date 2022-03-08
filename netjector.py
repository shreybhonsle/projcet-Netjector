from rich.progress import Progress
import subprocess
print("\033[1m\033[38;5;154m")
#print("\033[48;5;236m\033[38;5;231mStack \033[38;5;208mAbuse\033[0;0m")
subprocess.call("clear",shell=True)
subprocess.call("figlet -t -c -f slant.flf -k Netjector",shell=True)
print("\033[0;0m\n\n")
with Progress() as progress:
    task1 = progress.add_task("\033[1m\033[38;5;82m[cyan]Verifying installation :\033[0;0m", total=10)
    task3 = progress.add_task("\033[1m\033[38;5;82m[cyan]Loading modules        : \033[0;0m", total=10)
    import time
    progress.update(task1, advance=5)
    time.sleep(0.2)
    import os
    progress.update(task1, advance=5)
    time.sleep(0.2)

time.sleep(2)   
# from rich.console import Console
# from rich.highlighter import RegexHighlighter
# from rich.theme import Theme
# class EmailHighlighter(RegexHighlighter):
#     """Apply style to anything that looks like an email."""
#     base_style = "example."
#     highlights = [r"(?P<email>[\w-]+@([\w-]+\.)+[\w-]+)"]
# theme = Theme({"example.email": "bold magenta"})
# console = Console(highlighter=EmailHighlighter(), theme=theme)
# console.print("Send funds to money@example.org")