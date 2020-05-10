'''
Open a new window.
How to pass value form one window to other?
Write your window without QTDesigner. Another way of creating window.


'''
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon

class CNewWindow(QtWidgets.QDialog):
    def __init__(self, name, parent=None):
        super(CNewWindow, self).__init__(parent)

        self.userName = name
        self.queLable = QtWidgets.QLabel("Do you want to know your performance in QT and Python so far?")
        self.ansLable = QtWidgets.QLabel("Enter Yes if interested.")
        self.ans_LE = QtWidgets.QLineEdit()
        self.OKButton = QtWidgets.QPushButton("&OK")

        layout = QtWidgets.QFormLayout()
        layout.addWidget(self.queLable)
        layout.addWidget(self.ansLable)
        layout.addWidget(self.ans_LE)
        layout.addWidget(self.OKButton)
        
        self.setLayout(layout)  #to display all the widgets in window

        self.setWindowIcon(QIcon("D:\\@Study\\Python\\#QTBlogCode\\NewDialogOnButtonClick\\Code\\QTIcon.png"))
        self.setWindowTitle("MySecondQTWindow")

        self.OKButton.clicked.connect(self.OKButtonClicked)

    def OKButtonClicked(self):
        ansText = self.ans_LE.text()
        if "yes" == ansText.lower():
            QtWidgets.QMessageBox.about(self, "Hey! "+self.userName, "\nYou are doing awesome man.")
        else :
            QtWidgets.QMessageBox.about(self, "Hey! "+self.userName, "\nThere is no point of clicking the button if you are not interested.")
