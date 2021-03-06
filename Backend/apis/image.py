from flask_restful import Resource,reqparse
from flask import jsonify
import face_recognition as fr
from gtts import gTTS
import numpy as np
import base64
import sys 
from Image import faceData
sys.path.append("..") 

# parse parameters
parser = reqparse.RequestParser()
parser.add_argument('key', type=str)

# 接收前端照片
class ImageAPI(Resource):
    # http://127.0.0.1:5000/api/image/
    # 传{"key":"值"}
    def post(self):
        try:
            args = parser.parse_args()
            key = eval(args['key'])
            key = base64.b64decode(key[22:])
            result,aiVoice = faceRecognition(key)
            jsonObj = {"result":result,"aiVoice":aiVoice}
            return jsonify(jsonObj)
        except Exception:
            return jsonify({"error":"error"})

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
        return "NOBODY",0

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

    return people,str(base64.b64encode(aiVoice))[2:-1]
