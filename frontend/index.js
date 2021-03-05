class Section001 extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            w100: window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth,
            hIframe: parseInt(window.innerHeight || document.documentElement.clientHeight || document.body.clientHeights) - 194,
            verificationTimer:null,
        };
    }

    componentDidMount(){
        this.recordAudio();
        this.getCamera();
        this.setState({
            "verificationTimer":setInterval(() => {
                let takephoto = document.getElementById("takephoto");
                takephoto.click();
            }, 2000)
        })

    }
    // 动态改值
    changeCoding(e) {
        this.setState({
            [e.target.id]: e.target.value
        })
    }

    // 传audio给后台,接收字符串
    postAudio(params) {
        // let urlAudio = `http://127.0.0.1:5000/api/audio/`;
        let urlAudio = `/api/audio/`;
        axios.post(urlAudio, { key: JSON.stringify(params) })
            .then((response) => {
                if (response.data.error == "error") {
                    console.log("bakend error");
                } else {
                    // console.log(response.data.result);
                    let iframe = document.getElementById("iframe001");
                    iframe.srcdoc = response.data.result;
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
                this.visualizeAudio(audioCtx, canvasCtx, stream);
                record.onclick = function () {
                    if(status.innerText=="Waiting..."){
                        status.innerText = "Listening...";
                        mediaRecorder.start();
                        visualizer.style.filter="invert(0)";
                        record.style.backgroundColor="rgba(255,255,255,0.3)";
                        record.style.filter="invert(1)";
                    }else{
                        status.innerText = "Waiting...";
                        mediaRecorder.stop();
                        visualizer.style.filter="invert(1)";
                        record.style.backgroundColor="";
                        record.style.filter="";
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
    visualizeAudio(audioCtx, canvasCtx, stream) {
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
        if (navigator.mediaDevices.getUserMedia(constraints) == 'undefined') {
            alert("can't use media devices!");
        } else {
            var promise = navigator.mediaDevices.getUserMedia(constraints);
        }
        promise.then((MediaStream)=> {
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
        ctx.drawImage(video, 0, 0, 500, 500);
        this.postImage(canvas.toDataURL("image/jpg"));
    }

    // 传image给后台,接收字符串
    postImage(params) {
        // let urlImg = `http://127.0.0.1:5000/api/image/`;
        let urlImg = `/api/image/`;
        axios.post(urlImg, { key: JSON.stringify(params) })
            .then((response) => {
                if (response.data.error == "error") {
                    console.log("bakend error");
                } else {
                    let iframe = document.getElementById("iframe001");
                    if(response.data.result!="NOBODY"){
                        clearInterval(this.state.verificationTimer);
                        let video = document.getElementById("video001");
                        let aiVoice = document.getElementById("aiVoice");
                        video.style.display = "none";
                        iframe.srcdoc = `欢迎回来,${response.data.result}! (相似度:${response.data.likely})`;

                        aiVoice.src = `data:audio/mp3;base64,${response.data.aiVoice}`;
                        aiVoice.play();
                        const record = document.getElementById('start');
                        record.disabled = false;
                    }else{
                        iframe.srcdoc = "请点击顶部摄像头进行身份验证";
                    }
                }
            },
                function (err) {
                    console.log(err.data);
                }
            );
    }

    render() {
        return (
            <div className="whole">
                {/* 声音 */}
                <audio id="aiVoice" hidden></audio>
                <section className="flex center">
                    <video id="video001" height="500" width="500"></video>
                    <canvas id="canvas001" height="500" width="500"></canvas>
                </section>
                <section className="top flex">
                    <button id="takephoto" className="btn" onClick={()=>{this.takePhoto()}}></button>
                </section>
                {/* 中间内容界面 */}
                <section className="middle flex">
                    <iframe id="iframe001" className="iframe" height={this.state.hIframe}></iframe>
                </section>
                {/* 底部菜单栏 */}
                <section className="bottom flexv">
                    {/* 文字提示 */}
                    <h1 id="status">Waiting...</h1>
                    {/* 按钮 */}
                    <button id="start" className="btn" disabled></button>
                    {/* 声音条 */}
                    <canvas className="audio" id="visualizer" height="84px" width={this.state.w100}></canvas>
                </section>
                
            </div>
        )
    }
}

ReactDOM.render(<Section001 />, document.getElementById("section001"));