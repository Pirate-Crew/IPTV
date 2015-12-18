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
    print colored.yellow("##### v1.1 #####")
    print colored.yellow("################")
    print ""
    print colored.blue("Menu")
    print "0 - Exit"
    print "1 - Search for some Servers"
    print "2 - Look at the servers list"
    print "3 - Select language, default is Italian"
    print "4 - Brute force random accounts"
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
        for server in cr.parsedUrls:
            print server
    elif choosenMenu == 3:
        language = str(raw_input("What language do you need? (it, en, es): "))
        cr.change_language(language)
        print colored.green("Language changed")
    elif choosenMenu == 4:
        result =  cr.search_accounts()
        print colored.green(result)
    else:
        print colored.red("Option not recognized")
