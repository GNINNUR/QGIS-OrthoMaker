# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\anfla\.qgis2\python\plugins\OrthoMaker\ortho_maker_dialog_base.ui'
#
# Created: Tue Mar 15 10:10:43 2016
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_OrthoMakerDialogBase(object):
    def setupUi(self, OrthoMakerDialogBase):
        OrthoMakerDialogBase.setObjectName(_fromUtf8("OrthoMakerDialogBase"))
        OrthoMakerDialogBase.resize(396, 691)
        self.button_box = QtGui.QDialogButtonBox(OrthoMakerDialogBase)
        self.button_box.setGeometry(QtCore.QRect(40, 650, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.progressBar = QtGui.QProgressBar(OrthoMakerDialogBase)
        self.progressBar.setGeometry(QtCore.QRect(30, 610, 361, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.checkBoxDelTiff = QtGui.QCheckBox(OrthoMakerDialogBase)
        self.checkBoxDelTiff.setGeometry(QtCore.QRect(230, 530, 141, 17))
        self.checkBoxDelTiff.setObjectName(_fromUtf8("checkBoxDelTiff"))
        self.groupBox_3 = QtGui.QGroupBox(OrthoMakerDialogBase)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 130, 371, 151))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.inDir = QtGui.QLineEdit(self.groupBox_3)
        self.inDir.setGeometry(QtCore.QRect(20, 90, 291, 21))
        self.inDir.setObjectName(_fromUtf8("inDir"))
        self.pushButton_Input = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_Input.setGeometry(QtCore.QRect(318, 90, 31, 21))
        self.pushButton_Input.setObjectName(_fromUtf8("pushButton_Input"))
        self.scanSub = QtGui.QCheckBox(self.groupBox_3)
        self.scanSub.setGeometry(QtCore.QRect(20, 120, 101, 17))
        self.scanSub.setObjectName(_fromUtf8("scanSub"))
        self.inField1 = QtGui.QComboBox(self.groupBox_3)
        self.inField1.setGeometry(QtCore.QRect(20, 40, 331, 22))
        self.inField1.setObjectName(_fromUtf8("inField1"))
        self.radioButton_fieldpath = QtGui.QRadioButton(self.groupBox_3)
        self.radioButton_fieldpath.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.radioButton_fieldpath.setObjectName(_fromUtf8("radioButton_fieldpath"))
        self.radioButton_txtpath = QtGui.QRadioButton(self.groupBox_3)
        self.radioButton_txtpath.setGeometry(QtCore.QRect(20, 70, 82, 17))
        self.radioButton_txtpath.setObjectName(_fromUtf8("radioButton_txtpath"))
        self.groupBox_2 = QtGui.QGroupBox(OrthoMakerDialogBase)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 371, 101))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.inShapeA = QtGui.QComboBox(self.groupBox_2)
        self.inShapeA.setGeometry(QtCore.QRect(20, 30, 331, 22))
        self.inShapeA.setObjectName(_fromUtf8("inShapeA"))
        self.useSelectedA = QtGui.QCheckBox(self.groupBox_2)
        self.useSelectedA.setGeometry(QtCore.QRect(20, 70, 181, 17))
        self.useSelectedA.setObjectName(_fromUtf8("useSelectedA"))
        self.checkBox_bbox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_bbox.setGeometry(QtCore.QRect(190, 70, 161, 17))
        self.checkBox_bbox.setObjectName(_fromUtf8("checkBox_bbox"))
        self.checkBoxSTR = QtGui.QCheckBox(OrthoMakerDialogBase)
        self.checkBoxSTR.setGeometry(QtCore.QRect(230, 510, 141, 17))
        self.checkBoxSTR.setObjectName(_fromUtf8("checkBoxSTR"))
        self.groupBox_4 = QtGui.QGroupBox(OrthoMakerDialogBase)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 290, 371, 81))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.outDir = QtGui.QLineEdit(self.groupBox_4)
        self.outDir.setGeometry(QtCore.QRect(22, 30, 291, 21))
        self.outDir.setObjectName(_fromUtf8("outDir"))
        self.pushButton_Output = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_Output.setGeometry(QtCore.QRect(320, 30, 31, 21))
        self.pushButton_Output.setObjectName(_fromUtf8("pushButton_Output"))
        self.groupBox = QtGui.QGroupBox(OrthoMakerDialogBase)
        self.groupBox.setGeometry(QtCore.QRect(10, 380, 371, 111))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButtonDEM_2007 = QtGui.QRadioButton(self.groupBox)
        self.radioButtonDEM_2007.setGeometry(QtCore.QRect(20, 20, 82, 16))
        self.radioButtonDEM_2007.setObjectName(_fromUtf8("radioButtonDEM_2007"))
        self.radioButtonDEM_2015 = QtGui.QRadioButton(self.groupBox)
        self.radioButtonDEM_2015.setGeometry(QtCore.QRect(20, 50, 82, 17))
        self.radioButtonDEM_2015.setObjectName(_fromUtf8("radioButtonDEM_2015"))
        self.lineEditDEM = QtGui.QLineEdit(self.groupBox)
        self.lineEditDEM.setGeometry(QtCore.QRect(120, 80, 191, 20))
        self.lineEditDEM.setObjectName(_fromUtf8("lineEditDEM"))
        self.pushButton_DEM = QtGui.QPushButton(self.groupBox)
        self.pushButton_DEM.setGeometry(QtCore.QRect(320, 80, 31, 21))
        self.pushButton_DEM.setObjectName(_fromUtf8("pushButton_DEM"))
        self.radioButtonDEM_spec = QtGui.QRadioButton(self.groupBox)
        self.radioButtonDEM_spec.setGeometry(QtCore.QRect(20, 80, 91, 17))
        self.radioButtonDEM_spec.setObjectName(_fromUtf8("radioButtonDEM_spec"))
        self.label = QtGui.QLabel(OrthoMakerDialogBase)
        self.label.setGeometry(QtCore.QRect(20, 510, 46, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEditPixelSize = QtGui.QLineEdit(OrthoMakerDialogBase)
        self.lineEditPixelSize.setGeometry(QtCore.QRect(80, 510, 51, 20))
        self.lineEditPixelSize.setObjectName(_fromUtf8("lineEditPixelSize"))
        self.label_3 = QtGui.QLabel(OrthoMakerDialogBase)
        self.label_3.setGeometry(QtCore.QRect(20, 570, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(OrthoMakerDialogBase)
        self.label_2.setGeometry(QtCore.QRect(140, 510, 46, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_workdir = QtGui.QLineEdit(OrthoMakerDialogBase)
        self.lineEdit_workdir.setGeometry(QtCore.QRect(90, 570, 231, 20))
        self.lineEdit_workdir.setObjectName(_fromUtf8("lineEdit_workdir"))
        self.pushButton_workdir = QtGui.QPushButton(OrthoMakerDialogBase)
        self.pushButton_workdir.setGeometry(QtCore.QRect(330, 570, 31, 21))
        self.pushButton_workdir.setObjectName(_fromUtf8("pushButton_workdir"))

        self.retranslateUi(OrthoMakerDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), OrthoMakerDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), OrthoMakerDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(OrthoMakerDialogBase)

    def retranslateUi(self, OrthoMakerDialogBase):
        OrthoMakerDialogBase.setWindowTitle(_translate("OrthoMakerDialogBase", "Ortho Maker", None))
        self.checkBoxDelTiff.setText(_translate("OrthoMakerDialogBase", "Delete uncompressed tifs", None))
        self.groupBox_3.setTitle(_translate("OrthoMakerDialogBase", "Read raw photos from:", None))
        self.inDir.setToolTip(_translate("OrthoMakerDialogBase", "<html><head/><body><p><br/></p></body></html>", None))
        self.inDir.setWhatsThis(_translate("OrthoMakerDialogBase", "<html><head/><body><p>Select a single file. All files in dir will be used.</p></body></html>", None))
        self.pushButton_Input.setText(_translate("OrthoMakerDialogBase", "...", None))
        self.scanSub.setText(_translate("OrthoMakerDialogBase", "Scan sub dir", None))
        self.radioButton_fieldpath.setText(_translate("OrthoMakerDialogBase", "field value", None))
        self.radioButton_txtpath.setText(_translate("OrthoMakerDialogBase", "path", None))
        self.groupBox_2.setTitle(_translate("OrthoMakerDialogBase", "Shape file", None))
        self.inShapeA.setWhatsThis(_translate("OrthoMakerDialogBase", "<html><head/><body><p>Choose a PPC layer containing x,y,z,Omega, Phi, Cappa and Camera. Camera must be within the &quot;<span style=\" font-style:italic;\">Camera Calibration Database</span>&quot;</p></body></html>", None))
        self.useSelectedA.setText(_translate("OrthoMakerDialogBase", "Use only selected features", None))
        self.checkBox_bbox.setText(_translate("OrthoMakerDialogBase", "Use shape geometry as BBox", None))
        self.checkBoxSTR.setText(_translate("OrthoMakerDialogBase", "Create semi-true orthos", None))
        self.groupBox_4.setTitle(_translate("OrthoMakerDialogBase", "save orthos to:", None))
        self.pushButton_Output.setText(_translate("OrthoMakerDialogBase", "...", None))
        self.groupBox.setTitle(_translate("OrthoMakerDialogBase", "Elevation model", None))
        self.radioButtonDEM_2007.setText(_translate("OrthoMakerDialogBase", "DHM 2007", None))
        self.radioButtonDEM_2015.setText(_translate("OrthoMakerDialogBase", "DHM 2015", None))
        self.pushButton_DEM.setText(_translate("OrthoMakerDialogBase", "...", None))
        self.radioButtonDEM_spec.setText(_translate("OrthoMakerDialogBase", "Selected DHM:", None))
        self.label.setText(_translate("OrthoMakerDialogBase", "Pixel Size", None))
        self.label_3.setText(_translate("OrthoMakerDialogBase", "Working dir:", None))
        self.label_2.setText(_translate("OrthoMakerDialogBase", "meters", None))
        self.pushButton_workdir.setText(_translate("OrthoMakerDialogBase", "...", None))

