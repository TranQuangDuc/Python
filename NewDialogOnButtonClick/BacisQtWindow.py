from PySide2 import QtWidgets   #for QT widgets and function. pip install PySide2
import firstWindow
from PySide2.QtGui import QIcon # Get the package to add an icon
import NewWindow

class MyWindow(firstWindow.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        # Below line setup all the UI components we created in QTDesigner. If we comment this line, It will create a blank window.
        # Try it
        self.setupUi(self)
        # Give a good name to our window.
        self.setWindowTitle("MyFirstQTWindowApp")
        # Add an icon to window.
        self.setWindowIcon(QIcon("D:\\@Study\\Python\\#QTBlogCode\\NewDialogOnButtonClick\\Code\\QTIcon.png"))
        # Below function will connect Button to handler function
        self.Push_PB.clicked.connect(self.PushButtonHandler)
    # __init__

    def PushButtonHandler(self):
        text = self.AddName_LE.text()
        QtWidgets.QMessageBox.about(self, "Namaste! "+text, "Welcome to QT world.\nAfter clicking this OK button, your second window will open.")
        self.signupDialog = NewWindow.CNewWindow(text)
        #self.hide()
        self.signupDialog.show()


    # PushButtonHandler




#if __name__ == "__main__":

app = QtWidgets.QApplication()
MyFirstWindow = MyWindow()
MyFirstWindow.show()
app.exec_()
