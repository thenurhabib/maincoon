#! /usr/bin/python3
# Author Md. nur habib

# Import Some Modules and Functions
import colors
import banner
from os import system
from time import sleep
from getpass import getpass
from classes import AllTools
from loginCrd import loginCredentials

# Print Banner
banner.toolBanner()

# Login System
try:
    username = input("Enter Login Username : ")
    password = getpass("Enter Login Password : ")
    if username == loginCredentials[0] and loginCredentials[1]:
        print("Login Successfull.\n Please Wait a Second...")
        sleep(2)
        system("clear")
        banner.toolBanner()
        # Menu/Options
        menu = print(
            f""" {colors.blue}
                ALl Tools (Select a Number)
--------------------------------------------------------------
   01. Whois            : Get Website Whois Information.     
   02. Torrent          : Get Torrent Information Via IP Address.             
   03. Shodan IP Info   : IP Information Gathering From Shodan
   04. Image Search     : Reverse Image Search.
   05. Proxy Info       : Get Proxy Server Information.
   06. Port Scanning    : Port Scanning.
   07. Number Lookup    : Phone Number Information Gathering.
   08. DNS lookup       : Get Information About DNS.
   09. MAC Lookup       : Get Information About Mac Address.
   10. DNS Dump         : DNS Dump.
   11. Censys Lookup    : Censys Information Gathering from IP Address.
   12. Mail Lookup      : Get Mail Information.
--------------------------------------------------------------"""
        )

        # call Functions.
        try:
            menuInput = input("Select a Number : ")
            if "1" == menuInput or "01" == menuInput:
                AllmenuInput.whoisInformation()
            elif "2" == menuInput or "02" == menuInput:
                AllmenuInput.torrent()
            elif "3" == menuInput or "03" == menuInput:
                AllmenuInput.shodanipInformation()
            elif "4" == menuInput or "04" == menuInput:
                AllmenuInput.reverseImageSearch()
            elif "5" == menuInput or "05" == menuInput:
                AllmenuInput.profyInformation()
            elif "6" == menuInput or "06" == menuInput:
                AllmenuInput.PortScanning()
            elif "7" == menuInput or "07" == menuInput:
                AllmenuInput.phoneNumberInformation()
            elif "8" == menuInput or "08" == menuInput:
                AllmenuInput.dnslookup()
            elif "9" == menuInput or "09" == menuInput:
                AllmenuInput.MacAddressLookup()
            elif "10" == menuInput:
                AllmenuInput.dnsDump()
            elif "11" == menuInput:
                AllmenuInput.censysipinformation()
            elif "12" == menuInput:
                AllmenuInput.mailInformation()
            else:
                print("Enter a Valid Number between 1 and 12.")
        except Exception as err:
            print(f"An Error Occurred : {err}, Try Again.")
    # If login information is wrong
    else:
        print("Wrong Login Information.")

except Exception as error:
    print(f"You Get an Error : {error}")
