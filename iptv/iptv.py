#!/usr/bin/python
import Crawler
from clint.textui import colored

cr = Crawler.Crawler("it")

"""Print menu
Easy menu for CLI navigation
"""
def menu():
    print ""
    print colored.yellow("################")
    print colored.yellow("##### IPTV #####")
    print colored.yellow("##### v1.0 #####")
    print colored.yellow("################")
    print ""
    print colored.blue("Menu")
    print "1 - Search for some Servers"
    print "2 - Select language, default is Italian"
    print "3 - Brute force random accounts"
    print "4 - Exit"
    print ""

while True:
    menu()
    choosenMenu = int(raw_input("Please select an option: "))
    if choosenMenu == 1:
        print colored.green("Fetching URLs plase wait...")
        cr.search_links()
        print colored.green("Done, 30 URLs founded")
    elif choosenMenu == 2:
        language = str(raw_input("What language do you need? (it, en, es): "))
        cr.change_language(language)
        print colored.green("Language changed")
    elif choosenMenu == 3:
        result =  cr.search_accounts()
        print colored.green(result)
    elif choosenMenu == 4:
        print colored.red("Bye bye")
        break
    else:
        print colored.red("Option not recognized")
