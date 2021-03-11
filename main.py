from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time 
import home
import numpy as np
import cv2 
import getopt
import math

from video import create_capture
from common import clock, draw_str

from keras.models import model_from_json
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras import backend as K

class home(QtGui.QMainWindow, home.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.strt)
        self.pushButton_3.clicked.connect(self.ex)

    

    def strt(self):

        histarray={'PEACE':0, 'PUNCH':0, 'STOP': 0, 'Thumbs Up':0}
        
        
        def load_model():
            try:
                json_file = open('model.json', 'r')
                loaded_model_json = json_file.read()
                json_file.close()
                model = model_from_json(loaded_model_json)
                model.load_weights("weights.hdf5")
                print("Model successfully loaded from disk.")
                
                #compile again
                model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
                return model
            except Exception as e:
                print e
                print("""Model not found. Please train the CNN by running the script 
        cnn_train.py. Note that the training and test samples should be properly 
        set up in the dataset directory.""")
                return None
            
        def update(histarray2):
            global histarray
            histarray=histarray2
        
        
        #realtime:
        def realtime():
            #initialize preview
            cv2.namedWindow("preview")
            vc = cv2.VideoCapture(0)
            
            if vc.isOpened(): #get the first frame
                rval, frame = vc.read()
                
            else:
                rval = False
            
            classes=["peace","punch","stop","thumbs_up"]
            
            while rval:
                frame=cv2.flip(frame,1)
                cv2.rectangle(frame,(300,200),(500,400),(0,255,0),1)
                cv2.putText(frame,"Place your hand in the green box.", (50,50), cv2.FONT_HERSHEY_PLAIN , 1, 255)
                cv2.putText(frame,"Press esc to exit.", (50,100), cv2.FONT_HERSHEY_PLAIN , 1, 255)
                
                cv2.imshow("preview", frame)
                frame=frame[200:400,300:500]
                #frame = cv2.resize(frame, (200,200))
                frame = cv2.cvtColor( frame, cv2.COLOR_RGB2GRAY)
                frame=frame.reshape((1,)+frame.shape)
                frame=frame.reshape(frame.shape+(1,))
                test_datagen = ImageDataGenerator(rescale=1./255)
                m=test_datagen.flow(frame,batch_size=1)
                y_pred=model.predict_generator(m,1)
                histarray2={'PEACE': y_pred[0][0], 'PUNCH': y_pred[0][1], 'STOP': y_pred[0][2], 'Thumbs Up': y_pred[0][3]}
                update(histarray2)
                print(classes[list(y_pred[0]).index(y_pred[0].max())])
                rval, frame = vc.read()
                key = cv2.waitKey(20)
                if key == 27: # exit on ESC
                    break
            cv2.destroyWindow("preview")
            vc=None
            
               
        model=load_model()
        realtime()
               
    def ex(self):
        sys.exit()
        

def main():
    app = QtGui.QApplication(sys.argv)  
    form = home()                 
    form.show()                         
    app.exec_()                         


if __name__ == '__main__':              
    main()                             
