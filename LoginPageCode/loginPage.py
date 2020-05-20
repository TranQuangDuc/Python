from PySide2 import QtWidgets
from PySide2.QtGui import QIcon


class LoginUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginUI, self).__init__()

        self.user_name = ""
        self.password = ""
        self.flag = True

        self.user_name_lable = QtWidgets.QLabel("User Name: ")
        self.user_name_le = QtWidgets.QLineEdit()
        self.user_name_le.setPlaceholderText("Enter User Name.")

        self.password_lable = QtWidgets.QLabel("Password: ")
        self.password_le = QtWidgets.QLineEdit()
        self.password_le.setPlaceholderText("Enter password.")

        self.login_pb = QtWidgets.QPushButton()
        self.login_pb.setText("&login")
        self.login_pb.setDisabled(True)

        self.layout = QtWidgets.QFormLayout()
        self.layout.addWidget(self.user_name_lable)
        self.layout.addWidget(self.user_name_le)

        self.layout.addWidget(self.password_lable)
        self.layout.addWidget(self.password_le)
        self.layout.addWidget(self.login_pb)

        widget = QtWidgets.QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        self.setWindowTitle("Please login")
        self.setFixedSize(400, 200)

        self.login_pb.clicked.connect(self.loginHandler)
        self.user_name_le.textChanged.connect(self.UserNameEntered)
        self.password_le.textChanged.connect(self.PasswordEntered)


    def loginHandler(self):
        file = LoginOperation("login.dat")
        if file.isValidUser(self.user_name, self.password):
            QtWidgets.QMessageBox.about(self, "Success", "Login successful.")
        else:
            QtWidgets.QMessageBox.about(self, "Fail", "Login failed.")
        self.user_name_le.clear()
        self.password_le.clear()
        self.password = ""
        self.flag = True


    def UserNameEntered(self):
        self.user_name = self.user_name_le.text()
        self.password = self.password_le.text()
        if self.user_name != "" and self.password != "":
            self.login_pb.setDisabled(False)
            self.login_pb.setIcon(QIcon("ok.png"))
        else:
            self.login_pb.setDisabled(True)

    def PasswordEntered(self):
        self.user_name = self.user_name_le.text()
        temp_pass = self.password_le.text()

        if self.flag:
            self.password =  self.password + temp_pass[len(temp_pass)-1:]
            self.flag = False
        else:
            self.flag = True

        temp = ""
        for _ in range(0, len(temp_pass)):
            temp = temp + "*"

        self.password_le.setText(temp)
        if self.user_name != "" and self.password != "":
            self.login_pb.setDisabled(False)
            self.login_pb.setIcon(QIcon("ok.png"))
        else:
            self.login_pb.setDisabled(True)


class LoginOperation():
    def __init__(self, file_name):
        self.file_name = file_name
        self.login_details = dict()
        self.readLoginDetails()

    def getLoginDetails(self):
        return self.login_details

    def isValidUser(self, user, password):
        if user in self.login_details and password == self.login_details[user]:
            return True
        else:
            return False

    def readLoginDetails(self):
        with open(self.file_name, "r") as f:
            data = f.readlines()

            for line in data:
                user_temp, password_temp = line.split(" ")
                self.login_details[user_temp[2:]] = password_temp[2:]








app = QtWidgets.QApplication()
login_page = LoginUI()
login_page.show()
app.exec_()
