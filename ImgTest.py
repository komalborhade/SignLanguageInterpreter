# -*- coding: utf-8 -*-


from keras.models import model_from_json
from keras.preprocessing.image import ImageDataGenerator
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import threading
from matplotlib.pyplot import imshow
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras import backend as K



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
        return None
    
    
def visualize( img, layer_index=0, filter_index=0 ,all_filters=False ):
    
    act_fun = K.function([model.layers[0].input, K.learning_phase()], 
                                  [model.layers[layer_index].output,])
    
    #img = load_img('Dataset/test_set/punch/punch70.jpg',target_size=(200,200))
    x=img_to_array(img)
    img = cv2.cvtColor( x, cv2.COLOR_RGB2GRAY )
    img=img.reshape(img.shape+(1,))
    img=img.reshape((1,)+img.shape)
    img = act_fun([img,0])[0]
    
    if all_filters:
        fig=plt.figure(figsize=(7,7))
        filters = len(img[0,0,0,:])
        for i in range(filters):
                plot = fig.add_subplot(6, 6, i+1)
                plot.imshow(img[0,:,:,i],'gray')
                plt.xticks(np.array([]))
                plt.yticks(np.array([]))
        plt.tight_layout()
    else:
        img = np.rollaxis(img, 3, 1)
        img=img[0][filter_index]
        print(img.shape)
        imshow(img)


def update(histarray2):
    global histarray
    histarray=histarray2


#realtime:
def realtime(path):
      
    classes=["peace","punch","stop","thumbs_up"]
    
    
    frame=cv2.imread(path)
    frame=cv2.flip(frame,1)
    '''
    cv2.rectangle(frame,(300,200),(500,400),(0,255,0),1)
    cv2.putText(frame,"Place your hand in the green box.", (50,50), cv2.FONT_HERSHEY_PLAIN , 1, 255)
    cv2.putText(frame,"Press esc to exit.", (50,100), cv2.FONT_HERSHEY_PLAIN , 1, 255)
    
    cv2.imshow("preview", frame)
    frame=frame[200:400,300:500]
    #frame = cv2.resize(frame, (200,200))
    '''
    frame = cv2.cvtColor( frame, cv2.COLOR_RGB2GRAY)
    frame=frame.reshape((1,)+frame.shape)
    frame=frame.reshape(frame.shape+(1,))
    test_datagen = ImageDataGenerator(rescale=1./255)
    m=test_datagen.flow(frame,batch_size=1)
    y_pred=model.predict_generator(m,1)
    histarray2={'PEACE': y_pred[0][0], 'PUNCH': y_pred[0][1], 'STOP': y_pred[0][2], 'Thumbs Up': y_pred[0][3]}
    update(histarray2)
    print(classes[list(y_pred[0]).index(y_pred[0].max())])
    return classes[list(y_pred[0]).index(y_pred[0].max())]
       

#loading the model

model=load_model()

import socket                   # Import socket module
import random

  

port = 5000                     # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = "192.168.0.118"         #socket.gethostname()     # Get local machine name
#s.close()
s.bind((host, port))            # Bind to the port
s.listen(10)                     # Now wait for client connection.

print 'Server listening....'


if model is not None:
    while 1:
        conn, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr
        data = conn.recv(1024)
        if data!='':
            print('Server received', repr(data))
            conn.close()
            path="/var/www/html/uploads/1.jpg"
            sign=realtime(path)
            print "Sign=",sign
    
