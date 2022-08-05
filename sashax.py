import sys
import os
from os import system as ex

userpath = os.path.expanduser("~")
print(userpath)

print("SasHax is loading...")
print("Note that SasHax may need administrative privileges to run. Please enter your password to continue:")
os.system("sudo echo Authenticated...")
print("SasHax is ready to use!")
query = input("Press enter to continue...")
while query != "Q":
    print("Please enter a command:")
    print("D - Duplicate a save")
    print("C - Modify a save")
    print("Q - Quit")
    query = input("Command: ")
    if query == "D":
        print("WARNING! When duplicating a save, it replaces the original save with the new save. It may also remove backups. Please only duplicate to saves you know you don't need anymore.")
        print("Please enter the number of the save you wish to duplicate:")
        savefrom = input("Save: ")
        if savefrom == 1:
            savefrom = ""
        print("Please enter the number of the save you wish to replace:")
        saveto = input("Save: ")
        if saveto == 1:
            saveto = ""
        print("Duplicating save...")
        ex(f"cp -r {userpath}/Library/Containers/com.rac7.SneakySasquatchMac/Data/Library/Application Support/com.rac7.SneakySasquatchMac/default{savefrom} {userpath}/Library/Containers/com.rac7.SneakySasquatchMac/Data/Library/Application Support/com.rac7.SneakySasquatchMac/default{saveto}")
        print("Save duplicated!")
    if query == "C":
        print("Please enter a modification:")
        print("C - Coins")
        print("L - Lumber")
        # print("I - Inventory")
        # print("D - Disguise")
        print("E - Exit")
        modification = input("Modification: ")
        if modification == "C":
            print("Please enter the number of the save you wish to modify:")
            save = input("Save: ")
            if save == 1:
                save = ""
            print("Please enter the amount of coins you wish to have:")
            coins = input("Coins: ")
            print("Modifying save...")
            with open(f"{userpath}/Library/Containers/com.rac7.SneakySasquatchMac/Data/Library/Application Support/com.rac7.SneakySasquatchMac/default{save}/sasquatch.stuff", "r") as f:
                line = f.readline()
            digits = 0
            index = line.find("coins")+7
            hitnext = False
            while not hitnext:
                try:
                    int(line[index+digits])
                    digits += 1
                except:
                    hitnext = True
            # print(line[index:index+digits])
            beforecoins = int(line[index:index+digits])
            ls = list(line)
            ls[index:index+digits+1] = str(coins)
            line = "".join(ls)
            with open(f"{userpath}/Library/Containers/com.rac7.SneakySasquatchMac/Data/Library/Application Support/com.rac7.SneakySasquatchMac/default{save}/sasquatch.stuff", "w") as f:
                f.write(line)
            print("Save successfully modified!")
        elif modification == "L":
            print("Please enter the number of the save you wish to modify:")
            save = input("Save: ")
            if save == 1:
                save = ""
            print("Please enter the amount of lumber you wish to have:")
            lumber = input("Lumber: ")
            print("Modifying save...")
            with open(f"{userpath}/Library/Containers/com.rac7.SneakySasquatchMac/Data/Library/Application Support/com.rac7.SneakySasquatchMac/default{save}/sasquatch.stuff", "r") as f:
                line = f.readline()
            digits = 0
            index = line.find("lumber")+8
            hitnext = False
            while not hitnext:
                try:
                    int(line[index+digits])
                    digits += 1
                except:
                    hitnext = True
            beforelumber = int(line[index:index+digits])
            ls = list(line)
            ls[index:index+digits+1] = str(lumber)
            line = "".join(ls)
            with open(f"{userpath}/Library/Containers/com.rac7.SneakySasquatchMac/Data/Library/Application Support/com.rac7.SneakySasquatchMac/default{save}/sasquatch.stuff", "w") as f:
                f.write(line)
            print("Save successfully modified!")
    if query == "Q":
        print("Goodbye.")
        os.system("cd")
        sys.exit()
    else:
        print("Unknown command.")

