import React from "react";
import axios from "axios";
import { Select } from 'antd';
import { Input } from 'antd';
import { Button } from 'antd';
const { Option } = Select;
const { TextArea } = Input;

class Translator extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			fromlang: "english",
			tolang: "chinese",
			translatedSentence:""
		};
	}

	// 动态改值
	// changeValue(e) {
	//     this.setState({
	//         [e.target.id]: e.target.value
	//     })
	// }

	changeSelect(val, key) {
		this.setState({
			[key]: val
		})
	}

	getTranslate(e) {
		let url = `http://127.0.0.1:5000/api/translate/?sentence=${e.target.value}&fromlang=${this.state.fromlang}&tolang=${this.state.tolang}`
		axios.get(url).then((response) => {
			if (response.data.error == "error") {
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
		const wholeStyle = {
			display: "flex",
			alignItems: "center",
			justifyContent: "flexStart",
			flexDirection: "column",
		};
		const wmin100={
			minWidth:"100vw"
		};
		return (
			<div style={wholeStyle}>
				<div>
					<Select placeholder="输入语言类型" onChange={(val) => { this.changeSelect(val, "fromlang") }} defaultValue="english">
						<Option value="english">English</Option>
						<Option value="chinese">汉语</Option>
						<Option value="french">Français</Option>
						<Option value="spanish">Español</Option>
						<Option value="russian">Русский язык</Option>
						<Option value="hindi">हिन्दी</Option>
					</Select>

					<Select placeholder="输出语言类型" onChange={(val) => { this.changeSelect(val, "tolang") }} defaultValue="chinese">
						<Option value="english">English</Option>
						<Option value="chinese">汉语</Option>
						<Option value="french">Français</Option>
						<Option value="spanish">Español</Option>
						<Option value="russian">Русский язык</Option>
						<Option value="hindi">हिन्दी</Option>
					</Select>
				</div>
				<TextArea style={wmin100} rows={5} onBlur={(e) => this.getTranslate(e)}
				onPressEnter={(e) => this.getTranslate(e)} placeholder="请输入内容" showCount maxLength={255} allowClear/>
				<TextArea style={wmin100} rows={5} placeholder="翻译内容" autoSize allowClear value={this.state.translatedSentence}/>
			</div>
		);
	}
}

export default Translator;