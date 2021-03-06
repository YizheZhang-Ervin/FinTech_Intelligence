from flask_restful import Resource,reqparse
from flask import jsonify
import speech_recognition as sr
import os
import base64

# parse parameters
parser = reqparse.RequestParser()
parser.add_argument('key', type=str)

# 接收前端音频
class AudioAPI(Resource):
    # http://127.0.0.1:5000/api/audio/
    # 传{"key":"值"}
    def post(self):
        try:
            args = parser.parse_args()
            key = eval(args['key'])
            key = base64.b64decode(key[35:])
            result = audioRecognition(key)
            jsonObj = {"result":result}
            return jsonify(jsonObj)
        except Exception:
            return jsonify({"error":"error"})

def audioRecognition(audio):
    webm_path = "Audio/audio.webm"
    wav_path = "Audio/audio.wav"
    sampling_rate = 16000
    channel = 1
    # 二进制声音写入webm文件
    with open(webm_path,"wb") as f:
        f.write(audio)
    # webm 转 wav
    if os.path.exists(wav_path):
        os.remove(wav_path)
    command = "ffmpeg -loglevel quiet -i {} -ac {} -ar {} {}".format(webm_path, channel, sampling_rate, wav_path)
    os.system(command)
    
    # 语音识别
    r = sr.Recognizer()
    audio2 = sr.AudioFile(wav_path)
    with audio2 as source:
        audio3 = r.record(source)
    recognizeResult = r.recognize_google(audio3, language='zh-CN', show_all=True)
    text = recognizeResult["alternative"][0]["transcript"]
    return text