# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_client.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_client(object):
    def setupUi(self, client):
        client.setObjectName("client")
        client.resize(1000, 800)
        font = QtGui.QFont()
        font.setFamily("Arial")
        client.setFont(font)
        client.setStyleSheet("QWidget{\n"
"background:#484848;\n"
"}\n"
"QAbstractButton{\n"
"border-style:none;\n"
"border-radius:0px;\n"
"padding:5px;\n"
"color:#DCDCDC;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #858585,stop:1 #383838);\n"
"}\n"
"QAbstractButton:hover{\n"
"color:#000000;\n"
"background-color:#008aff;\n"
"}\n"
"QAbstractButton:pressed{\n"
"color:#DCDCDC;\n"
"border-style:solid;\n"
"border-width:0px 0px 0px 4px;\n"
"padding:4px 4px 4px 2px;\n"
"border-color:#008aff;\n"
"background-color:#444444;\n"
"}\n"
"\n"
"QLabel{\n"
"color:#DCDCDC;\n"
"\n"
"\n"
"}\n"
"QLabel:focus{\n"
"border:1px solid #00BB9E;\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"border:1px solid #242424;\n"
"border-radius:3px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#484848;\n"
"selection-color:#DCDCDC;\n"
"}\n"
"QLineEdit:focus,QLineEdit:hover{\n"
"border:1px solid #242424;\n"
"}\n"
"QLineEdit{\n"
"border:1px solid #242424;\n"
"border-radius:3px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#484848;\n"
"selection-color:#DCDCDC;\n"
"}\n"
"\n"
"QLineEdit:focus,QLineEdit:hover{\n"
"border:1px solid #242424;\n"
"}\n"
"QLineEdit{\n"
"lineedit-password-character:9679;\n"
"}\n"
"QSlider::groove:horizontal,QSlider::add-page:horizontal{\n"
"height:3px;\n"
"border-radius:3px;\n"
"background:#18181a;\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"height:8px;\n"
"border-radius:3px;\n"
"background:#008aff;\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal{\n"
"width:12px;\n"
"margin-top:-5px;\n"
"margin-bottom:-4px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #DCDCDC,stop:0.8 #DCDCDC);\n"
"}\n"
"QSlider::groove:vertical,QSlider::sub-page:vertical{\n"
"width:3px;\n"
"border-radius:3px;\n"
"background:#18181a;\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:vertical{\n"
"width:8px;\n"
"border-radius:3px;\n"
"background:#008aff;\n"
"}\n"
"\n"
"\n"
"QSlider::handle:vertical{\n"
"height:12px;\n"
"margin-left:-5px;\n"
"margin-right:-4px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #DCDCDC,stop:0.8 #DCDCDC);\n"
"}\n"
"\n"
"\n"
"\n"
"QGroupBox::title {\n"
"pading:2px;\n"
"color:white;\n"
"subcontrol-position: top center;\n"
"border-top:0px ;\n"
"background:  transparent;} \n"
"font: 10pt \"Arial\";")
        client.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Video = QtWidgets.QLabel(client)
        self.Video.setGeometry(QtCore.QRect(10, 10, 600, 450))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Video.setFont(font)
        self.Video.setStyleSheet("font: 10pt \"Arial\";")
        self.Video.setText("")
        self.Video.setObjectName("Video")
        self.Button_Buzzer = QtWidgets.QPushButton(client)
        self.Button_Buzzer.setGeometry(QtCore.QRect(750, 425, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_Buzzer.setFont(font)
        self.Button_Buzzer.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Buzzer.setObjectName("Button_Buzzer")
        self.lineEdit_IP_Adress = QtWidgets.QLineEdit(client)
        self.lineEdit_IP_Adress.setGeometry(QtCore.QRect(160, 470, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_IP_Adress.setFont(font)
        self.lineEdit_IP_Adress.setStyleSheet("font: 10pt \"Arial\";")
        self.lineEdit_IP_Adress.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_IP_Adress.setObjectName("lineEdit_IP_Adress")
        self.Button_Connect = QtWidgets.QPushButton(client)
        self.Button_Connect.setGeometry(QtCore.QRect(280, 470, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_Connect.setFont(font)
        self.Button_Connect.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Connect.setObjectName("Button_Connect")
        self.Button_Video = QtWidgets.QPushButton(client)
        self.Button_Video.setGeometry(QtCore.QRect(400, 470, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_Video.setFont(font)
        self.Button_Video.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Video.setObjectName("Button_Video")
        self.Button_IMU = QtWidgets.QPushButton(client)
        self.Button_IMU.setGeometry(QtCore.QRect(630, 425, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_IMU.setFont(font)
        self.Button_IMU.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_IMU.setObjectName("Button_IMU")
        self.Button_Calibration = QtWidgets.QPushButton(client)
        self.Button_Calibration.setGeometry(QtCore.QRect(40, 470, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_Calibration.setFont(font)
        self.Button_Calibration.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Calibration.setObjectName("Button_Calibration")
        self.Button_Sonic = QtWidgets.QPushButton(client)
        self.Button_Sonic.setGeometry(QtCore.QRect(880, 425, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_Sonic.setFont(font)
        self.Button_Sonic.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Sonic.setObjectName("Button_Sonic")
        self.Button_LED = QtWidgets.QPushButton(client)
        self.Button_LED.setGeometry(QtCore.QRect(750, 355, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_LED.setFont(font)
        self.Button_LED.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_LED.setObjectName("Button_LED")
        self.label_6 = QtWidgets.QLabel(client)
        self.label_6.setGeometry(QtCore.QRect(913, 75, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 10pt \"Arial\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_attitude = QtWidgets.QLabel(client)
        self.label_attitude.setGeometry(QtCore.QRect(801, 185, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_attitude.setFont(font)
        self.label_attitude.setStyleSheet("font: 10pt \"Arial\";")
        self.label_attitude.setAlignment(QtCore.Qt.AlignCenter)
        self.label_attitude.setObjectName("label_attitude")
        self.label_roll = QtWidgets.QLabel(client)
        self.label_roll.setGeometry(QtCore.QRect(911, 255, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_roll.setFont(font)
        self.label_roll.setStyleSheet("font: 10pt \"Arial\";")
        self.label_roll.setAlignment(QtCore.Qt.AlignCenter)
        self.label_roll.setObjectName("label_roll")
        self.label_Y = QtWidgets.QLabel(client)
        self.label_Y.setGeometry(QtCore.QRect(891, 285, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_Y.setFont(font)
        self.label_Y.setStyleSheet("font: 10pt \"Arial\";")
        self.label_Y.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y.setObjectName("label_Y")
        self.label_Y_2 = QtWidgets.QLabel(client)
        self.label_Y_2.setGeometry(QtCore.QRect(786, 285, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_Y_2.setFont(font)
        self.label_Y_2.setStyleSheet("font: 10pt \"Arial\";")
        self.label_Y_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y_2.setObjectName("label_Y_2")
        self.label_Y_3 = QtWidgets.QLabel(client)
        self.label_Y_3.setGeometry(QtCore.QRect(686, 285, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_Y_3.setFont(font)
        self.label_Y_3.setStyleSheet("font: 10pt \"Arial\";")
        self.label_Y_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y_3.setObjectName("label_Y_3")
        self.label_Y_4 = QtWidgets.QLabel(client)
        self.label_Y_4.setGeometry(QtCore.QRect(921, 285, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_Y_4.setFont(font)
        self.label_Y_4.setStyleSheet("font: 10pt \"Arial\";")
        self.label_Y_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y_4.setObjectName("label_Y_4")
        self.label_X = QtWidgets.QLabel(client)
        self.label_X.setGeometry(QtCore.QRect(665, 265, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_X.setFont(font)
        self.label_X.setStyleSheet("font: 10pt \"Arial\";")
        self.label_X.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X.setObjectName("label_X")
        self.label_X_2 = QtWidgets.QLabel(client)
        self.label_X_2.setGeometry(QtCore.QRect(665, 170, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_X_2.setFont(font)
        self.label_X_2.setStyleSheet("font: 10pt \"Arial\";")
        self.label_X_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_2.setObjectName("label_X_2")
        self.label_X_3 = QtWidgets.QLabel(client)
        self.label_X_3.setGeometry(QtCore.QRect(665, 74, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_X_3.setFont(font)
        self.label_X_3.setStyleSheet("font: 10pt \"Arial\";")
        self.label_X_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_3.setObjectName("label_X_3")
        self.label_X_4 = QtWidgets.QLabel(client)
        self.label_X_4.setGeometry(QtCore.QRect(645, 90, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_X_4.setFont(font)
        self.label_X_4.setStyleSheet("font: 10pt \"Arial\";")
        self.label_X_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_4.setObjectName("label_X_4")
        self.label_X_5 = QtWidgets.QLabel(client)
        self.label_X_5.setGeometry(QtCore.QRect(736, 54, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_X_5.setFont(font)
        self.label_X_5.setStyleSheet("font: 10pt \"Arial\";")
        self.label_X_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_5.setObjectName("label_X_5")
        self.label_sonic = QtWidgets.QLabel(client)
        self.label_sonic.setGeometry(QtCore.QRect(870, 355, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_sonic.setFont(font)
        self.label_sonic.setStyleSheet("font: 10pt \"Arial\";")
        self.label_sonic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sonic.setObjectName("label_sonic")
        self.label_Y_5 = QtWidgets.QLabel(client)
        self.label_Y_5.setGeometry(QtCore.QRect(917, 751, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_Y_5.setFont(font)
        self.label_Y_5.setStyleSheet("font: 10pt \"Arial\";")
        self.label_Y_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y_5.setObjectName("label_Y_5")
        self.label_Y_6 = QtWidgets.QLabel(client)
        self.label_Y_6.setGeometry(QtCore.QRect(686, 751, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_Y_6.setFont(font)
        self.label_Y_6.setStyleSheet("font: 10pt \"Arial\";")
        self.label_Y_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y_6.setObjectName("label_Y_6")
        self.label_X_6 = QtWidgets.QLabel(client)
        self.label_X_6.setGeometry(QtCore.QRect(665, 545, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_X_6.setFont(font)
        self.label_X_6.setStyleSheet("font: 10pt \"Arial\";")
        self.label_X_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_6.setObjectName("label_X_6")
        self.label_Y_7 = QtWidgets.QLabel(client)
        self.label_Y_7.setGeometry(QtCore.QRect(786, 751, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_Y_7.setFont(font)
        self.label_Y_7.setStyleSheet("font: 10pt \"Arial\";")
        self.label_Y_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y_7.setObjectName("label_Y_7")
        self.label_X_7 = QtWidgets.QLabel(client)
        self.label_X_7.setGeometry(QtCore.QRect(665, 640, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_X_7.setFont(font)
        self.label_X_7.setStyleSheet("font: 10pt \"Arial\";")
        self.label_X_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_7.setObjectName("label_X_7")
        self.label_Y_8 = QtWidgets.QLabel(client)
        self.label_Y_8.setGeometry(QtCore.QRect(891, 751, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_Y_8.setFont(font)
        self.label_Y_8.setStyleSheet("font: 10pt \"Arial\";")
        self.label_Y_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y_8.setObjectName("label_Y_8")
        self.label_X_8 = QtWidgets.QLabel(client)
        self.label_X_8.setGeometry(QtCore.QRect(665, 735, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_X_8.setFont(font)
        self.label_X_8.setStyleSheet("font: 10pt \"Arial\";")
        self.label_X_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_8.setObjectName("label_X_8")
        self.label_position = QtWidgets.QLabel(client)
        self.label_position.setGeometry(QtCore.QRect(801, 655, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_position.setFont(font)
        self.label_position.setStyleSheet("font: 10pt \"Arial\";")
        self.label_position.setAlignment(QtCore.Qt.AlignCenter)
        self.label_position.setObjectName("label_position")
        self.label_X_9 = QtWidgets.QLabel(client)
        self.label_X_9.setGeometry(QtCore.QRect(650, 560, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_X_9.setFont(font)
        self.label_X_9.setStyleSheet("font: 10pt \"Arial\";")
        self.label_X_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_9.setObjectName("label_X_9")
        self.label_X_10 = QtWidgets.QLabel(client)
        self.label_X_10.setGeometry(QtCore.QRect(736, 525, 130, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_X_10.setFont(font)
        self.label_X_10.setStyleSheet("font: 10pt \"Arial\";")
        self.label_X_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_10.setObjectName("label_X_10")
        self.slider_roll = QtWidgets.QSlider(client)
        self.slider_roll.setGeometry(QtCore.QRect(916, 105, 20, 140))
        self.slider_roll.setStyleSheet("font: 10pt \"Arial\";")
        self.slider_roll.setMinimum(-20)
        self.slider_roll.setMaximum(20)
        self.slider_roll.setOrientation(QtCore.Qt.Vertical)
        self.slider_roll.setObjectName("slider_roll")
        self.slider_Z = QtWidgets.QSlider(client)
        self.slider_Z.setGeometry(QtCore.QRect(916, 580, 20, 140))
        self.slider_Z.setStyleSheet("font: 10pt \"Arial\";")
        self.slider_Z.setMinimum(-40)
        self.slider_Z.setMaximum(40)
        self.slider_Z.setOrientation(QtCore.Qt.Vertical)
        self.slider_Z.setObjectName("slider_Z")
        self.label_Z = QtWidgets.QLabel(client)
        self.label_Z.setGeometry(QtCore.QRect(911, 725, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_Z.setFont(font)
        self.label_Z.setStyleSheet("font: 10pt \"Arial\";")
        self.label_Z.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Z.setObjectName("label_Z")
        self.label_9 = QtWidgets.QLabel(client)
        self.label_9.setGeometry(QtCore.QRect(913, 556, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 10pt \"Arial\";")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.Button_Face_ID = QtWidgets.QPushButton(client)
        self.Button_Face_ID.setGeometry(QtCore.QRect(40, 510, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_Face_ID.setFont(font)
        self.Button_Face_ID.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Face_ID.setObjectName("Button_Face_ID")
        self.Button_Face_Recognition = QtWidgets.QPushButton(client)
        self.Button_Face_Recognition.setGeometry(QtCore.QRect(630, 355, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_Face_Recognition.setFont(font)
        self.Button_Face_Recognition.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Face_Recognition.setObjectName("Button_Face_Recognition")
        self.Button_Relax = QtWidgets.QPushButton(client)
        self.Button_Relax.setGeometry(QtCore.QRect(520, 470, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_Relax.setFont(font)
        self.Button_Relax.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Relax.setObjectName("Button_Relax")
        self.slider_head_1 = QtWidgets.QSlider(client)
        self.slider_head_1.setGeometry(QtCore.QRect(245, 765, 160, 20))
        self.slider_head_1.setStyleSheet("font: 10pt \"Arial\";")
        self.slider_head_1.setMaximum(180)
        self.slider_head_1.setProperty("value", 90)
        self.slider_head_1.setOrientation(QtCore.Qt.Horizontal)
        self.slider_head_1.setObjectName("slider_head_1")
        self.label_head_1 = QtWidgets.QLabel(client)
        self.label_head_1.setGeometry(QtCore.QRect(410, 765, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_head_1.setFont(font)
        self.label_head_1.setStyleSheet("font: 10pt \"Arial\";")
        self.label_head_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_head_1.setObjectName("label_head_1")
        self.label_10 = QtWidgets.QLabel(client)
        self.label_10.setGeometry(QtCore.QRect(195, 765, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font: 10pt \"Arial\";")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_8 = QtWidgets.QLabel(client)
        self.label_8.setGeometry(QtCore.QRect(480, 555, 30, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: 10pt \"Arial\";")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.slider_head = QtWidgets.QSlider(client)
        self.slider_head.setGeometry(QtCore.QRect(485, 572, 20, 160))
        self.slider_head.setStyleSheet("font: 10pt \"Arial\";")
        self.slider_head.setMaximum(180)
        self.slider_head.setProperty("value", 90)
        self.slider_head.setOrientation(QtCore.Qt.Vertical)
        self.slider_head.setObjectName("slider_head")
        self.label_head = QtWidgets.QLabel(client)
        self.label_head.setGeometry(QtCore.QRect(480, 732, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_head.setFont(font)
        self.label_head.setStyleSheet("font: 10pt \"Arial\";")
        self.label_head.setAlignment(QtCore.Qt.AlignCenter)
        self.label_head.setObjectName("label_head")
        self.label_7 = QtWidgets.QLabel(client)
        self.label_7.setGeometry(QtCore.QRect(553, 555, 36, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 10pt \"Arial\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_speed = QtWidgets.QLabel(client)
        self.label_speed.setGeometry(QtCore.QRect(563, 732, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_speed.setFont(font)
        self.label_speed.setStyleSheet("font: 10pt \"Arial\";")
        self.label_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speed.setObjectName("label_speed")
        self.slider_speed = QtWidgets.QSlider(client)
        self.slider_speed.setGeometry(QtCore.QRect(560, 572, 20, 160))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.slider_speed.setFont(font)
        self.slider_speed.setStyleSheet("font: 10pt \"Arial\";")
        self.slider_speed.setMinimum(2)
        self.slider_speed.setMaximum(10)
        self.slider_speed.setProperty("value", 8)
        self.slider_speed.setOrientation(QtCore.Qt.Vertical)
        self.slider_speed.setObjectName("slider_speed")
        self.progress_Power1 = QtWidgets.QProgressBar(client)
        self.progress_Power1.setGeometry(QtCore.QRect(45, 705, 120, 20))
        self.progress_Power1.setStyleSheet("QProgressBar::chunk {\n"
"background-color:#08aaff;\n"
"width: 20px;\n"
"}\n"
"QProgressBar {\n"
"border-top: 2px solid grey;\n"
"border-bottom: 2px solid grey;\n"
"border-right: 2px solid grey;\n"
"border-left: 2px solid grey;\n"
"border-radius: 0px;\n"
"background-color: #FFFFFF;\n"
"}\n"
"QProgressBar {\n"
"text-align: center; \n"
"color: rgb(0,0,0);\n"
"}\n"
"font: 10pt \"Arial\";")
        self.progress_Power1.setProperty("value", 100)
        self.progress_Power1.setFormat("")
        self.progress_Power1.setObjectName("progress_Power1")
        self.progress_Power2 = QtWidgets.QProgressBar(client)
        self.progress_Power2.setGeometry(QtCore.QRect(45, 755, 120, 20))
        self.progress_Power2.setStyleSheet("QProgressBar::chunk {\n"
"background-color:#26fa03;\n"
"width: 20px;\n"
"}\n"
"QProgressBar {\n"
"border: 2px solid grey;\n"
"border-radius: 0px;\n"
"background-color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"QProgressBar {\n"
"text-align: center; \n"
"color: rgb(0,0,0);\n"
"}\n"
"font: 10pt \"Arial\";")
        self.progress_Power2.setProperty("value", 100)
        self.progress_Power2.setFormat("")
        self.progress_Power2.setObjectName("progress_Power2")
        self.layoutWidget = QtWidgets.QWidget(client)
        self.layoutWidget.setGeometry(QtCore.QRect(25, 620, 121, 60))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ButtonActionMode1 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ButtonActionMode1.setFont(font)
        self.ButtonActionMode1.setStyleSheet("font: 10pt \"Arial\";")
        self.ButtonActionMode1.setObjectName("ButtonActionMode1")
        self.verticalLayout.addWidget(self.ButtonActionMode1)
        self.ButtonActionMode2 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ButtonActionMode2.setFont(font)
        self.ButtonActionMode2.setStyleSheet("font: 10pt \"Arial\";")
        self.ButtonActionMode2.setObjectName("ButtonActionMode2")
        self.verticalLayout.addWidget(self.ButtonActionMode2)
        self.layoutWidget1 = QtWidgets.QWidget(client)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 550, 111, 60))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ButtonGaitMode1 = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ButtonGaitMode1.setFont(font)
        self.ButtonGaitMode1.setStyleSheet("font: 10pt \"Arial\";")
        self.ButtonGaitMode1.setObjectName("ButtonGaitMode1")
        self.verticalLayout_2.addWidget(self.ButtonGaitMode1)
        self.ButtonGaitMode2 = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ButtonGaitMode2.setFont(font)
        self.ButtonGaitMode2.setStyleSheet("font: 10pt \"Arial\";")
        self.ButtonGaitMode2.setObjectName("ButtonGaitMode2")
        self.verticalLayout_2.addWidget(self.ButtonGaitMode2)
        self.label_RasPi = QtWidgets.QLabel(client)
        self.label_RasPi.setGeometry(QtCore.QRect(10, 757, 30, 15))
        self.label_RasPi.setStyleSheet("font: 10pt \"Arial\";")
        self.label_RasPi.setObjectName("label_RasPi")
        self.label_Load = QtWidgets.QLabel(client)
        self.label_Load.setGeometry(QtCore.QRect(10, 707, 30, 15))
        self.label_Load.setStyleSheet("font: 10pt \"Arial\";")
        self.label_Load.setObjectName("label_Load")
        self.Video.raise_()
        self.Button_Buzzer.raise_()
        self.lineEdit_IP_Adress.raise_()
        self.Button_Connect.raise_()
        self.Button_Video.raise_()
        self.Button_IMU.raise_()
        self.Button_Calibration.raise_()
        self.Button_Sonic.raise_()
        self.Button_LED.raise_()
        self.label_6.raise_()
        self.label_attitude.raise_()
        self.label_roll.raise_()
        self.label_Y.raise_()
        self.label_Y_2.raise_()
        self.label_Y_3.raise_()
        self.label_Y_4.raise_()
        self.label_X.raise_()
        self.label_X_2.raise_()
        self.label_X_3.raise_()
        self.label_X_4.raise_()
        self.label_X_5.raise_()
        self.label_sonic.raise_()
        self.label_Y_5.raise_()
        self.label_Y_6.raise_()
        self.label_X_6.raise_()
        self.label_Y_7.raise_()
        self.label_X_7.raise_()
        self.label_Y_8.raise_()
        self.label_X_8.raise_()
        self.label_position.raise_()
        self.label_X_9.raise_()
        self.label_X_10.raise_()
        self.slider_roll.raise_()
        self.slider_Z.raise_()
        self.label_Z.raise_()
        self.label_9.raise_()
        self.Button_Face_ID.raise_()
        self.Button_Face_Recognition.raise_()
        self.Button_Relax.raise_()
        self.slider_head_1.raise_()
        self.label_head_1.raise_()
        self.label_10.raise_()
        self.label_8.raise_()
        self.slider_head.raise_()
        self.label_head.raise_()
        self.label_7.raise_()
        self.label_speed.raise_()
        self.slider_speed.raise_()
        self.progress_Power2.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.label_RasPi.raise_()
        self.label_Load.raise_()
        self.progress_Power1.raise_()

        self.retranslateUi(client)
        QtCore.QMetaObject.connectSlotsByName(client)

    def retranslateUi(self, client):
        _translate = QtCore.QCoreApplication.translate
        client.setWindowTitle(_translate("client", "Freenove Client for Hexapod"))
        self.Button_Buzzer.setText(_translate("client", "Buzzer"))
        self.lineEdit_IP_Adress.setText(_translate("client", "192.168.1.121"))
        self.Button_Connect.setText(_translate("client", "Connect"))
        self.Button_Video.setText(_translate("client", "Open Video"))
        self.Button_IMU.setText(_translate("client", "Balance"))
        self.Button_Calibration.setText(_translate("client", "Calibration"))
        self.Button_Sonic.setText(_translate("client", "Sonic"))
        self.Button_LED.setText(_translate("client", "LED"))
        self.label_6.setText(_translate("client", "Roll"))
        self.label_attitude.setText(_translate("client", "(0,0)"))
        self.label_roll.setText(_translate("client", "0"))
        self.label_Y.setText(_translate("client", "15"))
        self.label_Y_2.setText(_translate("client", "0"))
        self.label_Y_3.setText(_translate("client", "-15"))
        self.label_Y_4.setText(_translate("client", "(Yaw)"))
        self.label_X.setText(_translate("client", "-15"))
        self.label_X_2.setText(_translate("client", "0"))
        self.label_X_3.setText(_translate("client", "15"))
        self.label_X_4.setText(_translate("client", "(Pitch)"))
        self.label_X_5.setText(_translate("client", "Attitude"))
        self.label_sonic.setText(_translate("client", "Obstacle:0cm"))
        self.label_Y_5.setText(_translate("client", "(X)"))
        self.label_Y_6.setText(_translate("client", "-40"))
        self.label_X_6.setText(_translate("client", "40"))
        self.label_Y_7.setText(_translate("client", "0"))
        self.label_X_7.setText(_translate("client", "0"))
        self.label_Y_8.setText(_translate("client", "40"))
        self.label_X_8.setText(_translate("client", "-40"))
        self.label_position.setText(_translate("client", "(0,0)"))
        self.label_X_9.setText(_translate("client", "(Y)"))
        self.label_X_10.setText(_translate("client", "Position"))
        self.label_Z.setText(_translate("client", "0"))
        self.label_9.setText(_translate("client", "Z"))
        self.Button_Face_ID.setText(_translate("client", "Face ID"))
        self.Button_Face_Recognition.setText(_translate("client", "Face Recog"))
        self.Button_Relax.setText(_translate("client", "Relax"))
        self.label_head_1.setText(_translate("client", "90"))
        self.label_10.setText(_translate("client", "Head"))
        self.label_8.setText(_translate("client", "Head"))
        self.label_head.setText(_translate("client", "90"))
        self.label_7.setText(_translate("client", "Speed"))
        self.label_speed.setText(_translate("client", "8"))
        self.ButtonActionMode1.setText(_translate("client", "Action Mode 1"))
        self.ButtonActionMode2.setText(_translate("client", "Action Mode 2"))
        self.ButtonGaitMode1.setText(_translate("client", "Gait Mode 1"))
        self.ButtonGaitMode2.setText(_translate("client", "Gait Mode 2"))
        self.label_RasPi.setText(_translate("client", "RasPi"))
        self.label_Load.setText(_translate("client", "Load"))
