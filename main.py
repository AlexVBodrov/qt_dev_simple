from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

def add_label():
    print('add_label')
    
def application():
    app = QApplication(sys.argv)
    
    # Create main window
    window = QMainWindow()
    
    # Задаем парпметры window
    window.setWindowTitle('First simple programm')
    window.setGeometry(450, 550, 350, 200)
    
    # Сюда довавляем виджеты
    
    # надпись в объекте window
    main_text = QtWidgets.QLabel(window)
    # add simple text
    main_text.setText('This is a simple text label')
    # set parameters main text
    main_text.move(100, 100)
    main_text.adjustSize()
    
    #add button в объекте window
    btn = QtWidgets.QPushButton(window)
    # set parameters
    btn.move(70, 150)
    btn.setText('Нажми на меня')
    btn.setFixedWidth(200)
    # set signal
    btn.clicked.connect(add_label)
    
    
    # Показываем(рисуем окно) window
    window.show()
    # Закрываем приложение
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
