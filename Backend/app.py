from flask import Flask, jsonify, render_template, request
from flask_restful import Api,Resource,reqparse
from flask_cors import CORS
import speech_recognition as sr
import face_recognition as fr
import base64
import os
from imp import reload
import numpy as np
from Image import faceData
from gtts import gTTS
from translate import Translator

# Initialize Flask
app = Flask(__name__,static_folder='',template_folder='',static_url_path="")

api = Api(app)

# Cross Domain
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# parse parameters
parser = reqparse.RequestParser()
parser.add_argument('key', type=str)
parser.add_argument('sentence', type=str)
parser.add_argument('fromlang', type=str)
parser.add_argument('tolang', type=str)

# Basic Route
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'GET':
#         return render_template('home.html')

# RESTful API Route
# 接收前端音频
class AudioAPI(Resource):
    # http://127.0.0.1:5000/api/audio/
    # 传{"key":"值"}
    def post(self):
        # try:
        args = parser.parse_args()
        key = eval(args['key'])
        key = base64.b64decode(key[35:])
        result = audioRecognition(key)
        jsonObj = {"result":result}
        return jsonify(jsonObj)
        # except Exception:
        #     return jsonify({"error":"error"})
api.add_resource(AudioAPI, '/api/audio/')

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

# 接收前端照片
class ImageAPI(Resource):
    # http://127.0.0.1:5000/api/image/
    # 传{"key":"值"}
    def post(self):
        # try:
        args = parser.parse_args()
        key = eval(args['key'])
        key = base64.b64decode(key[22:])
        result,mostLikely,aiVoice = faceRecognition(key)
        jsonObj = {"result":result,"likely":mostLikely,"aiVoice":aiVoice}
        return jsonify(jsonObj)
        # except Exception:
        #     return jsonify({"error":"error"})
api.add_resource(ImageAPI, '/api/image/')

def faceRecognition(face):
    # 二进制图片写入jpg文件
    img_path = "Image/test.jpg"

    with open(img_path,"wb") as f:
        f.write(face)

    # trainImg = fr.load_image_file("Image/train.jpg")
    testImg = fr.load_image_file("Image/test.jpg")

    # trainImg_encoding = fr.face_encodings(trainImg)[0]
    ZYZ = np.array(faceData.ZYZ)
    HSJ = np.array(faceData.HSJ)
    SXK = np.array(faceData.SXK)
    CLJ = np.array(faceData.CLJ)
    LQJ = np.array(faceData.LQJ)
    WZQ = np.array(faceData.WZQ)

    testImg_encoding = fr.face_encodings(testImg)
    if testImg_encoding:
        testImg_encoding = testImg_encoding[0]
    else:
        return "NOBODY",0,0

    labels = ["张以哲","何仕杰","石烜逵","陈灵健","陆其杰","王祉祈"]

    # results = fr.compare_faces([ZYZ,HSJ,SXK,CLJ,LQJ,WZQ],testImg_encoding,tolerance=0.39)
    # print(results)
    # for i in range(0,len(results)):
    #     if results[i] == True:
    #         return labels[i]
    # return "NOBODY"

    results = fr.face_distance([ZYZ,HSJ,SXK,CLJ,LQJ,WZQ],testImg_encoding)
    mostNearly = min(results)
    people = labels[list(results).index(mostNearly)]

    likely = str((1- mostNearly)*100)[:5]+"%"
    
    sentence = f"欢迎回来{people},相似程度:百分之{likely[:5]}"
    tts = gTTS(text=sentence,lang="zh")
    tts.save("Audio/sentence.mp3")
    
    # 读取音频，转为二进制传到前端
    aiVoice = ""
    with open("Audio/sentence.mp3","rb") as f:
        aiVoice = f.read()

    return people,likely,str(base64.b64encode(aiVoice))[2:-1]

# 翻译
class TranslateAPI(Resource):
    # http://127.0.0.1:5000/api/translate/?pkg=值
    def get(self):
        try:
            sentence = request.args.get("sentence","")
            fromlang = request.args.get("fromlang","")
            tolang = request.args.get("tolang","")

            translator_ec = Translator(from_lang=fromlang, to_lang=tolang)
            translatedSentence = translator_ec.translate(sentence)
            jsonObj = {"result":translatedSentence}
            return jsonify(jsonObj)
        except Exception:
            return jsonify({"error":"error"})

api.add_resource(TranslateAPI, '/api/translate/')

if __name__ == '__main__':
    app.run()