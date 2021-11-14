# Imports necessary modules
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtWidgets
import tensorflow as tf
import ctypes
import cv2
import sys
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Cataract Detector by Richard for WAICY 2021")
        MainWindow.resize(774, 423)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(247, 50, 271, 41))
        self.textBrowser.setObjectName("textBrowser")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 120, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(detect)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 180, 141, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(instructions)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 240, 141, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(exit)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Cataract Detector by Richard for WAICY 2021", "Cataract Detector by Richard for WAICY 2021"))
        self.textBrowser.setHtml(_translate("Cataract Detector by Richard for WAICY 2021", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">CatAI</span></p></body></html>"))
        self.pushButton.setText(_translate("Cataract Detector by Richard for WAICY 2021", "Detect"))
        self.pushButton_2.setText(_translate("Cataract Detector by Richard for WAICY 2021", "Instructions"))
        self.pushButton_3.setText(_translate("Cataract Detector by Richard for WAICY 2021", "Exit"))
        self.actionExit.setText(_translate("Cataract Detector by Richard for WAICY 2021", "Exit"))

def detect():
    # Gets file path
    filename = QFileDialog.getOpenFileName()
    image_path = filename[0]

    if image_path != "":
        # Read in the image_data
        image_data = tf.io.gfile.GFile(image_path, 'rb').read()

        # Loads label file, strips off carriage return
        label_lines = [line.rstrip() for line in tf.io.gfile.GFile("retrained_labels.txt")]

        # Unpersists graph from file
        with tf.io.gfile.GFile("retrained_graph.pb", 'rb') as f:
            graph_def = tf.compat.v1.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name='')

        with tf.compat.v1.Session() as sess:
            # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
            
            predictions = sess.run(softmax_tensor, \
                    {'DecodeJpeg/contents:0': image_data})

            # Repeats for amount of labels
            for i in range(len(label_lines)):
                # Check if the maximum value is equal the value
                if max((predictions)[0]) == predictions[0][i]:
                    label = label_lines[i]
                    score = predictions[0][i]
                    # Round and turn into percentage
                    final_score = round(score*100)

            # Using cv2.imread() method
            img = cv2.imread(image_path)

            if img.shape[1] < 290:
                w = 290
            else:
                w = img.shape[1]

            # Resize image
            img = cv2.resize(img, (w, img.shape[0]), interpolation = cv2.INTER_AREA)

            # Puts name and percentage 
            cv2.putText(img, f'{label}: {final_score}%', (2, 25), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)

            # Displaying the image
            cv2.imshow('Image With Diagnosis', img)

def instructions():
    # Opens instructions.html
    os.system("explorer.exe instructions.html")

def exit():
    # Creates a yes or no messagebox
    result = ctypes.windll.user32.MessageBoxW(0, "Are you sure?", "Exit", 4)
    if result == 6:
        sys.exit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())