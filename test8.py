# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test8.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1564, 956)
        self.img_label = QtWidgets.QLabel(Form)
        self.img_label.setGeometry(QtCore.QRect(450, 80, 841, 461))
        self.img_label.setObjectName("img_label")
        self.startVideo = QtWidgets.QPushButton(Form)
        self.startVideo.setGeometry(QtCore.QRect(1360, 180, 180, 50))
        self.startVideo.setObjectName("startVideo")
        self.stopVideo = QtWidgets.QPushButton(Form)
        self.stopVideo.setGeometry(QtCore.QRect(1360, 250, 180, 50))
        self.stopVideo.setObjectName("stopVideo")
        self.exit_btn = QtWidgets.QPushButton(Form)
        self.exit_btn.setGeometry(QtCore.QRect(1360, 390, 181, 51))
        self.exit_btn.setObjectName("exit_btn")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(1350, 80, 71, 31))
        self.label_2.setObjectName("label_2")
        self.Id = QtWidgets.QTextEdit(Form)
        self.Id.setGeometry(QtCore.QRect(1420, 80, 104, 30))
        self.Id.setObjectName("Id")
        self.frequenceLabel = QtWidgets.QLabel(Form)
        self.frequenceLabel.setGeometry(QtCore.QRect(40, 600, 351, 211))
        self.frequenceLabel.setObjectName("frequenceLabel")
        self.deepLabel = QtWidgets.QLabel(Form)
        self.deepLabel.setGeometry(QtCore.QRect(50, 100, 331, 221))
        self.deepLabel.setObjectName("deepLabel")
        self.analysisBtn = QtWidgets.QPushButton(Form)
        self.analysisBtn.setGeometry(QtCore.QRect(1360, 320, 181, 51))
        self.analysisBtn.setObjectName("analysisBtn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 370, 297, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.depthLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.depthLabel.setFont(font)
        self.depthLabel.setObjectName("depthLabel")
        self.horizontalLayout_3.addWidget(self.depthLabel)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 820, 211, 101))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.frequencyLabel = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frequencyLabel.setFont(font)
        self.frequencyLabel.setObjectName("frequencyLabel")
        self.horizontalLayout_4.addWidget(self.frequencyLabel)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(0, 510, 421, 71))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 421, 71))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(710, -10, 331, 99))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(410, 0, 20, 981))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(420, 560, 1211, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1130, 30, 191, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.label_19 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout.addWidget(self.label_19)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(1310, 0, 20, 571))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(1010, 570, 20, 421))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.img_label_2 = QtWidgets.QLabel(Form)
        self.img_label_2.setGeometry(QtCore.QRect(1060, 680, 461, 241))
        self.img_label_2.setObjectName("img_label_2")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(1100, 590, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(460, 600, 521, 201))
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(470, 850, 191, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setMaximumSize(QtCore.QSize(126, 16777215))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_5.addWidget(self.label_22)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_6.addWidget(self.label_18)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(740, 850, 231, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_8.addWidget(self.label_21)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_7.addWidget(self.label_17)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "AI CPR "))
        self.img_label.setText(_translate("Form", "imgLabel"))
        self.startVideo.setText(_translate("Form", "開始錄影"))
        self.stopVideo.setText(_translate("Form", "結束錄影"))
        self.exit_btn.setText(_translate("Form", "離開"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">編號</span></p></body></html>"))
        self.frequenceLabel.setText(_translate("Form", "frequenceLabel"))
        self.deepLabel.setText(_translate("Form", "deepLabel"))
        self.analysisBtn.setText(_translate("Form", "總評"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">Depth</p></body></html>"))
        self.depthLabel.setText(_translate("Form", "<html><head/><body><p align=\"center\">0.0</p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\">Rate</p></body></html>"))
        self.frequencyLabel.setText(_translate("Form", "<html><head/><body><p align=\"center\">0.0</p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Compression  Rate</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Compression  Depth</span></p></body></html>"))
        self.label_20.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">CPR Screen</span></p></body></html>"))
        self.label_14.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Round</span></p></body></html>"))
        self.label_19.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt;\">0</span></p></body></html>"))
        self.img_label_2.setText(_translate("Form", "imgYOLOLabel"))
        self.label_15.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Compression Position</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "electrocardiogramLabel"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Depth</span></p></body></html>"))
        self.label_22.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">Abnormal</span></p></body></html>"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">   Rate</span></p></body></html>"))
        self.label_18.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">Abnormal</span></p></body></html>"))
        self.label_12.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Posture</span></p></body></html>"))
        self.label_21.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">Abnormal</span></p></body></html>"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Position</span></p></body></html>"))
        self.label_17.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">Abnormal</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())