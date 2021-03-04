from flask import Flask, jsonify, render_template, request
from flask_restful import Api,Resource,reqparse
from flask_cors import CORS
import speech_recognition as sr
import face_recognition as fr
import base64
import os
from imp import reload

# Initialize Flask
app = Flask(__name__,static_folder='frontend',template_folder='frontend',static_url_path="")
api = Api(app)

# Cross Domain
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# parse parameters
parser = reqparse.RequestParser()
parser.add_argument('key', type=str)

# Basic Route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('home.html')

# RESTful API Route
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
        try:
            args = parser.parse_args()
            key = eval(args['key'])
            key = base64.b64decode(key[22:])
            result = faceRecognition(key)
            jsonObj = {"result":result}
            return jsonify(jsonObj)
        except Exception:
            return jsonify({"error":"error"})
api.add_resource(ImageAPI, '/api/image/')

def faceRecognition(face):
    # 二进制图片写入jpg文件
    img_path = "Image/test.jpg"
    with open(img_path,"wb") as f:
        f.write(face)
    
    trainImg = fr.load_image_file("Image/train.jpg")
    testImg = fr.load_image_file("Image/test.jpg")

    trainImg_encoding = fr.face_encodings(trainImg)[0]
    testImg_encoding = fr.face_encodings(testImg)[0]

    results = fr.compare_faces([trainImg_encoding], testImg_encoding )
    labels = ["You"]

    return "".join([labels[i] for i in range(0, len(results)) if results[i] == True])

if __name__ == '__main__':
    app.run(debug=True)