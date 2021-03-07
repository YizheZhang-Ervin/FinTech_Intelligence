from flask import Flask, jsonify, render_template, request
from flask_restful import Api,Resource,reqparse
from flask_cors import CORS

from apis import audio,image,translator,stock,admin

# Initialize Flask
app = Flask(__name__,static_folder='',template_folder='',static_url_path="")

api = Api(app)

# Cross Domain
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Basic Route
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'GET':
#         return render_template('home.html')

# RESTful API Route
api.add_resource(audio.AudioAPI, '/api/audio/')
api.add_resource(image.ImageAPI, '/api/image/')
api.add_resource(translator.TranslateAPI, '/api/translate/')
api.add_resource(stock.StockAPI, '/api/stock/')
api.add_resource(admin.AdminAPI, '/api/admin/')

if __name__ == '__main__':
    app.run()