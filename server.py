from flask import Flask, render_template, request
# Import the emotion_detector function from the package 
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detectection():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output contains emotions and the scrores for each
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return f"For the given statement the system response is {response}"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)

