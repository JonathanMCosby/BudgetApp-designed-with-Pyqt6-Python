# Form implementation generated from reading ui file '/Users/benjicosby/Desktop/improveBudgetApp/signUpWindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
from invalidWindow_ui import Ui_invalidWindow
import mysql.connector
from mysql.connector import errorcode
from PyQt6 import QtCore, QtGui, QtWidgets
import sys





class Ui_signUpWindow(object):
    def setupUi(self, signUpWindow):
        signUpWindow.setObjectName("signUpWindow")
        signUpWindow.resize(680, 618)
        signUpWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.311828 rgba(118, 255, 163, 252), stop:0.688172 rgba(65, 183, 60, 255));")
        self.centralwidget = QtWidgets.QWidget(parent=signUpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 10, 161, 16))
        self.label.setStyleSheet("background-color: none;\n"
"color: rgb(255,255,255);")
        self.label.setObjectName("label")
        self.titleLbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.titleLbl.setGeometry(QtCore.QRect(180, 50, 341, 61))
        self.titleLbl.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.titleLbl.setStyleSheet("background-color: rgb(118,255,163) ;\n"
"font-size: 32px;\n"
"font: italic bold;\n"
"color: rgb(65,183,60);\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border-radius: 25px;\n"
"")
        self.titleLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLbl.setObjectName("titleLbl")
        self.signLbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.signLbl.setGeometry(QtCore.QRect(270, 120, 161, 61))
        self.signLbl.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.signLbl.setStyleSheet("background-color: rgb(118,255,163) ;\n"
"font-size: 24px;\n"
"font: italic bold;\n"
"color: rgb(65,183,60);\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border-radius: 25px;")
        self.signLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.signLbl.setObjectName("signLbl")
        self.firstNameLbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.firstNameLbl.setGeometry(QtCore.QRect(180, 190, 101, 51))
        self.firstNameLbl.setStyleSheet("background-color: rgb(118,255,163);\n"
"color: rgb(65,183,60);\n"
"font: italic bold;\n"
"font-size: 15px;\n"
"border-radius: 15px;\n"
"border-color: rgb(65,183,60);")
        self.firstNameLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.firstNameLbl.setObjectName("firstNameLbl")
        self.firstNameLine = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.firstNameLine.setGeometry(QtCore.QRect(320, 190, 181, 51))
        self.firstNameLine.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font: bold;\n"
"border-radius: 15px;\n"
"font-size: 18px;")
        self.firstNameLine.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.firstNameLine.setObjectName("firstNameLine")
        self.lastNameLbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.lastNameLbl.setGeometry(QtCore.QRect(180, 250, 101, 51))
        self.lastNameLbl.setStyleSheet("background-color: rgb(118,255,163);\n"
"color: rgb(65,183,60);\n"
"font: italic bold;\n"
"font-size: 15px;\n"
"border-radius: 15px")
        self.lastNameLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lastNameLbl.setObjectName("lastNameLbl")
        self.lastNameLine = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lastNameLine.setGeometry(QtCore.QRect(320, 250, 181, 51))
        self.lastNameLine.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font: bold;\n"
"border-radius: 15px;\n"
"font-size: 18px;")
        self.lastNameLine.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lastNameLine.setObjectName("lastNameLine")
        self.passwordLbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.passwordLbl.setGeometry(QtCore.QRect(180, 370, 101, 51))
        self.passwordLbl.setStyleSheet("background-color: rgb(118,255,163);\n"
"color: rgb(65,183,60);\n"
"font: italic bold;\n"
"font-size: 15px;\n"
"border-radius: 15px")
        self.passwordLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.passwordLbl.setObjectName("passwordLbl")
        self.passwordLine = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.passwordLine.setGeometry(QtCore.QRect(320, 370, 181, 51))
        self.passwordLine.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font: bold;\n"
