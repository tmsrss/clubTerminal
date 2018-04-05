import time
import csv
import os
from colorama import *
memname = []
memid = []
memtype = []
memyears = []
init(autoreset = True)
def start():
    loadCSV()
    terminal()
def loadCSV():
    if os.path.isfile("members.csv"):
        csv_in = open('members.csv', 'r')
        myreader = csv.reader(csv_in)
        for row in myreader:
            memberid, membername, membertype, memberyears = row
            memid.append(int(memberid))
            memname.append(membername)
            memtype.append(membertype)
            memyears.append(int(memberyears))
    elif not os.path.isfile("members.csv"):
        writeCSV()
def writeCSV():
    members = open("members.csv", "w", newline='')
    mywriter=csv.writer(members)
    r = zip(memid, memname, memtype, memyears)
    mywriter.writerows(r)
    members.close()
def newUser():
    print(Fore.GREEN + "------------------------------------------------")
    numreg = int(input("enter the number of people that you would like to register"))
    for a in range (numreg):
        name = str(input("input member name"))
        memname.append(name)
        if len(memid) != 0:
            count = max(memid)+1
            memid.append(int(count))
        if len(memid) == 0:
            count = 1
            memid.append(int(count))
        mtype = input("enter membership type, full or half? [f/h]")
        if mtype == "f":
            mtypeappend = "full"
            memtype.append(mtypeappend)
        elif mtype == "h":
            mtypeappend = "half"
            memtype.append(mtypeappend)
        nyears = int(input("Enter number of year that member is in the club"))
        memyears.append(nyears)
        writeCSV()
        print("NAME =", name)
        print("ID =", count)
        print("MEMBERSHIP TYPE =", mtype)
        print("MEMBER YEARS =", nyears)
        print(Fore.GREEN + "------------------------------------------------")
    writeCSV()
    print("The", numreg, "users have been succesfully added")
    input("Press Enter to continue...")
    terminal()
def delUser():
    print(Fore.GREEN + "------------------------------------------------")
    numdel = int(input("enter the number of people that you would like to delete"))
    for b in range (numdel):
        userid = int(input("input member id"))
        location = memid.index(userid)
        sure = input("are you sure to delete all of the records of user id num = " + str(userid) + " ? [y/n]")
        if sure == "y":
            memname.remove(memname[location])
            memid.remove(memid[location])
            memtype.remove(memtype[location])
            memyears.remove(memyears[location])
            writeCSV()
            print("User ID =", userid, "has been succesfully deleted")
        elif sure == "n":
            if numdel == 1:
                print("Deleting user action terminated")
            elif numdel != 1:
                print("Deleting users action terminated")
            print("No data has been deleted")
        print(Fore.GREEN + "-------------------------------------------------")
    input("Press Enter to continue...")
    terminal()
def repNAMEUser():
    print(Fore.GREEN + "------------------------------------------------")
    username = str(input("Enter user's name to see its report"))
    location = memname.index(username)
    print("ID =", memid[location])
    print("NAME =", memname[location])
    print("MEMBERSHIP TYPE =", memtype[location])
    print("YEARS =", memyears[location])
    print(Fore.GREEN + "------------------------------------------------")
    input("Press Enter to continue...")
    terminal()
def repIDUser():
    print(Fore.GREEN + "------------------------------------------------")
    userid = int(input("Enter user id to see its report"))
    location = memid.index(userid)
    print("NAME =", memname[location])
    print("ID =", memid[location])
    print("MEMBERSHIP TYPE =", memtype[location])
    print("YEARS =", memyears[location])
    print(Fore.GREEN + "------------------------------------------------")
    input("Press Enter to continue...")
    terminal()
def memCost():
    print(Fore.GREEN + "------------------------------------------------")
    userid = int(input("enter user id to see its payments"))
    location = memid.index(userid)
    type = memtype[location]
    if type == "full":
        cost = int(memyears[location]) * 20000
    elif type == "half":
        cost = int(memyears[location]) * 12000
    print("NAME =",memname[location])
    print("ID =",memid[location])
    print("MEMBERSHIP TYPE =",memtype[location])
    print("YEARS =",memyears[location])
    print("Total payments =", cost, "Baht")
    print(Fore.GREEN + "------------------------------------------------")
    input("Press Enter to continue...")
    terminal()
def terminal():
    print(Fore.GREEN + "-------------------------------------------------")
    time.sleep(0.1)
    print("Welcome to The Club terminal")
    time.sleep(0.1)
    print("Please select your desired action from below")
    time.sleep(0.1)
    print(Fore.GREEN + "-------------------------------------------------")
    print(Fore.RED + "0 = exit")
    time.sleep(0.1)
    print(Fore.YELLOW + "1 = add new member")
    time.sleep(0.1)
    print(Fore.GREEN + "2 = delete member")
    time.sleep(0.1)
    print(Fore.CYAN + "3 = member ID report")
    time.sleep(0.1)
    print(Fore.BLUE + "4 = user name report")
    time.sleep(0.1)
    print(Fore.MAGENTA + "5 = membership costs report")
    time.sleep(0.1)
    print(Fore.GREEN + "-------------------------------------------------")
    time.sleep(0.1)
    direction = input("Enter your choice's number")
    if direction == "0":
        exit()
    elif direction == "1":
        newUser()
    elif direction == "2":
        delUser()
    elif direction == "3":
        repIDUser()
    elif direction == "4":
        repNAMEUser()
    elif direction == "5":
        memCost()
start()
