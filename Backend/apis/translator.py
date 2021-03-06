from flask_restful import Resource,reqparse
from flask import jsonify,request
from translate import Translator

parser = reqparse.RequestParser()
parser.add_argument('sentence', type=str)
parser.add_argument('fromlang', type=str)
parser.add_argument('tolang', type=str)

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