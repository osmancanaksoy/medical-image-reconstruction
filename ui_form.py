# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(978, 707)
        MainWindow.setMinimumSize(QSize(978, 707))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.imageLabel = QLabel(self.groupBox_3)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setMaximumSize(QSize(453, 277))

        self.gridLayout_6.addWidget(self.imageLabel, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.reconsLayout = QVBoxLayout()
        self.reconsLayout.setObjectName(u"reconsLayout")

        self.gridLayout_5.addLayout(self.reconsLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 1, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.sinogramLayout = QVBoxLayout()
        self.sinogramLayout.setObjectName(u"sinogramLayout")

        self.gridLayout_3.addLayout(self.sinogramLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayoutWidget = QWidget(self.groupBox)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 30, 471, 281))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.projectionLabel = QLabel(self.gridLayoutWidget)
        self.projectionLabel.setObjectName(u"projectionLabel")

        self.gridLayout_2.addWidget(self.projectionLabel, 3, 0, 1, 1)

        self.filterComboBox = QComboBox(self.gridLayoutWidget)
        self.filterComboBox.addItem("")
        self.filterComboBox.addItem("")
        self.filterComboBox.setObjectName(u"filterComboBox")

        self.gridLayout_2.addWidget(self.filterComboBox, 2, 2, 1, 2)

        self.filterLabel = QLabel(self.gridLayoutWidget)
        self.filterLabel.setObjectName(u"filterLabel")

        self.gridLayout_2.addWidget(self.filterLabel, 2, 0, 1, 1)

        self.projectionValue = QLabel(self.gridLayoutWidget)
        self.projectionValue.setObjectName(u"projectionValue")

        self.gridLayout_2.addWidget(self.projectionValue, 3, 2, 1, 1)

        self.calculateButton = QPushButton(self.gridLayoutWidget)
        self.calculateButton.setObjectName(u"calculateButton")

        self.gridLayout_2.addWidget(self.calculateButton, 4, 2, 1, 1)

        self.methodComboBox = QComboBox(self.gridLayoutWidget)
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.methodComboBox.setObjectName(u"methodComboBox")

        self.gridLayout_2.addWidget(self.methodComboBox, 1, 2, 1, 1)

        self.clearButton = QPushButton(self.gridLayoutWidget)
        self.clearButton.setObjectName(u"clearButton")

        self.gridLayout_2.addWidget(self.clearButton, 4, 3, 1, 1)

        self.methodLabel = QLabel(self.gridLayoutWidget)
        self.methodLabel.setObjectName(u"methodLabel")

        self.gridLayout_2.addWidget(self.methodLabel, 1, 0, 1, 1)

        self.maxLabel = QLabel(self.gridLayoutWidget)
        self.maxLabel.setObjectName(u"maxLabel")

        self.gridLayout_2.addWidget(self.maxLabel, 0, 0, 1, 1)

        self.animationButton = QPushButton(self.gridLayoutWidget)
        self.animationButton.setObjectName(u"animationButton")

        self.gridLayout_2.addWidget(self.animationButton, 4, 1, 1, 1)

        self.angleValue = QLineEdit(self.gridLayoutWidget)
        self.angleValue.setObjectName(u"angleValue")

        self.gridLayout_2.addWidget(self.angleValue, 0, 2, 1, 1)

        self.loadButton = QPushButton(self.gridLayoutWidget)
        self.loadButton.setObjectName(u"loadButton")

        self.gridLayout_2.addWidget(self.loadButton, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 978, 17))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Medical Image Reconstruction", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Original Image", None))
        self.imageLabel.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Reconstruction", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Sinogram", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Medical Image Reconstruction", None))
        self.projectionLabel.setText(QCoreApplication.translate("MainWindow", u"Number of Projections:", None))
        self.filterComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Filtered Back Projection", None))
        self.filterComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"SART", None))

        self.filterLabel.setText(QCoreApplication.translate("MainWindow", u"Filter Type:", None))
        self.projectionValue.setText("")
        self.calculateButton.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.methodComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"ramp", None))
        self.methodComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"shepp-logan", None))
        self.methodComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"cosine", None))
        self.methodComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"hamming", None))
        self.methodComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"hann", None))

        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.methodLabel.setText(QCoreApplication.translate("MainWindow", u"Reconstruction Method:", None))
        self.maxLabel.setText(QCoreApplication.translate("MainWindow", u"Maximum Angle:", None))
        self.animationButton.setText(QCoreApplication.translate("MainWindow", u"Animation", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
    # retranslateUi

