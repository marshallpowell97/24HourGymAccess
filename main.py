#!/usr/bin/env python

# Main program
import sqlite3
import os.path
from os import path
import sys


# Determine if user should be granted access
def determineAccess(str, c):
    c.execute('SELECT Name FROM Members WHERE Barcode=?', [str])
    name = c.fetchone()

    if name:
        print(name[0])
        return name[0]
    else:
        return 0
    
# Unlock the door
def unlockDoor(name):
    print("Access granted for " + name)

if __name__ == '__main__':

    # Load database for members
    if path.exists("AccessList.db"):
        conn = sqlite3.connect('AccessList.db')
        c = conn.cursor()
    else:
        print("ERROR - Did not load database")
        sys.exit()
    

    while True:

        barcode = input("Waiting for barcode to be scanned...")
        print("Scanned barcode is: " + barcode)
        name = determineAccess(barcode,c)
        if name:
            unlockDoor(name)
        else:
            print("Access NOT granted.")


