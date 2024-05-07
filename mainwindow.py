# This Python file uses the following encoding: utf-8
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from skimage.transform import radon, iradon,rescale
from skimage.color import rgb2gray
from skimage import img_as_float
from skimage import io
from MI import MI

from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QDialog, QMessageBox
from PySide6.QtCore import QUrl, QDir
from qt_material import apply_stylesheet

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusbar.showMessage("Developed by Osman Can AKSOY")

        self.imagePath = ""

        self.ui.loadButton.clicked.connect(self.loadButtonClicked)
        self.ui.animationButton.clicked.connect(self.animationButtonClicked)
        self.ui.calculateButton.clicked.connect(self.calculateButtonClicked)
        self.ui.clearButton.clicked.connect(self.clearButtonClicked)


    def clearInterface(self):
        self.ui.imageLabel.clear()

        self.ui.projectionValue.clear()

        clearSinogram = self.ui.sinogramLayout.takeAt(0).widget()
        clearSinogram.deleteLater()

        clearRecons = self.ui.reconsLayout.takeAt(0).widget()
        clearRecons.deleteLater()



    def loadButtonClicked(self):
        dialog = QFileDialog(self)
        fname = QFileDialog.getOpenFileName(self, self.tr('Open file'),
                QDir.currentPath() + '/images', "Image files (*.jpg *.png *.bmp)")

        self.imagePath = fname[0]

        self.image = io.imread(str(self.imagePath))

        pix = QPixmap(self.imagePath)
        self.ui.imageLabel.setScaledContents(True)
        self.ui.imageLabel.setPixmap(pix)

    def animationButtonClicked(self):

        img = self.image
        theta = int(self.ui.angleValue.text())
        filterType = self.ui.methodComboBox.currentText()

        fig1, ax1 = plt.subplots(1,1, figsize=(3, 3))
        self.canvas = FigureCanvas(fig1)
        self.ui.sinogramLayout.addWidget(self.canvas)

        fig2, ax2 = plt.subplots(1,1, figsize=(3, 3))
        self.canvas2 = FigureCanvas(fig2)
        self.ui.reconsLayout.addWidget(self.canvas2)


        for thetaStep in range(10, theta+1, 10):
            self.medicalImage = MI(img, thetaStep, filterType)
            __, __, numProjection = self.medicalImage.processImage()
            self.ui.projectionValue.setText(str(numProjection) + " projections")

            sinogram = self.medicalImage.radonTransform()

            ax1.imshow(sinogram, cmap=plt.cm.Greys_r)
            self.canvas.draw()
            self.canvas.flush_events()

            reconstruction = self.medicalImage.filteredBackProjection()
            if(filterType == "SART"):
                reconstruction = self.medicalImage.sart()

            ax2.imshow(reconstruction, cmap=plt.cm.Greys_r)
            self.canvas2.draw()
            self.canvas2.flush_events()

    def calculateButtonClicked(self):

        if(self.ui.angleValue.text() == ""):
            button = QMessageBox.warning(self, "Warning", "Please specify the max angle!")


        img = self.image
        theta = int(self.ui.angleValue.text())
        filterType = self.ui.methodComboBox.currentText()

        self.medicalImage = MI(img, theta, filterType)

        sinogram = self.medicalImage.radonTransform()

        reconstruction = self.medicalImage.filteredBackProjection()
        if(filterType == "SART"):
            reconstruction = self.medicalImage.sart()

        __, __, numProjection = self.medicalImage.processImage()
        self.ui.projectionValue.setText(str(numProjection) + " projections")

        fig1, ax1 = plt.subplots(1,1, figsize=(3, 3))

        canvas = FigureCanvas(fig1)
        ax1.imshow(sinogram, cmap=plt.cm.Greys_r)

        self.ui.sinogramLayout.addWidget(canvas)

        fig2, ax2 = plt.subplots(1,1, figsize=(3, 3))
        canvas2 = FigureCanvas(fig2)
        ax2.imshow(reconstruction, cmap=plt.cm.Greys_r)

        self.ui.reconsLayout.addWidget(canvas2)

        #qimage = QImage(sinogram, sinogram.shape[1], sinogram.shape[0], sinogram.shape[1], QImage.Format_Grayscale8)
        qimage = QImage("sinogram.png")
        pixmap = QPixmap(qimage)

    def clearButtonClicked(self):
        self.clearInterface()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
