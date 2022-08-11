#!/usr/bin/env python3

def main():
    #prompt for hostname and lowercase the input
    hostname = input("What value should we set for hostname?")
    hostname = hostname.lower()


    if hostname == "mtg":
        print("The hostname was found to be MTG")
        print("The hostname matches expected config")
    print("Exiting the script")
main()
