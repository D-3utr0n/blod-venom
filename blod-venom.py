# Blod Venom copyrighted 2019
# coding by D-3utron
# Team Simpark Cyber Lite
##
import time
from platform import python_version
import os, sys, subprocess
os.system("clear")
    
def logo():
    os.system("figlet -f slant Blod Venom |lolcat")
    print "\033[36m==[ Tools Name : Blod Venom"
    print "\033[36m==[ Coded by : D-3utr0n"
    print "\033[36m==[ Version : 1.0.0"
    print "\033[36m==[ Team : Simpark cyber lite"
        
def rat():
    os.system(sys.executable + " modules/fexrat.py")   

def htmd():
    os.system(sys.executable + " modules/htmd.py")

def auto():
    os.system("php modules/autovisitor.php")

def base():
    os.system("python3 modules/md.py")

def spam():
    os.system("php modules/wa.php")

def gempa():
    os.system("php modules/inc.php")

def sc():
    os.system(sys.executable + " scdfc.py")

def mas():
    os.system("bash modules/mas.sh")

def dork():
    os.system("sh modules/dork.sh")

def sql():
   os.system("sh modules/sql.sh")

def log():
    print("""
\033[93mPlease select the Menu :
    01) Fex-Rat,create payload and listener
    02) Autovisitor Website
    03) Encoded and decoded Base64
    04) Spam Whatsapp
    05) Pendeteksi Gempa
    06) Script Deface Creator
    07) Webdav Mas Defacer
    08) Dork Generator
    09) HTML Downloader
    10) SQL Map\n""")

def logu():
    d = raw_input("blod-venom > ")
    if d == "01" or d == "1":
        rat()
    elif d == "02" or d == "2":
        auto()    
    elif d == "03" or d == "3":
        base()    
    elif d == "04" or d == "4":
        spam() 
    elif d == "05" or d == "5":
        gempa() 
    elif d == "06" or d == "6":
        sc() 
    elif d == "07" or d == "7":
        mas() 
    elif d == "08" or d == "8":
        dork()
    elif d == "09" or d == "9":
        htmd()
    elif d == "10" or d == "10":
        sql()    
    else:
        print "\nERROR: Wrong Input..."
        time.sleep(2)
        main()  
        
def main():
    os.system("clear")
    logo()
    log()
    logu()    
    
main()             