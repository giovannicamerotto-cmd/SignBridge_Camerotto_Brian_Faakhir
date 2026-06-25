# Directory
<pre>
│  README.md
│  app.py
│  keypoint_classification.ipynb
│  point_history_classification_EN.ipynb
│  point_history_classification.ipynb
│  requirements.txt
│  video tutorial.url
│  
├─.venv310
│  
├─model
│  ├─keypoint_classifier
│  │  │  keypoint.csv
│  │  │  keypoint_classifier.hdf5
│  │  │  keypoint_classifier.py
│  │  │  keypoint_classifier.tflite
│  │  └─ keypoint_classifier_label.csv
│  │          
│  └─point_history_classifier
│      │  point_history.csv
│      │  point_history_classifier.hdf5
│      │  point_history_classifier.py
│      │  point_history_classifier.tflite
│      └─ point_history_classifier_label.csv
│          
└─utils
    └─cvfpscalc.py
    └─tts.py
</pre>
### app.py
Main file running the whole programm

### keypoint_classification.ipynb
Model training script for hand sign recognition.

### keypoint_classification.ipynb
Model training script for hand sign recognition (English version).

### point_history_classification.ipynb
Model training script for finger gesture recognition.

### model/keypoint_classifier
This directory stores files related to hand sign recognition.<br>
The following files are stored.
* Training data(keypoint.csv)
* Trained model(keypoint_classifier.tflite)
* Label data(keypoint_classifier_label.csv)
* Inference module(keypoint_classifier.py)

### model/point_history_classifier
This directory stores files related to finger gesture recognition.<br>
The following files are stored.
* Training data(point_history.csv)
* Trained model(point_history_classifier.tflite)
* Label data(point_history_classifier_label.csv)
* Inference module(point_history_classifier.py)

### .venv310
Virtual environment to run python 3.10

### utils/cvfpscalc.py
This is a module for FPS measurement.

### utils/tts.py
This is a module for text-to-speech.

### requirements.txt
List of the main modules required to be installed.

### video tutorial.url
Youtube tutorial explaining the original project.



# How to run the Program
* on a terminal run ```& ".\.venv310\Scripts\python.exe" app.py```



# Training
Hand sign recognition and finger gesture recognition can add and change training data and retrain the model.


### Hand sign recognition training
#### 1.Learning data collection
Press "k" to enter the Logging Key Point mode
If you press "0" to "9", the current keypoints will be added to "[keypoint.csv](model/keypoint_classifier/keypoint.csv)" as a row, the data represented are:
- 1st column: Pressed number (used as class ID == relative hand sign)
- 2nd and subsequent columns: Keypoint coordinates in xy position
keypoints are the shown white circles on screen corresponding to the fingers' landmarks

#### 2.Model training
* on a terminal run ```jupyter notebook``` and wait untile the Jupyter page opens
* open "[keypoint_classification.ipynb](keypoint_classification.ipynb)" and run all cells
+ Parameters:
- number of training data classes: cell 3 > "NUM_CLASSES = 5"
- classes names: open "[keypoint_classifier_label.csv](model/keypoint_classifier/keypoint_classifier_label.csv)" > each line correspond to a class label start counting from ID = 0


### Finger gesture recognition training
#### 1.Learning data collection
Press "h" to enter the Logging Point History mode
If you press "0" to "9", the key points will be added to "[point_history.csv](model/point_history_classifier/point_history.csv)" as a row, the data represented are:
- 1st column: Pressed number (used as class ID == relative finger gesture)
- 2nd and subsequent columns: Keypoint coordinates in xy position
keypoints are the shown green circles on screen corresponding to the fingers' tips for each frame
+ Parameters:
- number of recording frames: open "[app.py](app.py)" > line 102 > "history_length = 8"

#### 2.Model training
* on a terminal run ```jupyter notebook``` and wait untile the Jupyter page opens
* open "[point_history_classification.ipynb](point_history_classification.ipynb) and run all cells
+ Parameters:
- number of training data classes: cell 3 > "NUM_CLASSES = 5"
- classes names: open "[point_history_classifier_label.csv](model/point_history_classifier/point_history_classifier_label.csv)" > each line correspond to a class label start counting from ID = 0
- time steps (must be equivalent to "history_length") > cell 4 > "TIME_STEPS = 8"
- architecture: cell 8 > "use_lstm = False". It is possible to switch between a fully connected neural network with and without Long Short-Term Memory. "CNN = False". It is possible also to use a Convolutional Neural Network.

# References and Sitografy
* [MediaPipe](https://mediapipe.dev/)
* [Original GitHub repostery](https://github.com/kinivi/hand-gesture-recognition-mediapipe)
* [Video Tutorial](https://youtu.be/7sywpZ7o2gg)
* [USA handsign language official site](https://www.handspeak.com/)
* [Final Project GitHub repostery](https://github.com/giovannicamerotto-cmd/SignBridge_Camerotto_Brian_Faakhir)
