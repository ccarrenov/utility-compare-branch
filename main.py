import sys
from  PyQt5 import QtWidgets
from view.main_view import MainView

if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    view = MainView()
    view.setFixedSize(800, 640)    
    view.show()
    sys.exit(app.exec_())