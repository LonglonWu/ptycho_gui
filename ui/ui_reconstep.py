# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_reconstep.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 551)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.canvas_object = MplCanvas(self.centralwidget)
        self.canvas_object.setGeometry(QtCore.QRect(10, 40, 311, 291))
        self.canvas_object.setObjectName("canvas_object")
        self.canvas_probe = MplCanvas(self.centralwidget)
        self.canvas_probe.setGeometry(QtCore.QRect(330, 40, 311, 291))
        self.canvas_probe.setObjectName("canvas_probe")
        self.cb_image_object = QtWidgets.QComboBox(self.centralwidget)
        self.cb_image_object.setGeometry(QtCore.QRect(10, 10, 311, 27))
        self.cb_image_object.setObjectName("cb_image_object")
        self.cb_image_object.addItem("")
        self.cb_image_object.addItem("")
        self.cb_image_probe = QtWidgets.QComboBox(self.centralwidget)
        self.cb_image_probe.setGeometry(QtCore.QRect(330, 10, 311, 27))
        self.cb_image_probe.setObjectName("cb_image_probe")
        self.cb_image_probe.addItem("")
        self.cb_image_probe.addItem("")
        self.canvas_object_chi = MplCanvas(self.centralwidget)
        self.canvas_object_chi.setGeometry(QtCore.QRect(10, 320, 311, 91))
        self.canvas_object_chi.setObjectName("canvas_object_chi")
        self.canvas_probe_chi = MplCanvas(self.centralwidget)
        self.canvas_probe_chi.setGeometry(QtCore.QRect(330, 320, 311, 91))
        self.canvas_probe_chi.setObjectName("canvas_probe_chi")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 400, 631, 141))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slider_iters = QtWidgets.QSlider(self.widget)
        self.slider_iters.setMinimum(1)
        self.slider_iters.setOrientation(QtCore.Qt.Horizontal)
        self.slider_iters.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.slider_iters.setTickInterval(5)
        self.slider_iters.setObjectName("slider_iters")
        self.horizontalLayout.addWidget(self.slider_iters)
        self.sb_iter = QtWidgets.QSpinBox(self.widget)
        self.sb_iter.setMinimum(1)
        self.sb_iter.setMaximum(9999)
        self.sb_iter.setObjectName("sb_iter")
        self.horizontalLayout.addWidget(self.sb_iter)
        self.ck_live = QtWidgets.QCheckBox(self.widget)
        self.ck_live.setChecked(True)
        self.ck_live.setObjectName("ck_live")
        self.horizontalLayout.addWidget(self.ck_live)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 8, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 1, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 8, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 0, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 7, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.btn_close = QtWidgets.QPushButton(self.widget)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_2.addWidget(self.btn_close)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.canvas_object.raise_()
        self.canvas_probe.raise_()
        self.cb_image_object.raise_()
        self.cb_image_probe.raise_()
        self.progressBar.raise_()
        self.btn_close.raise_()
        self.slider_iters.raise_()
        self.sb_iter.raise_()
        self.progressBar.raise_()
        self.canvas_object_chi.raise_()
        self.canvas_probe_chi.raise_()
        self.progressBar.raise_()
        self.btn_close.raise_()
        self.slider_iters.raise_()
        self.sb_iter.raise_()
        self.ck_live.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.spinBox.raise_()
        self.label_3.raise_()
        self.spinBox_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.doubleSpinBox.raise_()
        self.pushButton_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NSLS-II HXN Pytchography Recon. Monitor"))
        self.cb_image_object.setItemText(0, _translate("MainWindow", "object phase"))
        self.cb_image_object.setItemText(1, _translate("MainWindow", "object amplitude"))
        self.cb_image_probe.setItemText(0, _translate("MainWindow", "probe amplitude"))
        self.cb_image_probe.setItemText(1, _translate("MainWindow", "probe phase"))
        self.ck_live.setText(_translate("MainWindow", "live"))
        self.pushButton_3.setText(_translate("MainWindow", "Apply"))
        self.pushButton_2.setText(_translate("MainWindow", "Apply"))
        self.label_3.setText(_translate("MainWindow", "max"))
        self.label.setText(_translate("MainWindow", "Background remover"))
        self.label_2.setText(_translate("MainWindow", "min"))
        self.label_4.setText(_translate("MainWindow", "Periodic artifact remover"))
        self.label_5.setText(_translate("MainWindow", "param"))
        self.pushButton.setText(_translate("MainWindow", "Rot"))
        self.btn_close.setText(_translate("MainWindow", "Close"))

from core.widgets.mplcanvas import MplCanvas
