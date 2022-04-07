import sys 
from widgetQt import *
from funciones.ECC import encrypt


class formularioa(QtWidgets.QMainWindow):
    def __init__(self):
        super(formularioa, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.changePage)
        self.ui.pushButton_2.clicked.connect(self.restart)
        self.gmail = True
        self.encript = encrypt()
        
    def changePage(self):
        #self.ui.stackedWidget.setCurrentIndex(1)
        print(self.gmail)
        if self.gmail == True:
            t = self.ui.lineEdit.text()
            self.encript.generatemessagesing(t)
            self.ui.lineEdit.setText("contraseña")
            iclogin = QtGui.QIcon()
            iclogin.addPixmap(QtGui.QPixmap("./funciones/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.pushButton.setIcon(iclogin)
            self.ui.pushButton.setIconSize(QtCore.QSize(25, 25))
            self.ui.pushButton.setText("login")
            self.gmail = False
        else:
            t = self.ui.lineEdit.text()
            vr = self.encript.verifyer(t)
            print(vr)
            if vr['error'] == None:
                self.ui.stackedWidget.setCurrentIndex(1)    
    
    def restart(self):
        iclogin = QtGui.QIcon()
        iclogin.addPixmap(QtGui.QPixmap("./gmail.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.pushButton.setIcon(iclogin)
        self.ui.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.ui.lineEdit.setText("gmail")
        self.gmail = True
        print("restar")
        
        
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = formularioa()
    mi_app.show()
    sys.exit(app.exec_())