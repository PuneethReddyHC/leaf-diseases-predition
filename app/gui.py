import time

from PyQt5.QtWidgets import *
from .progress import long_operation
from .utils import resource_path
from .ui.appgui import Ui_MainWindow
from PyQt5.QtGui  import *
from PyQt5.QtCore  import *
from PyQt5 import uic
import json
global ImageFile
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.browse.pressed.connect(self.Analyze)

        self.radioButton_Tensorflow = QRadioButton(self.frame)
        self.radioButton_Tensorflow.setGeometry(QRect(320, 145, 95, 20))
        self.tensorlabel = QLabel(self.frame)
        self.tensorlabel.setText("TensorFlow")
        self.tensorlabel.setGeometry(QRect(340, 145, 95, 20))
        # adding signal and slot  
        self.radioButton_Tensorflow.toggled.connect(self.tensorSelected) 
         
        # Radio button for female 

        self.radioButton_Keras = QRadioButton(self.frame) 
        self.radioButton_Keras.setGeometry(QRect(440, 145, 95, 20))
        self.keraselabel = QLabel(self.frame) 
        self.keraselabel.setText("Keras")
        self.keraselabel.setGeometry(QRect(460, 145, 95, 20))
        # adding signal and slot 
        self.radioButton_Keras.toggled.connect(self.kerasSelected)

        self.radioButton_segment = QRadioButton(self.frame) 
        self.radioButton_segment.setGeometry(QRect(540, 145, 95, 20))
        self.segmentlabel = QLabel(self.frame) 
        self.segmentlabel.setText("Segment")
        self.segmentlabel.setGeometry(QRect(560, 145, 95, 20))
        # adding signal and slot 
        self.radioButton_segment.toggled.connect(self.segmentSelected) 

        self.radioButton_torch = QRadioButton(self.frame) 
        self.radioButton_torch.setGeometry(QRect(630, 145, 95, 20))
        self.torchlabel = QLabel(self.frame) 
        self.torchlabel.setText("PyTorch")
        self.torchlabel.setGeometry(QRect(650, 145, 95, 20))
        # adding signal and slot 
        self.radioButton_torch.toggled.connect(self.torchSelected) 
        
        self.radiolabels = QLabel(self.frame)
        self.radiolabels.setGeometry(QRect(330, 170, 300, 20))
        self.imagefile  = ""
        self.selectedModel = ""
        self.show()
    
    def tensorSelected(self, selected): 
        if selected:
            text = '<h3 style=\"color:blue\">You are selected to Analyze using TensorFlow Model</h3>'
            self.radiolabels.setText(text)
            self.selectedModel = "tensor"
              
    def kerasSelected(self, selected): 
        if selected:
            text = '<h3 style=\"color:green\">You are selected to Analyze using keras Model</h3>'
            self.radiolabels.setText(text)
            self.selectedModel = "keras"

    def segmentSelected(self, selected): 
        if selected:
            text = '<h3 style=\"color:red\">You are selected to display Segmented images</h3>'
            self.radiolabels.setText(text)
            self.selectedModel = "segment"
    
    def torchSelected(self, selected): 
        if selected:
            text = '<h3 style=\"color:green\">You are selected to Analyze using Pytorch Model</h3>'
            self.radiolabels.setText(text)
            self.selectedModel = "pytorch"

    def execfile(self, filepath, globals={}, locals=None):
        
        with open(filepath, 'rb') as file:
            exec(compile(file.read(), filepath, 'exec'), globals, locals)

    def Analyze(self):
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        ImageFile , something = QFileDialog.getOpenFileName(self,"Select Image To Process", "","All Files (*);;Image Files(*.jpg *.gif)"
                                                ,options=options)
        if ImageFile == "":
            text = '<h3 style=\"color:red\">No Image Selected</h3>'
            self.radiolabels.setText(text)
        else:
            self.imagefile = ImageFile
            if self.selectedModel == 'tensor':
                self.hdf5Model()
                print('#self.hdf5Model')
            elif self.selectedModel == 'segment':
                self.segment()
                print('#self.segment')
            elif self.selectedModel == 'keras':
                self.pklModel()
                print('#self.pklModel')
            elif self.selectedModel == 'pytorch':
                self.ckptModel()
                print('#self.ckptModel')
            else:
                text = '<h3 style=\"color:red\">Please Select any one Model</h3>'
                self.radiolabels.setText(text)
            
            
    @long_operation("Calculation")
    def segmentedProcessing(self, sleep):
        print("Start")
        self.execfile("./app/main.py",{'ImageFile': self.imagefile})
        time.sleep(sleep)
        print("End")

    @pyqtSlot()
    def segment(self):
        self.segmentedProcessing(5)
        self.statusBar().showMessage("Switched to window 1")
        self.cams = Window2() 
        self.cams.show()
        self.close()

    def button_press(self):
        text = self.calculation(3)
        QMessageBox.information(self, "Message Box", text)

    @long_operation("Calculation")
    def calculation(self, sleep):
        print("Start")
        with open(resource_path('example.txt')) as file:
            text = file.read()
        time.sleep(sleep)
        print("End")
        return text

    @long_operation("Calculation")
    def hdf5Processing(self, sleep):
        print("Start")
        from hdf5.main import index
        import urllib.parse
        filesrc=urllib.parse.quote(self.imagefile)
        

        with open('remedies.json', 'r') as f:
            remedie = json.load(f)

        disease = index(self.imagefile)

        text = "<center>" \
           "<img src="+ filesrc +" height=300 width=350>" \
            "<h1>"+ disease +"</h1>" \
           "&#8291;" \
           "</center>" \
            "<h1>Treatment</h1>" \
           "<p>"+ remedie[disease]+ "<br/>" \
           " "+ disease +"</p>"
        time.sleep(sleep)
        print(index(self.imagefile))
        return text

    def hdf5Model(self):
        text = self.hdf5Processing(4)
        QMessageBox.about(self, "Disease Prediction", text)

    

    @long_operation("Calculation")
    def pklProcessing(self, sleep):
        print("Start")
        from pkl.main import predict_plant_disease
        import urllib.parse
        filesrc=urllib.parse.quote(self.imagefile)

        with open('remedies.json', 'r') as f:
            remedie = json.load(f)

        disease = str(predict_plant_disease(self.imagefile))
        text = "<center>" \
           "<img src="+ filesrc +" height=300 width=350>" \
            "<h1>"+ disease +"</h1>" \
           "&#8291;" \
           "</center>" \
           "<h1>Treatment</h1>" \
           "<p>"+ remedie[disease]+"<br/>" \
           " "+ disease +"</p>"
        time.sleep(sleep)
        print('End')
        return text

    def pklModel(self):

        text = self.pklProcessing(4)
        QMessageBox.about(self, "Disease Prediction", text)

    def ckptModel(self):

        text = self.ckptprocessing()
        QMessageBox.about(self, "Disease Prediction", text)

    
    def ckptModel(self):
        print("Start")
        from ckpt.main import load_checkpoint
        from ckpt.predict import predict
        from ckpt.predict import loaded_model
        with open('categories.json', 'r') as f:
            cat_to_name = json.load(f)
        p, c = predict(self.imagefile, loaded_model)
        self.view_classify(self.imagefile, p, c, cat_to_name)
        print("End")


    def view_classify(self, img, probabilities, classes, mapper):
        import matplotlib.pyplot as plt
        import numpy as np
        from PIL import Image
        img = Image.open(img)
        fig, (ax1, ax2) = plt.subplots(figsize=(10,10), ncols=1, nrows=2)
        plt.subplots_adjust(top=0.995,bottom=0.127,left=0.402,right=0.964,hspace=0.051,wspace=0.21)
        ax1.imshow(img)
        ax1.axis('off')
        y_pos = np.arange(len(probabilities))
        ax2.barh(y_pos, probabilities)
        ax2.set_yticks(y_pos)
        ax2.set_yticklabels([mapper[x] for x in classes])
        ax2.invert_yaxis()
        plt.show()

    def resnetModel(self):
        from resnet34.main import analyze
        print ("\n*********************\nresnet34 : " + analyze(ImageFile) + "\n*********************")


