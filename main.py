from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
        # Задаем парпметры window
        self.setWindowTitle('First simple programm')
        self.setGeometry(450, 550, 350, 200)
        
        # Сюда довавляем виджеты
        
        # надпись в объекте window
        self.main_text = QtWidgets.QLabel(self)
        # add simple text
        self.main_text.setText('This is a simple text label')
        # set parameters main text
        self.main_text.move(100, 100)
        self.main_text.adjustSize()
        
        #add button в объекте window
        self.btn = QtWidgets.QPushButton(self)
        # set parameters
        self.btn.move(70, 150)
        self.btn.setText('Нажми на меня')
        self.btn.setFixedWidth(200)
        # set signal
        self.btn.clicked.connect(self.add_label)


    def add_label(self):
        print('add_label')
    
def application():
    app = QApplication(sys.argv)
    
    # Create main window
    window = Window()
    
    # Показываем(рисуем окно) window
    window.show()
    # Закрываем приложение
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
