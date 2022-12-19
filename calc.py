# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 442)
        MainWindow.setMinimumSize(QtCore.QSize(400, 442))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_text_label = QtWidgets.QLabel(self.centralwidget)
        self.main_text_label.setGeometry(QtCore.QRect(-1, 0, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.main_text_label.setFont(font)
        self.main_text_label.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.main_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_text_label.setObjectName("main_text_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 401, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 70, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 70, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(200, 70, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 150, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 150, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 150, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 230, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 230, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 230, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(0, 310, 151, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_equal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equal.setGeometry(QtCore.QRect(150, 310, 151, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_equal.setFont(font)
        self.pushButton_equal.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(55, 135, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(300, 70, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(55, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(300, 150, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(55, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_multiplies = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multiplies.setGeometry(QtCore.QRect(300, 230, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_multiplies.setFont(font)
        self.pushButton_multiplies.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(55, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_multiplies.setObjectName("pushButton_multiplies")
        self.pushButton_divide = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_divide.setGeometry(QtCore.QRect(300, 310, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_divide.setFont(font)
        self.pushButton_divide.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(55, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(0, 390, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 15, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_clear.setObjectName("pushButton_clear")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.add_functionc()

        self.is_equal = False
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.main_text_label.setText(_translate("MainWindow", "0"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_multiplies.setText(_translate("MainWindow", "*"))
        self.pushButton_divide.setText(_translate("MainWindow", "/"))
        
        self.pushButton_equal.setText(_translate("MainWindow", "="))
        
        self.pushButton_clear.setText(_translate("MainWindow", "Очистить"))


    def write_number(self, number):
        # print(number)
        if self.main_text_label.text() == '0' or self.is_equal == True:
            self.main_text_label.setText(number)
            self.is_equal = False
        else:
            self.main_text_label.setText(self.main_text_label.text() + number)
    
    def show_result(self):
        try:
            expression = self.main_text_label.text()
            res = eval(expression)
            input_res = f'Результат: {res}'
            self.main_text_label.setText(input_res)
            self.is_equal = True
        except Exception as e:
            self.main_text_label.setText('Error')
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            if isinstance(e, ZeroDivisionError):
                error.setText(f'На ноль делить нельзя')
            else:
                error.setText(f'Нет одного аргумента. Ошибка ВВОДА выражения')
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            error.setDetailedText(f'{e, type(e)}')
            
            error.buttonClicked.connect(self.clear_popup_action)
            
            error.exec_()


    def add_functionc(self):
        self.pushButton_0.clicked.connect(lambda: self.write_number(self.pushButton_0.text()))
        self.pushButton_1.clicked.connect(lambda: self.write_number(self.pushButton_1.text()))
        self.pushButton_2.clicked.connect(lambda: self.write_number(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.write_number(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.write_number(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.write_number(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(lambda: self.write_number(self.pushButton_6.text()))
        self.pushButton_7.clicked.connect(lambda: self.write_number(self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(lambda: self.write_number(self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(lambda: self.write_number(self.pushButton_9.text()))
        self.pushButton_plus.clicked.connect(lambda: self.write_number(self.pushButton_plus.text()))
        self.pushButton_minus.clicked.connect(lambda: self.write_number(self.pushButton_minus.text()))
        self.pushButton_multiplies.clicked.connect(lambda: self.write_number(self.pushButton_multiplies.text()))
        self.pushButton_divide.clicked.connect(lambda: self.write_number(self.pushButton_divide.text()))
        
        self.pushButton_equal.clicked.connect(self.show_result)
        self.pushButton_clear.clicked.connect(self.clear_popup_action)
    
    def clear_popup_action(self, button):
        self.main_text_label.setText("0")
        self.is_equal = False
            
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
