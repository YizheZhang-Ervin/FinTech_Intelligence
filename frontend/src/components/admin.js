import React from 'react';
import axios from "axios";
import { Input,Divider,Button } from 'antd';
const { TextArea } = Input;

class Admin extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            commands: "",
            commandsResult: "",
            commandsHistory:""
        };
    }

    // 设置state值
    setStateValue(key, val) {
        this.setState({
            [key]: val
        })
    }

    getOS() {
        let urlOS = `http://127.0.0.1:5000/api/admin/`;
        // let urlOS = `/api/admin/`;
        axios.post(urlOS, { commands: JSON.stringify(this.state.commands) })
            .then((response) => {
                if (response.data.error === "error") {
                    console.log("backend error");
                } else {
                    this.setStateValue("commandsResult", response.data.result);
                    this.setStateValue("commandsHistory", this.state.commandsHistory+this.state.commands);
                    this.setStateValue("commands", "");
                }
            },
                (err) => {
                    console.log(err.data);
                }
            );
    }

    render() {
        const whole = {
            backgroundColor: "black",
            color: "gold",
            minHeight: "100vh",
            width: "100vw"
        }
        const codeArea1 = {
            backgroundColor: "black",
            color: "gold",
            border: "none",
            height: "10vh",
            width: "100vw"
        }
        const codeArea2 = {
            backgroundColor: "black",
            color: "gold",
            border: "none",
            height: "15vh",
            width: "100vw"
        }
        const codeArea3 = {
            backgroundColor: "black",
            color: "gold",
            border: "none",
            minHeight: "50vh",
            width: "100vw"
        }
        const dividerStyle={
            color:"gold",
            borderColor:"gold"
        }
        const titleStyle={
            color:"gold",
            fontSize:"2em"
        }
        return (
            <div style={whole}>
                <Button id="adminbtn" type="link" href="/" style={titleStyle}>Command Prompt</Button>
                <Divider orientation="left" style={dividerStyle}>History</Divider>
                <TextArea style={codeArea1} value={this.state.commandsHistory} disabled />
                <Divider orientation="left" style={dividerStyle}>CMD</Divider>
                <TextArea style={codeArea2} value={this.state.commands}
                    onChange={(e) => this.setStateValue("commands", e.target.value)}
                    onPressEnter={(e) => { this.getOS() }}
                    placeholder="please enter commands here..."
                />
                <Divider orientation="left" style={dividerStyle}>Result</Divider>
                <TextArea style={codeArea3} value={this.state.commandsResult} disabled />
            </div>
        )
    }
}

export default Admin;