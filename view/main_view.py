from  PyQt5 import QtWidgets, QtGui
from view.form.compareform import CloneToCompareForm
from view.build.doprop import LoadProperties

#load properties
prop = LoadProperties()

class MainView(QtWidgets.QDialog):    

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Compare Branch')
        formLayout = CloneToCompareForm(self).getFormLayout()
        # ADD FORM
        self.setLayout(formLayout)
        # changing the background color to yellow
        self.setStyleSheet(prop.getConfig().get("THEME", "window.background"))
        self.setWindowIcon(QtGui.QIcon(prop.windowIcon))