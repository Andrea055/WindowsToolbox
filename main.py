from colorama import init
from colorama import Fore, Back, Style
import subprocess, sys
init()
n=0
def inizio():
    print(Fore.BLUE + 'Windows Toolbox')
    print(Fore.RED + '- Action Center and Notification')
    print(Fore.WHITE + "1 Enable action center and notification")
    print("2 Disable action center and notification")
    print(Fore.RED+ "- Cortana");
    print(Fore.WHITE+ "3 Enable Cortana")
    print(Fore.WHITE + "4 Disable Cortana")
    print(Fore.RED + "- Print Spooler")
    print(Fore.WHITE + "5 Enable")
    print(Fore.WHITE + "6 Disable")
    print(Fore.RED + "- Windows Hello")
    print(Fore.WHITE + "7 Enable")
    print(Fore.WHITE + "8 Disable")
    print(Fore.RED + "- Misc")
    print(Fore.WHITE + "17 WSL2")
    print(Fore.WHITE + "18 Modify the context menu with Easy Context Menu")
    print(Fore.WHITE + "9 Set a custom pagefile(not more than 16Gb raccomanded)")
    print(Fore.WHITE + "10 Stop windows update")
    print(Fore.WHITE + "18 Change CMD color scheme")
    print(Fore.RED+ "- Microsoft Store")
    print(Fore.WHITE+ "11 Install Microsoft Store")
    print(Fore.WHITE + "12 Remove Microsoft Store")
    print(Fore.RED + "- New app of Windows 11 for 10")
    print(Fore.WHITE + "13 Microsoft paint new design")
    print(Fore.WHITE + "14 Notepad new design")
    print(Fore.RED + "- Function for Windows 11")
    print(Fore.WHITE + "15 Old Taskbar,explorer and context menu for windows 11")
    print(Fore.WHITE + "16 Windows subsystem for Android")
    print(Fore.RED + "- 18 Install Application")
    print(Fore.RED + "- Tweaking")
    print(Fore.WHITE + "19 Disable HPET")
    print(Fore.WHITE + "20 Enable HPET")
    print(Fore.WHITE + "21 HPET: Enable  / Dynamictick: Yes / Tscsync: Enhanced")
    print(Fore.WHITE + "22 HPET: Disable / Dynamictick: Yes / Tscsync: Enhanced")
    print(Fore.WHITE + "23 Enable Ultimate performance power")
    print(Fore.WHITE + "24 Enable Hardware-accelerated GPU scheduling")
    scelta=input(Fore.GREEN + "Select an option:")
    if scelta=="17":
        print(Fore.WHITE + "1 Ubuntu")
        print(Fore.WHITE + "2 Ubuntu 16.04")
        print(Fore.WHITE + "3 Ubuntu 18.04")
        print(Fore.WHITE + "4 Ubuntu 20.04")
        print(Fore.CYAN + "5 Kali Linux")
        print(Fore.GREEN + "6 OpenSUSE")
        print(Fore.GREEN + "7 SLES")
        linux=input("Pick a distribution")
        match linux:
            case "1":
                p = subprocess.Popen(["powershell.exe",
                                      "WSL/ubuntu.ps1"],
                                     stdout=sys.stdout)
                p.communicate()
            case "2":
                p = subprocess.Popen(["powershell.exe",
                                      "WSL/ubuntu16.ps1"],
                                     stdout=sys.stdout)
                p.communicate()
            case "3":
                p = subprocess.Popen(["powershell.exe",
                                      "WSL/ubuntu18.ps1"],
                                     stdout=sys.stdout)
                p.communicate()
            case "4":
                p = subprocess.Popen(["powershell.exe",
                                      "WSL/ubuntu20.ps1"],
                                     stdout=sys.stdout)
                p.communicate()
            case "5":
                p = subprocess.Popen(["powershell.exe",
                                      "WSL/kali.ps1"],
                                     stdout=sys.stdout)
                p.communicate()
            case "6":
                p = subprocess.Popen(["powershell.exe",
                                      "WSL/opensuse.ps1"],
                                     stdout=sys.stdout)
                p.communicate()
            case "7":
                p = subprocess.Popen(["powershell.exe",
                                      "WSL/sles.ps1"],
                                     stdout=sys.stdout)
                p.communicate()
    if scelta=="18":
        package=input("Insert the name of the package or of file:")

while n==0:
    inizio()

