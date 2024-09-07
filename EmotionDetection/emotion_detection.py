''' Perform emotion detection using IBM Watson embedded API
'''
import json
import requests

def emotion_detector(text_to_analyze):
    ''' This code receives the text to analyse it then passes it to the
        api and return a formated dictionary containing the label and the score
    '''
    # setup the endpoint and input data
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data =  { "raw_document": { "text": text_to_analyze } }
    # do the call to the api    
    response = requests.post(url, json = data, headers=header)
    # setup the result 
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    result = {}
    high = 0.0
    dominant_emotion = ''   
    for emotion, score in emotions.items():
        result[emotion] = score
        if float(score) > high: 
            high = score
            dominant_emotion = emotion 
    result['dominant_emotion'] = dominant_emotion
    return result;   
 