import React from 'react';
import { Menu } from 'antd';
import Login from "./login";
import Visualization from "./visualization";
import Tools from "./tools";

class Home extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            menuSelected: "visual",
            userInterface: "visual"
        };
    }

    // 改变显示的组件
    changeShow = (e) => {
        this.setState({
            userInterface: e.key,
            menuSelected: e.key,
        })
    }

    render() {
        // change component show
        let UserInterface = null;
        let ui = this.state.userInterface;
        if (ui === "visual") {
            UserInterface = <Visualization ></Visualization>
        } else if (ui === "tools") {
            UserInterface = <Tools ></Tools>
        } else if (ui === "login") {
            UserInterface = <Login ></Login>
        }
        return (
            <div>
                <section>
                    {/* menu */}
                    <Menu theme="dark" mode="horizontal" onClick={this.changeShow} selectedKeys={this.state.menuSelected}
                        onChange={this.changeShow}
                    >
                        <Menu.Item key="visual">
                            Home
                        </Menu.Item>
                        <Menu.Item key="tools">
                            Tools
                        </Menu.Item>
                        <Menu.Item key="login">
                            Admin
                        </Menu.Item>
                    </Menu>
                    {/* change components*/}
                    {UserInterface}
                </section>
            </div>
        )
    }
}

export default Home;