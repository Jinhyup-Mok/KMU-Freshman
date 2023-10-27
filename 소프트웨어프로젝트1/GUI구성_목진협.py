import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt

class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scdb = []
        self.readScoreDB()
        self.showScoreDB("Name")

    def initUI(self):
        Name = QLabel("Name:", self)
        Age = QLabel("Age:", self)
        Score = QLabel("Score:", self)
        Amount = QLabel("Amount:", self)
        Key = QLabel("Key:", self)

        self.NameEdit = QLineEdit()
        self.AgeEdit = QLineEdit()
        self.ScoreEdit = QLineEdit()
        self.AmountEdit = QLineEdit()

        self.keyCombo = QComboBox()
        self.keyCombo.addItem('Name')
        self.keyCombo.addItem('Age')
        self.keyCombo.addItem('Score')

        Add = QPushButton("Add")
        Del = QPushButton("Del")
        Find = QPushButton("Find")
        Inc = QPushButton("Inc")
        show = QPushButton("show")

        Result = QLabel("Result:", self)
        self.ResultEdit = QTextEdit()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(Name), hbox1.addWidget(self.NameEdit), hbox1.addWidget(Age), hbox1.addWidget(self.AgeEdit)
        hbox1.addWidget(Score), hbox1.addWidget(self.ScoreEdit)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(Amount), hbox2.addWidget(self.AmountEdit)
        hbox2.addWidget(Key), hbox2.addWidget(self.keyCombo)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(Add)
        hbox3.addWidget(Del)
        hbox3.addWidget(Find)
        hbox3.addWidget(Inc)
        hbox3.addWidget(show)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(Result)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.ResultEdit)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        Add.clicked.connect(self.buttonClicked)
        Del.clicked.connect(self.buttonClicked)
        Find.clicked.connect(self.buttonClicked)
        Inc.clicked.connect(self.buttonClicked)
        show.clicked.connect(self.buttonClicked)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == "Add":
            self.addScoreDB()
        elif sender.text() == "Del":
            self.delScoreDB()
        elif sender.text() == "Find":
            self.findScoreDB()
        elif sender.text() == "Inc":
            self.incScoreDB()
        elif sender.text() == "show":
            sortKey = self.keyCombo.currentText()
            self.showScoreDB(sortKey)

    def addScoreDB(self):
        try:
            record = {'Name': self.NameEdit.text(), 'Age': int(self.AgeEdit.text()), 'Score': int(self.ScoreEdit.text())}
            self.scdb += [record]
        except:
            pass
    def delScoreDB(self):
        try:
            temp1 = []
            for p in self.scdb:
                if p['Name'] != self.NameEdit.text():
                    temp1.append(p)
                self.scdb = temp1
        except:
            pass

    def findScoreDB(self):
        try:
            for p in self.scdb:
                if p['Name'] == self.NameEdit.text():
                    temp = ""
                    for attr in sorted(p):
                        temp += (attr + "=" + str(p[attr]) + ' ')
                    self.ResultEdit.append(temp)
        except:
            pass

    def incScoreDB(self):
        try:
            for p in self.scdb:
                if p['Name'] == self.NameEdit.text():
                    score = int(p['Score'])
                    score += int(self.AmountEdit.text())
                    p['Score'] = str(score)
        except:
            pass

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scdb = []
            return

        try:
            self.scdb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scdb, fH)
        fH.close()

    def showScoreDB(self, keyname):
        self.ResultEdit.clear()
        for p in sorted(self.scdb, key=lambda person: person[keyname]):
            temp = ""
            for attr in sorted(p):
                temp += (attr + "=" + str(p[attr]) + ' ')
            self.ResultEdit.append(temp)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
