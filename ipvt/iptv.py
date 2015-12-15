#!/usr/bin/python
#-*- coding: utf-8 -*-

#########################################################################
#  This program is free software; you can redistribute it and/or modify #
#  it under the terms of the GNU General Public License as published by #
#  the Free Software Foundation; either version 2 of the License, or    #
#  (at your option) any later version.                                  #
#                                                                       #
#  This program is distributed in the hope that it will be useful,      #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of       #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
#  GNU General Public License for more details.                         #
#                                                                       #
#  You should have received a copy of the GNU General Public License    #
#  along with this program; if not, write to the Free Software          #
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,           #
#  MA 02110-1301, USA.                                                  #
############################# DISCALIMER ################################
#  Usage of this software for probing/attacking targets without prior   #
#  mutual consent, is illegal. It's the end user's responsability to    #
#  obey alla applicable local laws. Developers assume no liability and  #
#  are not responible for any missue or damage caused by thi program    #
#########################################################################

#by Pinperepette - The Pirate

import Crawler
from clint.textui import colored
from sys import argv as s

#Parameters
version = "v1.0"
search = "Xtream Codes v1.0.59.5"
cr = Crawler.Crawler("it")

def menu():
    print colored.yellow("################")
    print colored.yellow("##### ") + s[0] + colored.yellow(" ##")
    print colored.yellow("##### ") + version + colored.yellow(" #####")
    print colored.yellow("################")
    print ""
    print colored.blue("Basic Usage")
    print "Print the servers list: " + colored.red(s[0] + " " + "-pl")
    print "Account search: " + colored.red(s[0] + " " + "http://site.server")

if len(s) == 1:
    menu()
    exit()
elif s[1] == "-h":
    menu()
    exit()
elif s[1] == "-pl":
    cr.search_links()
    exit()
else:
    cr.search_accounts(s[1])
