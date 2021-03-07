# EZ Intelligence      
Antd + React + Flask RESTful + Echarts + Sqlite  
  
## Features   
- Home(Visualization) : Echarts(CandleStick) + DataDisplay     
- Login: Speech Recognition (Voice to word / Word to Voice)  + Face Recognition  
- Admin: shell command prompt  
- Tools : Translator  
  
## Infrastructure  
Front End: React + Antd + Axios + Echarts   
Back End: Flask RESTful + Sqlite + translate + speech_recognition + face_recognition + gtts + numpy + pandas  
Linux: ffmpeg  + gunicorn + gevent + python-dotenv  
  
## Run  
cd frontend  > npm install  
npm run start  
workon env_develop  or source ./activate  
cd backend > pip install -r requirements.txt  
  
## FrontEnd: React
### start project  
create-react-app xxApp  
  
### modules  
npm i react  
npm i react-dom  
npm i babel-standalone  
npm i prop-types  
npm i create-react-app -g  
npm i pubsub-js  
npm install antd  
npm install @ant-design/icons  
npm i json-server -g  
npm install axios  
npm install react-router-dom  
npm i redux  
  
### other commands  
npm start  
npm test  
npm run build  
npm run eject  
  
## BackEnd: Flask
### Libs  
pip install Flask  
pip install Flask_RESTful  
pip install Flask_Cors  
pip install numpy  
pip install pandas  
pip install cmake  
pip install dlib  
pip install SpeechRecognition  
pip install face_recognition  
pip install gTTS  
pip install gunicorn  
pip install gevent  
pip install python-dotenv  
  
### Backend Management  
python -m flask run  
  
### Dependency List  
Virtual Env libs: pip freeze > requirements.txt   
Dependency libs: pipreqs ./  
pip install -r requirements.txt   
  
### Deploy  
Gunicorn Common 1) gunicorn -w 4 -b 127.0.0.1:4000 myproject:app  
Gunicorn Factory 2) gunicorn "myproject:create_app()"  
uWSGI 1) uwsgi --http 127.0.0.1:5000 --module myproject:app  
twistd 1) twistd -n web --port tcp:8080 --wsgi myproject.app  
Gevent 1) python manage_gevent.py  
  
## Linux Shell  
apt-get/yum install ffmpeg  
  