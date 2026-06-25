## TODO
- Virtual Machine Raspberry
- save FPS and accuracy
- different Neural Network architecture


## How to run
video tutorial: https://youtu.be/7sywpZ7o2gg

run on terminal: & ".\.venv310\Scripts\python.exe" app.py
* ESC to close
+ Learning process:
    0. In app.py line 72: set max_num_hands = x to the number of hands between 1 and 2
    * for finger sign
    1. Go to model\keypoint_classifier\keypoint_classifier_label.csv
    2. Write the sign you want the model to learn (max = 10)
    3. Run the program with & ".\.venv310\Scripts\python.exe" app.py on terminal
    4. Once opened, press 'k' (it doesn't remove the already setted points, just add new ones)
    5. Do each position wirtten in the keypoint_classifier_label.csv lines and record many ground truth position by pressing the corresponding number on your keyboard (first position, press 0)
    6. To start the learning process go to keypoint_classification.ipynb
    7. In call 3: modify NUM_CLASSES = x to the number of sign you recorded (max = 10)
    8. on terminal write jupyter notebook
    9. Run All Cells
    * analog process for gestures using:
    1. \point_history_classifier instead of \keypoint_classifier
    4. 'h' instead of 'k'
        * the number of points recorded in the past for each gesture is in app.py line 103 history_length = x

# Work Pipeline
* Go to app.py and read the green text (comments), start from main().
* If you wish to reset the model records remove any value from model\keypoint_classifier\keypoint.csv, then repeat the Learning Process. (analogaly for \point_history_classifier)
* [Hand gestures from](https://www.handspeak.com/)

## changes
the program runs on python 3.10.11 so it can works with mediapipe and other modules that in new version would not.
.venv310 is a virtual environment for pyhton 3.10 to run.
Jupyter may not find modules installed in the virtual env, you must pip install all of them.

# Installed modules:
## - numpy
mathematical functions in python
## - jupyter
To open notebooks and run cells
## - ipykernel
Makes Jupyter work on Python 3.10
cmd example:
c:/Users/Acer/Documents/ComputerVision/Final-project/SignBridge-py/.venv310/Scripts/python.exe -m pip install ipykernel -U --force-reinstall
## - mediapipe
MediaPipe is an open-source, cross-platform framework developed by Google that allows developers to build machine learning pipelines for processing streaming media, such as video, audio, and sensor data.
+ What MediaPipe Does:
- Pose Estimation
- Tracks human body posture
- Hand Tracking
- Face Mesh
- Object Detection
- Image & Selfie Segmentation
## - opencv
Image and video analysis
## - sci-kit
To train machine learning models and analyze data
+ Features:
- Classification: Predicts discrete categories (e.g., email spam vs. legitimate).
    Techniques: Support Vector Machines (SVM), Random Forests, Logistic Regression, k-Nearest Neighbors (k-NN), and Naive Bayes
- Regression: Predicts continuous numerical values (e.g., house prices).
    Techniques: Linear Regression, Ridge/Lasso Regression, and Gradient Boosting
- Clustering: Groups unlabelled data based on shared traits (e.g., customer segmentation).
    Techniques: k-Means, DBSCAN, and Hierarchical Clustering
- Dimensionality Reduction: Simplifies large datasets by condensing features without losing critical data.
    Techniques: Principal Component Analysis (PCA) and t-SNE
## - tensorflow
Building and deploying machine learning and deep learning models
AI techniques:
- Deep Neural Networks (DNNs)
- Convolutional Neural Networks (CNNs)
- Recurrent Neural Networks (RNNs) & Transformers
- Reinforcement Learning
- Transfer Learning
## - matplotlib
To visualize data in Python
## - seaborn
To visualize data on matplotlib
## - pandas
To do data manipulation and analysis
## - tts
text-to-speech