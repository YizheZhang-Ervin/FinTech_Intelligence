import React from "react";
import axios from "axios";
import { Button } from 'antd';
import { AudioOutlined,AudioMutedOutlined } from '@ant-design/icons';

class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            voiceIcon : <AudioMutedOutlined style={{ fontSize: "2em", color: "white" }}/>
        };
    }

    componentDidMount() {
        this.recordAudio();
        this.getCamera();
        this.setState({
            "verificationTimer":setInterval(() => {
                let takephoto = document.getElementById("takephoto");
                takephoto.click();
            }, 2000)
        })
    }
    componentWillUnmount(){
        clearInterval(this.state.verificationTimer);
    }
    
    // 设置state值
    setStateValue(key,val){
        this.setState({
            [key]:val
        })
    }
    // 传audio给后台,接收字符串
    postAudio(params) {
        let urlAudio = `http://127.0.0.1:5000/api/audio/`;
        // let urlAudio = `/api/audio/`;
        axios.post(urlAudio, { key: JSON.stringify(params) })
            .then((response) => {
                if (response.data.error === "error") {
                    console.log("bakend error");
                } else {
                    const status = document.getElementById("status");
                    status.innerText = response.data.result;
                }
            },
                function (err) {
                    console.log(err.data);
                }
            );
    }

    // 记录音频
    recordAudio() {
        const record = document.getElementById('start');
        const visualizer = document.getElementById('visualizer');
        const status = document.getElementById("status");
        let audioCtx;
        const canvasCtx = visualizer.getContext("2d");
        if (navigator.mediaDevices.getUserMedia) {
            const constraints = { audio: true };
            let chunks = [];
            let onSuccess = (stream) => {
                const mediaRecorder = new MediaRecorder(stream);
                this.visualizeAudio(audioCtx, canvasCtx, stream, visualizer);
                record.onclick = ()=> {
                    if (status.innerText !== "Listening...") {
                        this.setStateValue("voiceIcon",<AudioOutlined style={{ fontSize: "2em", color: "white" }} spin="true"/>)
                        status.innerText = "Listening...";
                        mediaRecorder.start();
                    } else {
                        this.setStateValue("voiceIcon",<AudioMutedOutlined style={{ fontSize: "2em", color: "white" }}/>)
                        status.innerText = "Waiting...";
                        mediaRecorder.stop();
                        record.style.filter = "";
                    }

                }
                mediaRecorder.ondataavailable = (e) => {
                    let that = this;
                    chunks.push(e.data);
                    // blob转base64
                    function blobToDataURL(blob) {
                        let a = new FileReader();
                        a.onload = function (e) {
                            that.postAudio.call(that, e.target.result);
                        }
                        a.readAsDataURL(blob);
                    }
                    blobToDataURL(e.data);
                }
            }
            let onError = function (err) {
                console.log('Error:' + err);
            }
            navigator.mediaDevices.getUserMedia(constraints).then(onSuccess, onError);
        } else {
            console.log('getUserMedia not supported!');
        }
    }

    // 可视化音频
    visualizeAudio(audioCtx, canvasCtx, stream, visualizer) {
        if (!audioCtx) {
            audioCtx = new AudioContext();
        }
        const source = audioCtx.createMediaStreamSource(stream);
        const analyser = audioCtx.createAnalyser();
        analyser.fftSize = 2048;
        const bufferLength = analyser.frequencyBinCount;
        const dataArray = new Uint8Array(bufferLength);
        source.connect(analyser);
        draw()
        function draw() {
            const WIDTH = visualizer.width
            const HEIGHT = visualizer.height;
            requestAnimationFrame(draw);
            analyser.getByteTimeDomainData(dataArray);
            let grd = canvasCtx.createLinearGradient(0, 60, 0, 0);
            grd.addColorStop(0, "black");
            grd.addColorStop(0.5, "black");
            grd.addColorStop(1, "black");
            canvasCtx.fillStyle = grd;
            canvasCtx.fillRect(0, 0, WIDTH, HEIGHT);
            canvasCtx.lineWidth = 2;
            canvasCtx.strokeStyle = "darkgrey";
            canvasCtx.beginPath();
            let sliceWidth = WIDTH * 1.0 / bufferLength;
            let x = 0;
            for (let i = 0; i < bufferLength; i++) {
                let v = dataArray[i] / 128.0;
                let y = v * HEIGHT / 2;
                if (i === 0) {
                    canvasCtx.moveTo(x, y);
                } else {
                    canvasCtx.lineTo(x, y);
                }
                x += sliceWidth;
            }
            canvasCtx.lineTo(visualizer.width, visualizer.height / 2);
            canvasCtx.stroke();
        }
    }

    // 打开摄像机
    getCamera() {
        let video = document.getElementById("video001");
        let constraints = {
            video: { width: 300, height: 300 },
            audio: false
        };
        if (navigator.mediaDevices.getUserMedia(constraints) === 'undefined') {
            alert("can't use media devices!");
        } else {
            var promise = navigator.mediaDevices.getUserMedia(constraints);
        }
        promise.then((MediaStream) => {
            video.srcObject = MediaStream;
            video.play();
        }).catch(function (PermissionDeniedError) {
            console.log(PermissionDeniedError);
        })
    }

    // 拍照
    takePhoto() {
        let video = document.getElementById("video001");
        let canvas = document.getElementById("canvas001");
        let ctx = canvas.getContext('2d');
        ctx.drawImage(video, 0, 0, 300, 300);
        this.postImage(canvas.toDataURL("image/jpg"));
    }

    // 传image给后台,接收字符串
    postImage(params) {
        let urlImg = `http://127.0.0.1:5000/api/image/`;
        // let urlImg = `/api/image/`;
        axios.post(urlImg, { key: JSON.stringify(params) })
            .then((response) => {
                const status = document.getElementById("status");
                if (response.data.error === "error") {
                    console.log("bakend error");
                } else {
                    if (response.data.result !== "NOBODY") {
                        clearInterval(this.state.verificationTimer);
                        let video = document.getElementById("video001");
                        let canvas = document.getElementById("canvas001");
                        let aiVoice = document.getElementById("aiVoice");
                        video.style.display = "none";
                        canvas.hidden = false;
                        aiVoice.src = `data:audio/mp3;base64,${response.data.aiVoice}`;
                        aiVoice.play();
                        status.innerText = `Hi,${response.data.result}`;
                    } else {
                        status.innerText = "验证未通过";
                    }
                }
            },
                function (err) {
                    console.log(err.data);
                }
            );
    }

    render() {
        const whole = {
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            minHeight: "100vh",
            flexDirection: "column",
            backgroundImage: "linear-gradient(45deg, steelblue, white)"
        };
        const voiceInput = {
            position: "relative",
            marginTop: "20px"
        }
        const btn = {
            position: "absolute",
            height: "64px",
            width: "64px",
            top: 84 / 2 - 32,
            left: 300 / 2 - 32,
            border: "2px dashed white"
        }
        return (
            <div style={whole}>
                <h1>Admin Login</h1>
                <video id="video001" height="300" width="300" className="bordered"></video>
                <canvas id="canvas001" height="300" width="300" hidden></canvas>
                <h1 id="status">Waiting...</h1>
                <section style={voiceInput}>
                    <canvas id="visualizer" height="84" width="300" className="bordered"></canvas>
                    <Button id="start" type="ghost" icon={this.state.voiceIcon} style={btn} shape="circle" />
                    <Button id="takephoto" onClick={() => { this.takePhoto() }} hidden />
                    <audio id="aiVoice" hidden></audio>
                </section>
            </div>
        );
    }
}

export default Login;