import os
class Window2(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title = 'Segmented Images Using OpenCV'
        self.left = 10
        self.top = 50
        self.width = 500
        self.height = 300
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        highlight_dir = 'C:/Users/punehemukeeru/Documents/1Aplantdiseases/pyqt-gui-template/tests'

        self.scrollArea = QScrollArea(widgetResizable=True)
        self.setCentralWidget(self.scrollArea)
        content_widget = QWidget()
        self.scrollArea.setWidget(content_widget)
        self._lay = QVBoxLayout(content_widget)

        self.files_it = iter([os.path.join(highlight_dir, file) for file in os.listdir(highlight_dir)])

        self._timer = QTimer(self, interval=1)
        
        self._timer.timeout.connect(self.on_timeout)
        self._timer.start()

    def on_timeout(self):
        try:
            from pathlib import Path
            file = next(self.files_it)
            filename=Path(file).stem
            pixmap = QPixmap(file)
            pixmap = pixmap.scaled(250, 250)
            
            self.add_pixmap(pixmap,filename,file)
            
        except StopIteration:
            self._timer.stop()
            
    def add_pixmap(self, pixmap,fname,file):
        if not pixmap.isNull():
            table_data ="<br><tr>"\
                "<td ><h1 style=\"color:green;margin:30%;\">"+ fname +"</h1></td>"\
                "<td><div style=\"margin-left:100px;margin-right:50px;\" ><img src="+ file +" height=300 width=350></div></td>"\
                "<td><p> this is about this segmented Image</p></td>"\
            "</tr><br>"

            label_data = QLabel()
            label_data.setText(table_data)
            self._lay.addWidget(label_data)
            