import React from "react";
import axios from "axios";

class Videochat extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
		};
	}

	render() {
		const wholeStyle = {
			display: "flex",
			alignItems: "center",
			justifyContent: "center",
			flexDirection: "column",
			height: "100vh",
			width: "100vw",
		};
		return (
			<div style={wholeStyle}>

			</div>
		);
	}
}

export default Videochat;