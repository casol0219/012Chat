# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/012Chat_emoji.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from server import *
from client import *

class Ui_Form(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.fontDB = QtGui.QFontDatabase()
        fontPath = '\\'.join(__file__.split('\\')[:-2])+'\\resource\\SEBANG Gothic.ttf'
        self.fontDB.addApplicationFont(fontPath)
        self.setFont(QtGui.QFont("SEBANG Gothic", 10))
        self.setupUi()
        self.clickFrodo()

    #서버로 이모티콘 이름 전송
    def sendEmoji(self, name):
        send_message(name)

    def disconnectButtonSignals(self, button):
        try:
                button.clicked.disconnect()
        except TypeError:
                pass

    def connectButton(self, button, image):
        self.disconnectButtonSignals(button)
        button.clicked.connect(lambda: self.sendEmoji(image))

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(465, 267)
        self.setStyleSheet("background-color: #FFFFFF;")
        self.Icon_emoji = QtWidgets.QLabel(self)
        self.Icon_emoji.setGeometry(QtCore.QRect(16, 16, 24, 24))
        self.Icon_emoji.setText("")
        self.Icon_emoji.setPixmap(QtGui.QPixmap(":/icon/emoji-happy.png"))
        self.Icon_emoji.setObjectName("Icon_emoji")
        self.Text_emoji = QtWidgets.QLabel(self)
        self.Text_emoji.setGeometry(QtCore.QRect(48, 19, 56, 19))
        self.Text_emoji.setStyleSheet("color: #343A40;")
        self.Text_emoji.setFont(QtGui.QFont("SEBANG Gothic", 11))
        self.Text_emoji.setObjectName("Text_emoji")
        self.Widget_emojiTab = QtWidgets.QWidget(self)
        self.Widget_emojiTab.setGeometry(QtCore.QRect(16, 48, 432, 32))
        self.Widget_emojiTab.setMinimumSize(QtCore.QSize(432, 32))
        self.Widget_emojiTab.setMaximumSize(QtCore.QSize(432, 32))
        self.Widget_emojiTab.setObjectName("Widget_emojiTab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Widget_emojiTab)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Btn_tabFrodo = QtWidgets.QPushButton(self.Widget_emojiTab)
        self.Btn_tabFrodo.setMinimumSize(QtCore.QSize(72, 32))
        self.Btn_tabFrodo.setMaximumSize(QtCore.QSize(72, 32))
        self.Btn_tabFrodo.setStyleSheet("QPushButton {\n"
"    border-style: none;\n"
"    selection-background-color: #F0F0F0;\n"
"    background-color: #F0F0F0;\n"
"}\n"
"QPushButton::checked {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #6F3FE2;\n"
"    selection-background-color: #F0F0F0;\n"
"}")
        self.Btn_tabFrodo.setText("")
        self.Btn_tabFrodo.clicked.connect(self.clickFrodo)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/emoji/1002.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_tabFrodo.setIcon(icon)
        self.Btn_tabFrodo.setCheckable(True)
        self.Btn_tabFrodo.setChecked(True)
        self.Btn_tabFrodo.setObjectName("Btn_tabFrodo")
        self.horizontalLayout_2.addWidget(self.Btn_tabFrodo)
        self.Btn_tabNeo = QtWidgets.QPushButton(self.Widget_emojiTab)
        self.Btn_tabNeo.setMinimumSize(QtCore.QSize(72, 32))
        self.Btn_tabNeo.setMaximumSize(QtCore.QSize(72, 32))
        self.Btn_tabNeo.setStyleSheet("QPushButton {\n"
"    border-style: none;\n"
"    selection-background-color: #F0F0F0;\n"
"    background-color: #F0F0F0;\n"
"}\n"
"QPushButton::checked {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #6F3FE2;\n"
"    selection-background-color: #F0F0F0;\n"
"}")
        self.Btn_tabNeo.setText("")
        self.Btn_tabNeo.clicked.connect(self.clickNeo)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/emoji/1007.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_tabNeo.setIcon(icon1)
        self.Btn_tabNeo.setCheckable(True)
        self.Btn_tabNeo.setObjectName("Btn_tabNeo")
        self.horizontalLayout_2.addWidget(self.Btn_tabNeo)
        self.Btn_tabTube = QtWidgets.QPushButton(self.Widget_emojiTab)
        self.Btn_tabTube.setMinimumSize(QtCore.QSize(72, 32))
        self.Btn_tabTube.setMaximumSize(QtCore.QSize(72, 32))
        self.Btn_tabTube.setStyleSheet("QPushButton {\n"
"    border-style: none;\n"
"    selection-background-color: #F0F0F0;\n"
"    background-color: #F0F0F0;\n"
"}\n"
"QPushButton::checked {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #6F3FE2;\n"
"    selection-background-color: #F0F0F0;\n"
"}")
        self.Btn_tabTube.setText("")
        self.Btn_tabTube.clicked.connect(self.clickTube)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/emoji/1013.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_tabTube.setIcon(icon2)
        self.Btn_tabTube.setCheckable(True)
        self.Btn_tabTube.setObjectName("Btn_tabTube")
        self.horizontalLayout_2.addWidget(self.Btn_tabTube)
        self.Btn_tabApeach = QtWidgets.QPushButton(self.Widget_emojiTab)
        self.Btn_tabApeach.setMinimumSize(QtCore.QSize(72, 32))
        self.Btn_tabApeach.setMaximumSize(QtCore.QSize(72, 32))
        self.Btn_tabApeach.setStyleSheet("QPushButton {\n"
"    border-style: none;\n"
"    selection-background-color: #F0F0F0;\n"
"    background-color: #F0F0F0;\n"
"}\n"
"QPushButton::checked {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #6F3FE2;\n"
"    selection-background-color: #F0F0F0;\n"
"}")
        self.Btn_tabApeach.setText("")
        self.Btn_tabApeach.clicked.connect(self.clickApeach)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/emoji/1023.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_tabApeach.setIcon(icon3)
        self.Btn_tabApeach.setCheckable(True)
        self.Btn_tabApeach.setObjectName("Btn_tabApeach")
        self.horizontalLayout_2.addWidget(self.Btn_tabApeach)
        self.Btn_tabMuzi = QtWidgets.QPushButton(self.Widget_emojiTab)
        self.Btn_tabMuzi.setMinimumSize(QtCore.QSize(72, 32))
        self.Btn_tabMuzi.setMaximumSize(QtCore.QSize(72, 32))
        self.Btn_tabMuzi.setStyleSheet("QPushButton {\n"
"    border-style: none;\n"
"    selection-background-color: #F0F0F0;\n"
"    background-color: #F0F0F0;\n"
"}\n"
"QPushButton::checked {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #6F3FE2;\n"
"    selection-background-color: #F0F0F0;\n"
"}")
        self.Btn_tabMuzi.setText("")
        self.Btn_tabMuzi.clicked.connect(self.clickMuzi)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/emoji/1026.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_tabMuzi.setIcon(icon4)
        self.Btn_tabMuzi.setCheckable(True)
        self.Btn_tabMuzi.setObjectName("Btn_tabMuzi")
        self.horizontalLayout_2.addWidget(self.Btn_tabMuzi)
        self.Btn_tabJayG = QtWidgets.QPushButton(self.Widget_emojiTab)
        self.Btn_tabJayG.setMinimumSize(QtCore.QSize(72, 32))
        self.Btn_tabJayG.setMaximumSize(QtCore.QSize(72, 32))
        self.Btn_tabJayG.setStyleSheet("QPushButton {\n"
"    border-style: none;\n"
"    selection-background-color: #F0F0F0;\n"
"    background-color: #F0F0F0;\n"
"}\n"
"QPushButton::checked {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #6F3FE2;\n"
"    selection-background-color: #F0F0F0;\n"
"}")
        self.Btn_tabJayG.setText("")
        self.Btn_tabJayG.clicked.connect(self.clickJayG)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/emoji/1033.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_tabJayG.setIcon(icon5)
        self.Btn_tabJayG.setCheckable(True)
        self.Btn_tabJayG.setObjectName("Btn_tabJayG")
        self.horizontalLayout_2.addWidget(self.Btn_tabJayG)
        self.widget__Emoji = QtWidgets.QWidget(self)
        self.widget__Emoji.setEnabled(True)
        self.widget__Emoji.setGeometry(QtCore.QRect(16, 80, 432, 171))
        self.widget__Emoji.setMinimumSize(QtCore.QSize(432, 171))
        self.widget__Emoji.setMaximumSize(QtCore.QSize(432, 171))
        self.widget__Emoji.setStyleSheet("background-color: #f0f0f0;")
        self.widget__Emoji.setObjectName("widget__Emoji")
        self.scrollArea_Frodo = QtWidgets.QScrollArea(self.widget__Emoji)
        self.scrollArea_Frodo.setEnabled(True)
        self.scrollArea_Frodo.setGeometry(QtCore.QRect(8, 8, 417, 155))
        self.scrollArea_Frodo.setMinimumSize(QtCore.QSize(417, 155))
        self.scrollArea_Frodo.setMaximumSize(QtCore.QSize(417, 155))
        self.scrollArea_Frodo.setStyleSheet("QScrollArea {\n"
"    border-style: none;\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border-style: none;\n"
"    background:white;\n"
"    width:10px;    \n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {         \n"
"    min-height: 0px;\n"
"    border-style: none;\n"
"    border-radius: 5px;\n"
"    background-color: #6F3FE2;\n"
"}\n"
"QScrollBar::add-line:vertical {       \n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}")
        self.scrollArea_Frodo.setWidgetResizable(True)
        self.scrollArea_Frodo.setObjectName("scrollArea_Frodo")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 407, 192))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.Btn_1001 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Btn_1001.setMinimumSize(QtCore.QSize(84, 84))
        self.Btn_1001.setMaximumSize(QtCore.QSize(84, 84))
        self.Btn_1001.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1001.png)")
        self.Btn_1001.setText("")
        self.Btn_1001.setObjectName("Btn_1001")
        self.gridLayout.addWidget(self.Btn_1001, 0, 0, 1, 1)
        self.Btn_1002 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Btn_1002.setMinimumSize(QtCore.QSize(84, 84))
        self.Btn_1002.setMaximumSize(QtCore.QSize(84, 84))
        self.Btn_1002.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1002.png)")
        self.Btn_1002.setText("")
        self.Btn_1002.setObjectName("Btn_1002")
        self.gridLayout.addWidget(self.Btn_1002, 0, 1, 1, 1)
        self.Btn_1003 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Btn_1003.setMinimumSize(QtCore.QSize(84, 84))
        self.Btn_1003.setMaximumSize(QtCore.QSize(84, 84))
        self.Btn_1003.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1003.png)")
        self.Btn_1003.setText("")
        self.Btn_1003.setObjectName("Btn_1003")
        self.gridLayout.addWidget(self.Btn_1003, 0, 2, 1, 1)
        self.Btn_1004 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Btn_1004.setMinimumSize(QtCore.QSize(84, 84))
        self.Btn_1004.setMaximumSize(QtCore.QSize(84, 84))
        self.Btn_1004.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1004.png)")
        self.Btn_1004.setText("")
        self.Btn_1004.setObjectName("Btn_1004")
        self.gridLayout.addWidget(self.Btn_1004, 0, 3, 1, 1)
        self.Btn_1005 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Btn_1005.setMinimumSize(QtCore.QSize(84, 84))
        self.Btn_1005.setMaximumSize(QtCore.QSize(84, 84))
        self.Btn_1005.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1005.png)")
        self.Btn_1005.setText("")
        self.Btn_1005.setObjectName("Btn_1005")
        self.gridLayout.addWidget(self.Btn_1005, 1, 0, 1, 1)
        self.Btn_1006 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Btn_1006.setMinimumSize(QtCore.QSize(84, 84))
        self.Btn_1006.setMaximumSize(QtCore.QSize(84, 84))
        self.Btn_1006.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1006.png)")
        self.Btn_1006.setText("")
        self.Btn_1006.setObjectName("Btn_1006")
        self.gridLayout.addWidget(self.Btn_1006, 1, 1, 1, 1)
        self.scrollArea_Frodo.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Emoji"))
        self.Text_emoji.setText(_translate("Form", "Emoji"))

    def clickFrodo(self):
        self.Btn_tabFrodo.setChecked(True)
        self.Btn_tabNeo.setChecked(False)
        self.Btn_tabApeach.setChecked(False)
        self.Btn_tabTube.setChecked(False)
        self.Btn_tabMuzi.setChecked(False)
        self.Btn_tabJayG.setChecked(False)
        self.Btn_1006.show()
        self.Btn_1001.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1001.png)")
        self.Btn_1002.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1002.png)")
        self.Btn_1003.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1003.png)")
        self.Btn_1004.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1004.png)")
        self.Btn_1005.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1005.png)")
        self.Btn_1006.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1006.png)")
        self.connectButton(self.Btn_1001, '1001.png')
        self.connectButton(self.Btn_1002, '1002.png')
        self.connectButton(self.Btn_1003, '1003.png')
        self.connectButton(self.Btn_1004, '1004.png')
        self.connectButton(self.Btn_1005, '1005.png')
        self.connectButton(self.Btn_1006, '1006.png')

    def clickNeo(self):
        self.Btn_tabFrodo.setChecked(False)
        self.Btn_tabNeo.setChecked(True)
        self.Btn_tabApeach.setChecked(False)
        self.Btn_tabTube.setChecked(False)
        self.Btn_tabMuzi.setChecked(False)
        self.Btn_tabJayG.setChecked(False)
        self.Btn_1006.show()
        self.Btn_1001.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1007.png)")
        self.Btn_1002.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1008.png)")
        self.Btn_1003.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1009.png)")
        self.Btn_1004.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1010.png)")
        self.Btn_1005.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1011.png)")
        self.Btn_1006.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1012.png)")
        self.connectButton(self.Btn_1001, '1007.png')
        self.connectButton(self.Btn_1002, '1008.png')
        self.connectButton(self.Btn_1003, '1009.png')
        self.connectButton(self.Btn_1004, '1010.png')
        self.connectButton(self.Btn_1005, '1011.png')
        self.connectButton(self.Btn_1006, '1012.png')

    def clickApeach(self):
        self.Btn_tabFrodo.setChecked(False)
        self.Btn_tabNeo.setChecked(False)
        self.Btn_tabApeach.setChecked(True)
        self.Btn_tabTube.setChecked(False)
        self.Btn_tabMuzi.setChecked(False)
        self.Btn_tabJayG.setChecked(False)
        self.Btn_1006.hide()
        self.Btn_1001.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1018.png)")
        self.Btn_1002.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1019.png)")
        self.Btn_1003.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1020.png)")
        self.Btn_1004.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1021.png)")
        self.Btn_1005.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1022.png)")
        self.connectButton(self.Btn_1001, '1018.png')
        self.connectButton(self.Btn_1002, '1019.png')
        self.connectButton(self.Btn_1003, '1020.png')
        self.connectButton(self.Btn_1004, '1021.png')
        self.connectButton(self.Btn_1005, '1022.png')
        
    def clickTube(self):
        self.Btn_tabFrodo.setChecked(False)
        self.Btn_tabNeo.setChecked(False)
        self.Btn_tabApeach.setChecked(False)
        self.Btn_tabTube.setChecked(True)
        self.Btn_tabMuzi.setChecked(False)
        self.Btn_tabJayG.setChecked(False)
        self.Btn_1006.hide()
        self.Btn_1001.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1013.png)")
        self.Btn_1002.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1014.png)")
        self.Btn_1003.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1015.png)")
        self.Btn_1004.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1016.png)")
        self.Btn_1005.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1017.png)")
        self.connectButton(self.Btn_1001, '1013.png')
        self.connectButton(self.Btn_1002, '1014.png')
        self.connectButton(self.Btn_1003, '1015.png')
        self.connectButton(self.Btn_1004, '1016.png')
        self.connectButton(self.Btn_1005, '1017.png')

    def clickMuzi(self):
        self.Btn_tabFrodo.setChecked(False)
        self.Btn_tabNeo.setChecked(False)
        self.Btn_tabApeach.setChecked(False)
        self.Btn_tabTube.setChecked(False)
        self.Btn_tabMuzi.setChecked(True)
        self.Btn_tabJayG.setChecked(False)
        self.Btn_1006.show()
        self.Btn_1001.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1024.png)")
        self.Btn_1002.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1025.png)")
        self.Btn_1003.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1026.png)")
        self.Btn_1004.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1027.png)")
        self.Btn_1005.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1028.png)")
        self.Btn_1006.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1029.png)")
        self.connectButton(self.Btn_1001, '1024.png')
        self.connectButton(self.Btn_1002, '1025.png')
        self.connectButton(self.Btn_1003, '1026.png')
        self.connectButton(self.Btn_1004, '1027.png')
        self.connectButton(self.Btn_1005, '1028.png')
        self.connectButton(self.Btn_1006, '1029.png')

    def clickJayG(self):
        self.Btn_tabFrodo.setChecked(False)
        self.Btn_tabNeo.setChecked(False)
        self.Btn_tabApeach.setChecked(False)
        self.Btn_tabTube.setChecked(False)
        self.Btn_tabMuzi.setChecked(False)
        self.Btn_tabJayG.setChecked(True)
        self.Btn_1001.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1030.png)")
        self.Btn_1002.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1031.png)")
        self.Btn_1003.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1032.png)")
        self.Btn_1004.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1033.png)")
        self.Btn_1005.setStyleSheet("selection-background-color: #F0F0F0;\n"
"background-color: #F0F0F0;\n"
"border-image: url(:/emoji/1034.png)")
        self.Btn_1006.hide()
        self.connectButton(self.Btn_1001, '1030.png')
        self.connectButton(self.Btn_1002, '1031.png')
        self.connectButton(self.Btn_1003, '1032.png')
        self.connectButton(self.Btn_1004, '1033.png')
        self.connectButton(self.Btn_1005, '1034.png')

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = Ui_Form()
    Form.show()
    sys.exit(app.exec_())
