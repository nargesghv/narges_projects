from PyQt5 import QtWidgets,uic
import sys
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui,self).__init__()
        uic.loadUi(r"C:/Users/nariv/Desktop/Project/writting_script/app.ui",self)
        self.show()
        self.addButton.clicked.connect(self.add)
        self.DoneButton.clicked.connect(self.Done)
        self.ClearButton.clicked.connect(self.Clear)
    def add(self):
        if self.lineEdit.text():
            strjob=self.lineEdit.text()
            self.listWidget.addItem(strjob)
            self.lineEdit.setText("")
            self.lineEdit.setFocus()
    def Done(self):
        clickedIndex= self.listWidget.currentRow()
        self.listWidget.takeItem(clickedIndex)
    def Clear(self):
        self.listWidget.clear()


app=QtWidgets.QApplication(sys.argv) 
window=Ui()      
app.exec_()


