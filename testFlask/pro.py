from flask import Flask,request
import tensorflow as tf
import base64
import cv2
import numpy as np



new_model = tf.keras.models.load_model("c:/Users/pc/graduation_project/API/ImageClassification/testFlask/imageclassifier.h5")


app = Flask(__name__)



@app.route('/api',methods = ['Put'] )
def index():
       inputchar = request.get_data()
       imgdata = base64.b64decode(inputchar)
       filename = 'somthing.jpg'  
       with open(filename, 'wb') as f:
        f.write(imgdata)

       img = cv2.imread('c:/Users/pc/graduation_project/API/ImageClassification/testflask/somthing.jpg')
       resize = tf.image.resize(img, (256,256))
       yhat = new_model.predict(np.expand_dims(resize/255, 0))

       result = ""
       if yhat > 0.5: 
              result= 'Predicted class is Sad'
       else:
              result= 'Predicted class is happy'

    


       return result



if __name__ == "__main__":
    app.run(debug=True)





