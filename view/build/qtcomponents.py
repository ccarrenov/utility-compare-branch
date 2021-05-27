from  PyQt5 import QtWidgets, QtCore, QtGui
from view.build.doprop import LoadProperties

prop = LoadProperties()

def createPushButton(keyProp):
    pushButton = QtWidgets.QPushButton(prop.getConfig().get("FORM_PARAMETERS", keyProp));
    pushButton.setStyleSheet(prop.getConfig().get("THEME", "window.font.color.push.button"))
    return pushButton

def createLabel(keyProp):
    label = QtWidgets.QLabel(prop.getConfig().get("FORM_PARAMETERS", keyProp))
    label.setStyleSheet(prop.getConfig().get("THEME", "window.font.color.label"))
    return label

def createLabelTitle(keyProp):
    label = QtWidgets.QLabel(prop.getConfig().get("FORM_PARAMETERS", keyProp))
    label.setStyleSheet(prop.getConfig().get("THEME", "window.font.color.title"))
    return label    

def createLineEdit(keyProp):
    lineEdit = QtWidgets.QLineEdit(prop.getConfig().get("FORM_PARAMETERS", keyProp))
    lineEdit.setStyleSheet(prop.getConfig().get("THEME", "window.font.color.line.edit") + prop.getConfig().get("THEME", "window.background.color.line.edit"))
    return lineEdit

def createLineEditDisabled(text, disabled):
    lineEdit = QtWidgets.QLineEdit(text)
    lineEdit.setDisabled(disabled)
    lineEdit.setStyleSheet(prop.getConfig().get("THEME", "window.font.color.line.edit"))
    return lineEdit         