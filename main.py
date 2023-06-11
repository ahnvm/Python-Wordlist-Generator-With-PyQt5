import random
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow
from datetime import datetime



def main():
    allInput = ["1","2","3","4","5","6","7","8","9","0","+","-","*","/","2000","2001","2002"]
    allPasswords = []
    tempPasswords = []
    
    class pwdGenApp(QMainWindow):
        def __init__(self,minPassLen,maxPassLen,randomCase):
            super(pwdGenApp, self).__init__()
            
            self.setWindowTitle("Password Generator")
            self.setGeometry(200,200,800,600)
            self.setStyleSheet("background-color : Black;")
            self.minPassLen = int(minPassLen)
            self.maxPassLen = int(maxPassLen)
            self.randomCase = int(randomCase)
            
            self.initUI()
        def initUI(self):
            self.lbl_text1 = QtWidgets.QLabel(self)
            self.lbl_text1.move(5,30)
            self.lbl_text1.setText("Info text :")
            self.lbl_text1.setAlignment(QtCore.Qt.AlignCenter)
            self.lbl_text1.setStyleSheet("background-color: gray; color: white")
            self.lbl_text1.resize(100,30)
            self.lbl_text1.setFont(QFont("Arial.bold",12))
            
            self.lbl_text2 = QtWidgets.QLabel(self)
            self.lbl_text2.move(5,550)
            self.lbl_text2.setText("File Name :")
            self.lbl_text2.setAlignment(QtCore.Qt.AlignCenter)
            self.lbl_text2.setStyleSheet("background-color: gray; color: white")
            self.lbl_text2.resize(100,30)
            self.lbl_text2.setFont(QFont("Arial.bold",12))

            self.lbl_text3 = QtWidgets.QLabel(self)
            self.lbl_text3.move(5,80)
            self.lbl_text3.setText("Min password length: ")
            self.lbl_text3.setAlignment(QtCore.Qt.AlignCenter)
            self.lbl_text3.setStyleSheet("background-color: gray; color: white")
            self.lbl_text3.resize(175,30)
            self.lbl_text3.setFont(QFont("Arial.bold",10))

            self.lbl_text4 = QtWidgets.QLabel(self)
            self.lbl_text4.move(230,80)
            self.lbl_text4.setText(str(self.minPassLen))
            self.lbl_text4.setAlignment(QtCore.Qt.AlignCenter)
            self.lbl_text4.setStyleSheet("background-color: gray; color: white")
            self.lbl_text4.resize(100,30)
            self.lbl_text4.setFont(QFont("Arial.bold",12))

            self.lbl_text5 = QtWidgets.QLabel(self)
            self.lbl_text5.move(5,175)
            self.lbl_text5.setText("Max password length: ")
            self.lbl_text5.setAlignment(QtCore.Qt.AlignCenter)
            self.lbl_text5.setStyleSheet("background-color: gray; color: white")
            self.lbl_text5.resize(175,30)
            self.lbl_text5.setFont(QFont("Arial.bold",10))

            self.lbl_text6 = QtWidgets.QLabel(self)
            self.lbl_text6.move(230,175)
            self.lbl_text6.setText(str(self.maxPassLen))
            self.lbl_text6.setAlignment(QtCore.Qt.AlignCenter)
            self.lbl_text6.setStyleSheet("background-color: gray; color: white")
            self.lbl_text6.resize(100,30)
            self.lbl_text6.setFont(QFont("Arial.bold",12))

            self.lbl_text7 = QtWidgets.QLabel(self)
            self.lbl_text7.move(5,275)
            self.lbl_text7.setText("Random case repeating: ")
            self.lbl_text7.setAlignment(QtCore.Qt.AlignCenter)
            self.lbl_text7.setStyleSheet("background-color: gray; color: white")
            self.lbl_text7.resize(175,30)
            self.lbl_text7.setFont(QFont("Arial.bold",9))

            self.lbl_text8 = QtWidgets.QLabel(self)
            self.lbl_text8.move(230,275)
            self.lbl_text8.setText(str(self.randomCase))
            self.lbl_text8.setAlignment(QtCore.Qt.AlignCenter)
            self.lbl_text8.setStyleSheet("background-color: gray; color: white")
            self.lbl_text8.resize(100,30)
            self.lbl_text8.setFont(QFont("Arial.bold",12))

            self.txt_input = QtWidgets.QLineEdit(self)
            self.txt_input.move(120,30)
            self.txt_input.resize(100,30)
            self.txt_input.setStyleSheet("background-color : white")
            self.txt_input.returnPressed.connect(self.onPressed)

            self.minpwdlen_input = QtWidgets.QLineEdit(self)
            self.minpwdlen_input.move(5,120)
            self.minpwdlen_input.resize(175,30)
            self.minpwdlen_input.setStyleSheet("background-color: white")
            self.minpwdlen_input.returnPressed.connect(self.setMinPwdLen)

            self.maxpwdlen_input = QtWidgets.QLineEdit(self)
            self.maxpwdlen_input.move(5,215)
            self.maxpwdlen_input.resize(175,30)
            self.maxpwdlen_input.setStyleSheet("background-color: white")
            self.maxpwdlen_input.returnPressed.connect(self.setMaxPwdLen)
            
            self.randomRepeat_input = QtWidgets.QLineEdit(self)
            self.randomRepeat_input.move(5,315)
            self.randomRepeat_input.resize(175,30)
            self.randomRepeat_input.setStyleSheet("background-color: white")
            self.randomRepeat_input.returnPressed.connect(self.setRandomRepeat)

            self.file_name_input = QtWidgets.QLineEdit(self)
            self.file_name_input.move(120,550)
            self.file_name_input.resize(100,30)
            self.file_name_input.setStyleSheet("background-color : white")
            
            self.submitRandomRepeatbtn = QtWidgets.QPushButton(self)
            self.submitRandomRepeatbtn.move(230,315)
            self.submitRandomRepeatbtn.resize(100,30)
            self.submitRandomRepeatbtn.setStyleSheet("background-color: #F5943E")
            self.submitRandomRepeatbtn.setText("Submit")
            self.submitRandomRepeatbtn.clicked.connect(self.setRandomRepeat)

            self.submitMinLenBtn = QtWidgets.QPushButton(self)
            self.submitMinLenBtn.move(230,120)
            self.submitMinLenBtn.resize(100,30)
            self.submitMinLenBtn.setStyleSheet("background-color: #F5943E")
            self.submitMinLenBtn.setText("Submit")
            self.submitMinLenBtn.clicked.connect(self.setMinPwdLen)

            self.submitMaxLenBtn = QtWidgets.QPushButton(self)
            self.submitMaxLenBtn.move(230,215)
            self.submitMaxLenBtn.resize(100,30)
            self.submitMaxLenBtn.setStyleSheet("background-color: #F5943E")
            self.submitMaxLenBtn.setText("Submit")
            self.submitMaxLenBtn.clicked.connect(self.setMaxPwdLen)

            self.appendBtn = QtWidgets.QPushButton(self)
            self.appendBtn.move(230,30)
            self.appendBtn.resize(100,30)
            self.appendBtn.setStyleSheet("background-color : #F5943E")
            self.appendBtn.setText("APPEND INFO")
            self.appendBtn.clicked.connect(self.appendList)

            self.createFile = QtWidgets.QPushButton(self)
            self.createFile.move(230,550)
            self.createFile.resize(100,30)
            self.createFile.setStyleSheet("background-color : red")
            self.createFile.setText("CREATE WORDLIST")
            self.createFile.clicked.connect(self.createTxtFile)

            self.listInfo = QtWidgets.QListWidget(self)
            self.listInfo.move(350,28)
            self.listInfo.resize(350,550)
            self.listInfo.addItems(allInput)
            self.listInfo.setStyleSheet("background-color : white")
            self.errorMsg = QtWidgets.QErrorMessage(self)
            self.errorMsg.setWindowTitle("Error")
            self.errorMsg.setStyleSheet("background-color : white")

            self.successMsg = QtWidgets.QErrorMessage(self)
            self.successMsg.setWindowTitle("Info")
            self.successMsg.setStyleSheet("background-color : white")

            self.clearAllBtn = QtWidgets.QPushButton(self)
            self.clearAllBtn.move(715,28)
            self.clearAllBtn.resize(28,28)
            self.clearAllBtn.setText("C")
            self.clearAllBtn.setStyleSheet("Background-color: gray")
            self.clearAllBtn.clicked.connect(self.clearAll)

            self.clearPrevBtn = QtWidgets.QPushButton(self)
            self.clearPrevBtn.move(750,28)
            self.clearPrevBtn.resize(28,28)
            self.clearPrevBtn.setText("-")
            self.clearPrevBtn.setStyleSheet("Background-color: gray")
            self.clearPrevBtn.clicked.connect(self.clearPrev)

        def setRandomRepeat(self):
            if self.randomRepeat_input.text().strip() == "":
                self.errorMsg.showMessage("Nothing here")
            else:
                try:
                    p = int(self.randomRepeat_input.text().strip().replace(" ",""))
                    self.randomCase = p
                    self.randomRepeat_input.setText("")
                    self.lbl_text8.setText(str(self.randomCase))
                except:
                    self.errorMsg.showMessage("Random case repeating must be an integer")
                    self.randomRepeat_input.setText("")    
        def setMinPwdLen(self):
            if self.minpwdlen_input.text().strip() == "":
                self.errorMsg.showMessage("Nothing here")
            else:
                try:
                    e = int(self.minpwdlen_input.text().strip().replace(" ",""))
                    if e>self.maxPassLen:
                        self.errorMsg.showMessage("Min pass len must be smaller than max")
                        self.minpwdlen_input.setText("")
                    else:
                        self.minPassLen = e
                        self.lbl_text4.setText(str(self.minPassLen))
                        self.minpwdlen_input.setText("")
                except:
                   
                    self.errorMsg.showMessage("Min pass len must be an integer")
                    self.minpwdlen_input.setText("")


        def setMaxPwdLen(self):
            if self.maxpwdlen_input.text().strip() == "":
                self.errorMsg.showMessage("Nothing here")
            else:
                try:
                    z = int(self.maxpwdlen_input.text().strip().replace(" ",""))
                    if z<self.minPassLen:
                        self.errorMsg.showMessage("Max pass len must be bigger than min")
                        self.maxpwdlen_input.setText("")
                    else:
                        self.maxPassLen = z
                        self.lbl_text6.setText(str(self.maxPassLen))
                        self.maxpwdlen_input.setText("")
                except:
                   
                    self.errorMsg.showMessage("Max pass len must be an integer")
                    self.maxpwdlen_input.setText("")
        def clearPrev(self):
            try:
                allInput.pop()
                self.listInfo.clear()
                self.listInfo.addItems(allInput)
            except:
                self.errorMsg.showMessage("Nothing to delete here")
        def clearAll(self):
            try:
                _ = allInput[0]
                allInput.clear()
                self.listInfo.clear()
                self.listInfo.addItems(allInput)
            except:
                self.errorMsg.showMessage("Nothing to delete here")

        def onPressed(self):
            if self.txt_input.text().strip() == "":
                self.errorMsg.showMessage("Nothing here")
            else:
                allInput.append(self.txt_input.text().strip())
                self.listInfo.clear()
                self.listInfo.addItems(allInput)
                self.txt_input.setText("")
        def appendList(self):
            if self.txt_input.text().strip() == "":
                self.errorMsg.showMessage("Nothing here")
            else:
                allInput.append(self.txt_input.text().strip())
                self.listInfo.clear()
                self.listInfo.addItems(allInput)
                self.txt_input.setText("")
        
        def createPasswords(self):
            for item in allInput:
                tempPasswords.append(item)
            
            for item1 in allInput:
                for item2 in allInput:
                    a = item1+item2
                    tempPasswords.append(a)
                    
    
            for item1 in allInput:
                for item2 in allInput:
                    for item3 in allInput:
                        c = item1+item2+item3
                        tempPasswords.append(c)
            for item1 in allInput:
                for item2 in allInput:
                    for item3 in allInput:
                        for item4 in allInput:
                            e = item1+item2+item3+item4
                            tempPasswords.append(e)
                        
                        

                    

        def createTxtFile(self):
            if self.file_name_input.text().strip() == "":
                self.errorMsg.showMessage("Nothing here")
            else:
                try:
                    k = allInput[0]
                    time_start = datetime.now().replace(microsecond=0)
                    time_start = str(time_start)
                    replaced1 = time_start.replace("-","")
                    replaced2 = replaced1.replace(" ","")
                    replaced3 = replaced2.replace(":","")
                    fileFirst = self.file_name_input.text().replace(" ","")
                    fileName =fileFirst+replaced3+".txt"
                    f = open(fileName,"w",encoding= "utf-8")
                    self.createPasswords()
                    for pwd in tempPasswords:
                        if len(pwd)> self.maxPassLen:
                            stripper = len(pwd)-self.maxPassLen
                            pwd = pwd[:len(pwd)- stripper]
                            allPasswords.append(pwd)
                            output_string = str("")
                            try:
                                int(pwd)
                            except:
                                i=0
                                output_string = str("")
                                while i<self.randomCase:
                                    output_string = str("")
                                    for letter in pwd.lower():
                                        if (random.randint(0,100))%2 == 0:
                                            output_string += letter
                                        else:
                                            output_string += letter.upper()
                                        
                                    allPasswords.append(output_string)
                                    i+=1
                            try:
                                int(pwd)
                            except:    
                                pwd.upper()
                                allPasswords.append(pwd)
                        elif len(pwd)< self.minPassLen:
                            continue
                        else:
                            allPasswords.append(pwd)
                            output_string = str("")
                            try:
                                int(pwd)
                            except:
                                i=0
                                output_string = str("")
                                while i < self.randomCase:
                                    output_string = str("")
                                    for letter in pwd.lower():
                                        if (random.randint(0,100))%2 == 0:
                                            output_string += letter
                                        else:
                                            output_string += letter.upper()
                                    allPasswords.append(output_string)
                                    i+=1
                            try:
                                int(pwd)
                            except:    
                                pwd.upper()
                                allPasswords.append(pwd)
                    before_pass = set(allPasswords)
                    final_pass = list(before_pass)    
                    for passWords in final_pass:
                        f.write(passWords+"\n")    

                    self.successMsg.showMessage(f"File created. File contains {len(final_pass)} passwords ")
                    f.close()                      
                    self.file_name_input.setText("") 
                except:
                    self.errorMsg.showMessage("Nothing here")
                
        
        


    def pwdApp():
        app = QApplication(sys.argv)
        window = pwdGenApp(0,10,1)
        window.show()
        sys.exit(app.exec_())
    
    pwdApp()

if __name__ == "__main__":
    main()