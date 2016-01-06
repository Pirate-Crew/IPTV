#!/usr/bin/python
from PyQt4 import QtCore, QtGui
import Crawler
import warnings
import time

# Global variables
warnings.filterwarnings("ignore")
cr = Crawler.Crawler("it")
message = ""

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
        self.connect(self.pushButton_2, QtCore.SIGNAL("released()"), self.release_signal)
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItems(cr.parsedUrls)
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

    def addBatch2(self, text="release_signal", iters=6, delay=0.3):
        global message
        global url
        url = str(self.lineEdit.text())
        message = "Fetching account from " + url + " this might take a while."
        self.send_signal()
        time.sleep(delay)
        message = cr.search_accounts(url)
        self.send_signal()
        time.sleep(delay)

    def release_signal(self):
        self.threadPool.append(GenericThread(self.addBatch2, message, delay=0.3))
        self.disconnect(self, QtCore.SIGNAL("add(QString)"), self.add )
        self.connect(self, QtCore.SIGNAL("add(QString)"), self.add )
        self.threadPool[len(self.threadPool)-1].start()

    def send_signal(self):
        self.threadPool.append( WorkThread() )
        self.connect(self.threadPool[len(self.threadPool)-1], QtCore.SIGNAL("update(QString)"), self.add)
        self.threadPool[len(self.threadPool)-1].start()

class WorkThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        for i in range(6):
            time.sleep(0.3)
            self.emit(QtCore.SIGNAL('update(QString)'), message)
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
        self.function(*self.args, **self.kwargs)
        return

if __name__ == "__main__":
    import sys
    cr.search_links()
    cr.add_links()
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
