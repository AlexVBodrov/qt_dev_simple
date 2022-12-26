import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi('login_Form\login.ui', self)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btn_login.clicked.connect(self.loginfuntion)
        self.btn_create_account.clicked.connect(self.goto_create_account)
    
    
    def loginfuntion(self):
        """Login to chat client."""
        name = self.lineEdit_name.text()
        password = self.lineEdit_password.text()
        print(f'Successfully logged in name={name}, password={password}')
    
    def goto_create_account(self):
        create_acc = CreateAcc()
        widget.addWidget(create_acc)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi('login_Form\create_acc.ui', self)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password_conform.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btn_sing_up.clicked.connect(self.create_acc_funtion)
    
    
    def create_acc_funtion(self):
        """Login to chat client."""
        name = self.lineEdit_name.text()
        if self.lineEdit_password.text() == self.lineEdit_password_conform.text():
            password = self.lineEdit_password.text()
        email = self.lineEdit_email.text()
        print(f'Successfully logged in name={name}, password={password}, email={email}')
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_login = Login()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_login)
    # widget.setFixedWidth(400)
    # widget.setFixedHeight(400)
    widget.show()
    sys.exit(app.exec_())
