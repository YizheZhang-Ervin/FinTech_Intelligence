import React from 'react';
import { Menu } from 'antd';
import Recognition from "./recognition";
import Translator from "./translator";
import Videochat from "./videochat";

class Home extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            menuSelected:"tr",
            userInterface:"tr"
        };
    }

    // 改变显示的组件
    changeShow =(e)=> {
        this.setState({
            userInterface: e.key,
            menuSelected:e.key,
        })
    }

    render() {
        // change component show
        let UserInterface = null;
        let ui = this.state.userInterface;
        if(ui==="rec"){
            UserInterface = <Recognition ></Recognition>
        }else if(ui==="tr"){
            UserInterface = <Translator ></Translator>
        }else{
            UserInterface = <Videochat ></Videochat>
        }
        return (
            <div>
                <section>
                    {/* menu */}
                    <Menu theme="dark" mode="horizontal" onClick={this.changeShow} selectedKeys={this.state.menuSelected}
                        onChange={this.changeShow}
                    >
                        <Menu.Item key="rec">
                            Recognition
                        </Menu.Item>
                        <Menu.Item key="tr">
                            Translator
                        </Menu.Item>
                        <Menu.Item key="vc">
                            Videochat
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