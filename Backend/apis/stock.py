from flask_restful import Resource,reqparse
from flask import jsonify, request
import pandas as pd
import os
import numpy as np
import datetime

# parse parameters
parser = reqparse.RequestParser()
parser.add_argument('stockid', type=str)
parser.add_argument('start', type=str)
parser.add_argument('end', type=str)

# 接收前端音频
class StockAPI(Resource):
    # http://127.0.0.1:5000/api/stock/?stockid=值&start=值&end=值
    # 传{"key":"值"}
    def get(self):
        try:
            stockid = request.args.get("stockid","")
            start = request.args.get("start","")
            start = datetime.datetime.strptime(start,"%Y/%m/%d")
            end = request.args.get("end","")
            end = datetime.datetime.strptime(end,"%Y/%m/%d")
            data = searchFromDB(stockid,start,end)
            return jsonify(data)
        except Exception:
            return jsonify({"error":"error"})

def searchFromDB(stockid,start,end):
    dir_name = os.path.dirname(os.path.dirname(__file__))
    filePath = os.path.join(dir_name,"Data","goldFutures.xlsx")
    data = pd.read_excel(filePath)
    data2 = data.loc[(data["Date"]>start) & (data["Date"]<end),["Date","Open","Close","Low","High","Volume"]].dropna()
    data2["Date"] = data2["Date"].astype(str)
    data3 = data2.values.tolist()
    return data3