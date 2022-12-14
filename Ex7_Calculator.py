from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Simple Calculator")
        MainWindow.resize(364, 576)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output_Label = QtWidgets.QLabel(self.centralwidget)
        self.output_Label.setGeometry(QtCore.QRect(10, 10, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.output_Label.setFont(font)
        self.output_Label.setFrameShape(QtWidgets.QFrame.Box)
        self.output_Label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.output_Label.setLineWidth(2)
        self.output_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output_Label.setObjectName("output_Label")
        self.percentageBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("%"))
        self.percentageBtn.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentageBtn.setFont(font)
        self.percentageBtn.setObjectName("percentageBtn")
        self.CBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("C"))
        self.CBtn.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.CBtn.setFont(font)
        self.CBtn.setObjectName("CBtn")
        self.arrowBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.remove_it())
        self.arrowBtn.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrowBtn.setFont(font)
        self.arrowBtn.setObjectName("arrowBtn")
        self.divideBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("/"))
        self.divideBtn.setGeometry(QtCore.QRect(280, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideBtn.setFont(font)
        self.divideBtn.setObjectName("divideBtn")
        self.eightBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("8"))
        self.eightBtn.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightBtn.setFont(font)
        self.eightBtn.setObjectName("eightBtn")
        self.nineBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("9"))
        self.nineBtn.setGeometry(QtCore.QRect(190, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineBtn.setFont(font)
        self.nineBtn.setObjectName("nineBtn")
        self.sevenBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("7"))
        self.sevenBtn.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenBtn.setFont(font)
        self.sevenBtn.setObjectName("sevenBtn")
        self.multiplyBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("*"))
        self.multiplyBtn.setGeometry(QtCore.QRect(280, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyBtn.setFont(font)
        self.multiplyBtn.setObjectName("multiplyBtn")
        self.fiveBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("5"))
        self.fiveBtn.setGeometry(QtCore.QRect(100, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveBtn.setFont(font)
        self.fiveBtn.setObjectName("fiveBtn")
        self.sixBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("6"))
        self.sixBtn.setGeometry(QtCore.QRect(190, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixBtn.setFont(font)
        self.sixBtn.setObjectName("sixBtn")
        self.fourBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("4"))
        self.fourBtn.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourBtn.setFont(font)
        self.fourBtn.setObjectName("fourBtn")
        self.subtractBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("-"))
        self.subtractBtn.setGeometry(QtCore.QRect(280, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.subtractBtn.setFont(font)
        self.subtractBtn.setObjectName("subtractBtn")
        self.twoBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("2"))
        self.twoBtn.setGeometry(QtCore.QRect(100, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoBtn.setFont(font)
        self.twoBtn.setObjectName("twoBtn")
        self.threeBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("3"))
        self.threeBtn.setGeometry(QtCore.QRect(190, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeBtn.setFont(font)
        self.threeBtn.setObjectName("threeBtn")
        self.oneBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("1"))
        self.oneBtn.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneBtn.setFont(font)
        self.oneBtn.setObjectName("oneBtn")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("+"))
        self.addBtn.setGeometry(QtCore.QRect(280, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.addBtn.setFont(font)
        self.addBtn.setObjectName("addBtn")
        self.zeroBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("0"))
        self.zeroBtn.setGeometry(QtCore.QRect(100, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroBtn.setFont(font)
        self.zeroBtn.setObjectName("zeroBtn")
        self.dotBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.dot_it())
        self.dotBtn.setGeometry(QtCore.QRect(190, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.dotBtn.setFont(font)
        self.dotBtn.setObjectName("dotBtn")
        self.plusMinusBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.plusMinus_it())
        self.plusMinusBtn.setGeometry(QtCore.QRect(10, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusMinusBtn.setFont(font)
        self.plusMinusBtn.setObjectName("plusMinusBtn")
        self.equalBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.math_it())
        self.equalBtn.setGeometry(QtCore.QRect(280, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalBtn.setFont(font)
        self.equalBtn.setObjectName("equalBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def math_it(self):
        try:
            screen = self.output_Label.text()
            answer = eval(screen)
            self.output_Label.setText(str(answer))
        except:
            self.output_Label.setText("Error")

    def plusMinus_it(self):
        screen = self.output_Label.text()
        if "-" in screen:
            self.output_Label.setText(screen.replace("-", ""))
        else:
            self.output_Label.setText(f'-{screen}')

    def remove_it(self):
        screen = self.output_Label.text()
        screen = screen[:-1]
        self.output_Label.setText(screen)

    def dot_it(self):
        screen = self.output_Label.text()
        if screen[-1] == ".":
            pass
        else:
            self.output_Label.setText(f'{screen}.')

    def press_it(self, pressed):
        if pressed == "C":
            self.output_Label.setText("0")
        else:
            if self.output_Label.text() == "0":
                self.output_Label.setText("")
            self.output_Label.setText(f'{self.output_Label.text()}{pressed}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Calculator"))
        self.output_Label.setText(_translate("MainWindow", "0"))
        self.percentageBtn.setText(_translate("MainWindow", "%"))
        self.CBtn.setText(_translate("MainWindow", "C"))
        self.arrowBtn.setText(_translate("MainWindow", "<<"))
        self.divideBtn.setText(_translate("MainWindow", "/"))
        self.eightBtn.setText(_translate("MainWindow", "8"))
        self.nineBtn.setText(_translate("MainWindow", "9"))
        self.sevenBtn.setText(_translate("MainWindow", "7"))
        self.multiplyBtn.setText(_translate("MainWindow", "x"))
        self.fiveBtn.setText(_translate("MainWindow", "5"))
        self.sixBtn.setText(_translate("MainWindow", "6"))
        self.fourBtn.setText(_translate("MainWindow", "4"))
        self.subtractBtn.setText(_translate("MainWindow", "-"))
        self.twoBtn.setText(_translate("MainWindow", "2"))
        self.threeBtn.setText(_translate("MainWindow", "3"))
        self.oneBtn.setText(_translate("MainWindow", "1"))
        self.addBtn.setText(_translate("MainWindow", "+"))
        self.zeroBtn.setText(_translate("MainWindow", "0"))
        self.dotBtn.setText(_translate("MainWindow", "."))
        self.plusMinusBtn.setText(_translate("MainWindow", "+/-"))
        self.equalBtn.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
