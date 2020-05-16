from PySide2 import QtWidgets
from PySide2.QtGui import QIcon
from PySide2 import QtCore

class MyDialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.push_pb = QtWidgets.QPushButton("&PushButton")
        self.setWindowTitle("MyQTWindow")  
        self.setCentralWidget(self.push_pb)  
        self.push_pb.clicked.connect(self.PushButtonHandler)

    def PushButtonHandler(self):
        QtWidgets.QMessageBox.about(self, "Namaste! ","Welcome to QT world.\nAfter clicking this OK button, your second window will open.")
        self.newDialog = CNewDialog()
        self.newDialog.show()


class CNewDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(CNewDialog, self).__init__(parent)

        self.question_lable = QtWidgets.QLabel("Do you want to know your performance in QT and Python so far?")
        self.answer_lable = QtWidgets.QLabel("Enter Yes if interested.")
        self.answer_le = QtWidgets.QLineEdit()
        self.ok_button = QtWidgets.QPushButton("&OK")

        layout = QtWidgets.QFormLayout()
        layout.addWidget(self.question_lable)
        layout.addWidget(self.answer_lable)
        layout.addWidget(self.answer_le)
        layout.addWidget(self.ok_button)
        #to display all the widgets in window
        self.setLayout(layout)  

        self.setWindowTitle("MySecondDialog")

        self.ok_button.clicked.connect(self.OKButtonClicked)

    def OKButtonClicked(self):
        ans_text = self.answer_le.text()
        if "yes" == ans_text.lower():
            QtWidgets.QMessageBox.about(self, "Hey! ", "\nYou are doing awesome man.")
        else :
            QtWidgets.QMessageBox.about(self, "Hey! ", "\nThere is no point of clicking the button if you are not interested.")



app = QtWidgets.QApplication()
MyFirstWindow = MyDialog()
MyFirstWindow.show()
app.exec_()
