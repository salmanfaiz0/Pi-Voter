import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("page1.ui",self)
        self.submit_button.clicked.connect(self.loginfunction)   ##ith submit button##
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)   ## ith phonebumber ##
        self.createaccbutton.clicked.connect(self.gotocreate)     ## adutha finger ileak ##



    def loginfunction(self):
     password = self.password.text()
     print("Successfully logged in with email: ", password)    ## output on terminal ##


    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("page2.ui",self)
        self.pushButton_3.clicked.connect(self.gotocreate)

    def gotocreate(self):
            createaccs = CreateAccs()
            widget.addWidget(createaccs)
            widget.setCurrentIndex(widget.currentIndex() + 1)

class CreateAccs(QDialog):
    def __init__(self):
        super(CreateAccs,self).__init__()
        loadUi("page3.ui",self)
        self.pushButton_4.clicked.connect(self.gotocreate)

    def gotocreate(self):
            createaccs = CreateAccs()
            widget.addWidget(createaccs)
            widget.setCurrentIndex(widget.currentIndex() + 1)



app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(800)
widget.setFixedHeight(480)
widget.show()
app.exec_()
