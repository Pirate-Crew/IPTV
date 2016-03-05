#!/usr/bin/python
import Crawler
import warnings
from clint.textui import colored

# Global Variables
warnings.filterwarnings("ignore")
cr = Crawler.Crawler("it")

"""Print menu
Easy menu for CLI navigation
"""
def menu():
    print ""
    print colored.yellow("################")
    print colored.yellow("##### IPTV #####")
    print colored.yellow("##### v" + cr.version + " ###")
    print colored.yellow("################")
    print ""
    print colored.blue("Menu")
    print "0 - Exit"
    print "1 - Search for some Servers"
    print "2 - Look at the servers list"
    print "3 - Select language, default is Italian"
    print "4 - Brute force all server from the list"
    print "5 - Brute force random server from the list"
    print "6 - Brute force specific server from the list"
    print "7 - Provide a random server to attack"
    print ""

while True:
    menu()
    choosenMenu = int(raw_input("Please select an option: "))
    if choosenMenu == 0:
        print colored.red("Bye bye")
        break;
    elif choosenMenu == 1:
        print colored.green("Fetching URLs plase wait...")
        cr.search_links()
        print colored.green("Done, 30 URLs founded")
    elif choosenMenu == 2:
        print colored.green("Printing server list")
        for index, server in enumerate(cr.parsedUrls):
            print "[" + str(index) + "] - " + server
    elif choosenMenu == 3:
        language = str(raw_input("What language do you need? (it, en, es): "))
        if cr.change_language(language):
            print colored.green("Language changed, the system now will attack the servers with " + language + "txt.")
        else:
            print colored.red("Language not changes, the file language for " + language + " does not exists")
    elif choosenMenu == 4:
        for i in range(0,30):
            url = cr.parsedUrls[i]
            result = cr.search_accounts(url)
            print colored.green(result)
    elif choosenMenu == 5:
        result =  cr.search_accounts()
        print colored.green(result)
    elif choosenMenu == 6:
        try:
            index = int(raw_input("Please provide the number near the URLs founded: "))
            url = cr.parsedUrls[index]
            result = cr.search_accounts(url)
            print colored.green(result)
        except IndexError as e:
            print colored.red("No URL founded at index: " + str(index))
        except ValueError as e:
            print colored.red("You have entered a wrong value, please provide a NUMBER. Use option 2 first")
    elif choosenMenu == 7:
        print colored.blue("coming soon...")
    else:
        print colored.red("Option not recognized")
