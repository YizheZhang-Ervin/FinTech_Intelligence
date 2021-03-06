import React from "react";
import axios from "axios";
import { Divider } from 'antd';
import { Select } from 'antd';
import { Input } from 'antd';
import { Button } from 'antd';
import { SearchOutlined } from '@ant-design/icons';
const { Option } = Select;
const { TextArea } = Input;

class Tools extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            fromlang: "english",
			tolang: "chinese",
            inputSentence:"",
			translatedSentence:""
        };
    }

    changeSelect(val, key) {
		this.setState({
			[key]: val
		})
	}

	getTranslate() {
		let url = `http://127.0.0.1:5000/api/translate/?sentence=${this.state.inputSentence}&fromlang=${this.state.fromlang}&tolang=${this.state.tolang}`
		axios.get(url).then((response) => {
			if (response.data.error === "error") {
				console.log("bakend error");
			} else {
				this.changeSelect(response.data.result,"translatedSentence");
			}
		},
			(err) => {
				console.log("frontend error", err);
			}
		);
	}

    render() {
        const whole = {
			display: "flex",
			alignItems: "center",
			justifyContent: "flexStart",
			flexDirection: "column",
		};
        const flexv = {
            display: "flex",
			alignItems: "center",
            justifyContent: "space-between",
			flexDirection: "row",
            width:"100vw"
        }
		const w50={
			width:"50vw"
		};
        const w10 = {
            width:"10vw"
        }
        return (
            <div style={whole}>
                <Divider orientation="left">Translator</Divider>
                <div style={flexv}>
                    <div>
                    <Select style={w10} placeholder="输入语言类型" onChange={(val) => { this.changeSelect(val, "fromlang") }} defaultValue="english">
                        <Option value="english">English</Option>
                        <Option value="chinese">汉语</Option>
                        <Option value="french">Français</Option>
                        <Option value="spanish">Español</Option>
                        <Option value="russian">Русский язык</Option>
                        <Option value="hindi">हिन्दी</Option>
                    </Select>
                    <Select style={w10} placeholder="输出语言类型" onChange={(val) => { this.changeSelect(val, "tolang") }} defaultValue="chinese">
                        <Option value="english">English</Option>
                        <Option value="chinese">汉语</Option>
                        <Option value="french">Français</Option>
                        <Option value="spanish">Español</Option>
                        <Option value="russian">Русский язык</Option>
                        <Option value="hindi">हिन्दी</Option>
                    </Select>
                    </div>
                    <Button style={w10} icon={<SearchOutlined />} onClick={() => this.getTranslate()}>Translate</Button>
                </div>
                <div style={flexv}>
                    <TextArea style={w50} rows={5} onBlur={() => this.getTranslate()} 
                    value={this.state.inputSentence} onChange={(e)=>this.changeSelect(e.target.value,"inputSentence")}
                    onPressEnter={() => this.getTranslate()} placeholder="请输入内容" showCount maxLength={255} allowClear />
                    <TextArea style={w50} rows={5} placeholder="翻译内容" showCount maxLength={255} value={this.state.translatedSentence} disabled/>
                </div>
            </div>
        );
    }
}

export default Tools;