"border-radius: 15px;\n"
"font-size: 18px;")
        self.passwordLine.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.passwordLine.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.passwordLine.setClearButtonEnabled(False)
        self.passwordLine.setObjectName("passwordLine")
        self.enterBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.enterBtn.setGeometry(QtCore.QRect(270, 450, 121, 51))
        self.enterBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.enterBtn.setStyleSheet("background-color: rgb(65,183,60);\n"
"font: italic bold;\n"
"color: rgb(118,255,163);\n"
"font-size: 20px;\n"
"border-radius: 15px;\n"
"")
        self.enterBtn.setObjectName("enterBtn")
        self.signInBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.signInBtn.setGeometry(QtCore.QRect(250, 510, 171, 51))
        self.signInBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.signInBtn.setStyleSheet("background-color: rgb(65,183,60);\n"
"font: italic bold;\n"
"color: rgb(118,255,163);\n"
"font-size: 20px;\n"
"border-radius: 15px;\n"
"")
        self.signInBtn.setObjectName("signInBtn")
        self.userNameLbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.userNameLbl.setGeometry(QtCore.QRect(180, 310, 101, 51))
        self.userNameLbl.setStyleSheet("background-color: rgb(118,255,163);\n"
"color: rgb(65,183,60);\n"
"font: italic bold;\n"
"font-size: 15px;\n"
"border-radius: 15px")
        self.userNameLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.userNameLbl.setObjectName("userNameLbl")
        self.userNameLine = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.userNameLine.setGeometry(QtCore.QRect(320, 310, 181, 51))
        self.userNameLine.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font: bold;\n"
"border-radius: 15px;\n"
"font-size: 18px;")
        self.userNameLine.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.userNameLine.setObjectName("userNameLine")
        signUpWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=signUpWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 21))
        self.menubar.setObjectName("menubar")
        signUpWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=signUpWindow)
        self.statusbar.setObjectName("statusbar")
        signUpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(signUpWindow)
        QtCore.QMetaObject.connectSlotsByName(signUpWindow)

    def retranslateUi(self, signUpWindow):
        _translate = QtCore.QCoreApplication.translate
        signUpWindow.setWindowTitle(_translate("signUpWindow", "MainWindow"))
        self.label.setText(_translate("signUpWindow", "Made By: Jonathan Cosby"))
        self.titleLbl.setText(_translate("signUpWindow", "BudgetApp"))
        self.signLbl.setText(_translate("signUpWindow", "Sign Up"))
        self.firstNameLbl.setText(_translate("signUpWindow", "First Name"))
        self.firstNameLine.setPlaceholderText(_translate("signUpWindow", "First Name"))
        self.lastNameLbl.setText(_translate("signUpWindow", "Last Name"))
        self.lastNameLine.setPlaceholderText(_translate("signUpWindow", "Last Name"))
        self.passwordLbl.setText(_translate("signUpWindow", "Passsword"))
        self.passwordLine.setPlaceholderText(_translate("signUpWindow", "Password"))
        self.enterBtn.setText(_translate("signUpWindow", "Enter"))
        self.signInBtn.setText(_translate("signUpWindow", "Sign In"))
        self.userNameLbl.setText(_translate("signUpWindow", "User Name"))
        self.userNameLine.setPlaceholderText(_translate("signUpWindow", "User Name"))

        self.enterBtn.clicked.connect(lambda:self.enter(signUpWindow))
        self.signInBtn.clicked.connect(lambda:self.signIn(signUpWindow))

    def enter(self,signUpWindow):
             try:
                my_connection = mysql.connector.connect(
                     user = "root",
                     password = "Kteasley",
                     host = "localhost",
                     database = "budgetProgram"
                     )
                
             except mysql.connector.Error as err:
                  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                        print("Invaild credentials")

                        if err.errno == errorcode.ER_BAD_DB_ERROR:
                             print("No database available")
                        else:
                              print("Error occured", err)
             else:
                print('Connection Successful')
                user_cursor = my_connection.cursor()
                query = "INSERT INTO user (user_name, first_name, last_name, password) VALUES (%s,%s,%s,%s)"
        
                firstNameLine = self.firstNameLine.text()
                lastNameLine = self.lastNameLine.text()
                userNameLine = self.userNameLine.text()
                passwordLine = self.passwordLine.text()
                if firstNameLine == "" or lastNameLine == "" or userNameLine == "" or passwordLine == "":
                        self.invalidWindow = QtWidgets.QMainWindow()
                        self.invalidUi = Ui_invalidWindow()
                        self.invalidUi.setupUi(self.invalidWindow)
                        self.invalidWindow.show()
                else:
                     user_cursor.execute(query,(userNameLine, firstNameLine, lastNameLine, passwordLine))
                     print("You are in the database")
                     my_connection.commit()
                     my_connection.close()
                     signUpWindow.hide()

    def signIn(self,signUpWindow):
        signUpWindow.hide()