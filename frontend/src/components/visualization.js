import React from "react";
import axios from "axios";
import moment from "moment";
import { DatePicker, Card, Input } from 'antd';
import 'echarts/lib/chart/candlestick';
import ReactEcharts from 'echarts-for-react';
const { Search } = Input;
const { RangePicker } = DatePicker;

class Visualization extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			stockData: [],
			stockId: 1,
			dates: [moment("2019-01-01"), moment("2019-01-15")]
		};
	}

	componentDidMount() {
		this.getFromBackend();
	}

	// 改值
	changeVal(key, val) {
		this.setState({
			[key]: val
		});
	}

	// 限制日期长度
	disabledDate = current => {
		let dates = this.state.dates;
		const tooLate = dates[0] && current.diff(dates[0], 'days') > 30;
		const tooEarly = dates[1] && dates[1].diff(current, 'days') > 30;
		return tooEarly || tooLate;
	};

	getFromBackend() {
		let start = this.state.dates[0].format('YYYY/MM/DD');
		let end = this.state.dates[1].format('YYYY/MM/DD');
		let url = `http://127.0.0.1:5000/api/stock/?stockid=${this.state.stockId}&start=${start}&end=${end}`
		axios.get(url).then((response) => {
			if (response.data.error === "error") {
				console.log("bakend error");
			} else {
				this.changeVal("stockData", response.data);
			}
		},
			(err) => {
				console.log("frontend error", err);
			}
		);
	}

	// Echarts灯烛图
	getOption = () => {
		let transformData = () => {
			// var stockData = [
			//     ['2013/1/24', 2320.26, 2320.26, 2287.3, 2362.94,86160000],
			//     ['2013/1/25', 2300, 2291.3, 2288.26, 2308.38,79330000]];
			var stockData = this.state.stockData;
			var price = [];
			var date = [];
			var volume = [];
			for (var i = 0; i < stockData.length; i++) {
				date.push(stockData[i].slice(0, 1));
				price.push(stockData[i].slice(1, 5));
				volume.push(stockData[i].slice(-1)[0]);
			}
			var data = { price: price, date: date, volume: volume }
			return data;
		}

		let calculateMA = (dayCount) => {
			var result = [];
			for (var i = 0, len = data.date.length; i < len; i++) {
				if (i < dayCount) {
					result.push('-');
					continue;
				}
				var sum = 0;
				for (var j = 0; j < dayCount; j++) {
					sum += data.price[i - j][1];
				}
				result.push(sum / dayCount);
			}
			return result;
		}

		let upColor = '#ec0000';
		let upBorderColor = '#8A0000';
		let downColor = '#00da3c';
		let downBorderColor = '#008F28';
		let data = transformData();

		let option = {
			tooltip: {
				trigger: 'axis',
				axisPointer: {
					type: 'cross'
				},
				backgroundColor: 'rgba(245, 245, 245, 0.8)',
				borderWidth: 1,
				borderColor: '#ccc',
				padding: 10,
				textStyle: {
					color: '#000'
				},
				position: function (pos, params, el, elRect, size) {
					var obj = { top: 10 };
					obj[['left', 'right'][+(pos[0] < size.viewSize[0] / 2)]] = 30;
					return obj;
				}
			},
			legend: {
				top: '320em',
				data: ['Day K', 'MA5', 'MA10', 'MA20', 'MA30']
			},
			axisPointer: {
				link: { xAxisIndex: 'stockData' },
				label: {
					backgroundColor: '#777'
				}
			},
			toolbox: {
				feature: {
					dataZoom: {
						yAxisIndex: false
					},
					brush: {
						type: ['lineX', 'clear']
					}
				}
			},
			visualMap: {
				show: false,
				seriesIndex: 5,
				dimension: 2,
				pieces: [{
					value: 1,
					color: downColor
				}, {
					value: -1,
					color: upColor
				}]
			},
			grid: [
				{
					height: '220em'
				},
				{
					top: '370em',
					height: '80em'
				}
			],
			xAxis: [{
				type: 'category',
				data: data.date,
				scale: true,
				boundaryGap: false,
				axisLine: { onZero: false },
				splitLine: { show: false },
				splitNumber: 20,
				min: 'dataMin',
				max: 'dataMax'
			}, {
				type: 'category',
				gridIndex: 1,
				data: data.date,
				scale: true,
				boundaryGap: false,
				axisLine: { onZero: false },
				axisTick: { show: false },
				splitLine: { show: false },
				axisLabel: { show: false },
				splitNumber: 20,
				min: 'dataMin',
				max: 'dataMax'
			}],
			yAxis: [{
				scale: true,
				splitArea: {
					show: true
				}
			}, {
				scale: true,
				gridIndex: 1,
				splitNumber: 2,
				axisLabel: { show: false },
				axisLine: { show: false },
				axisTick: { show: false },
				splitLine: { show: false }
			}
			],
			dataZoom: [
				{
					type: 'inside',
					xAxisIndex: [0, 1],
					start: 50,
					end: 100
				},
				{
					show: true,
					type: 'slider',
					xAxisIndex: [0, 1],
					top: '355em',
					start: 50,
					end: 100
				}
			],
			series: [
				{
					name: 'Day K',
					type: 'candlestick',
					data: data.price,
					itemStyle: {
						color: upColor,
						color0: downColor,
						borderColor: upBorderColor,
						borderColor0: downBorderColor
					},
					markPoint: {
						label: {
							normal: {
								formatter: function (param) {
									return param != null ? Math.round(param.value) : '';
								}
							}
						},
						data: [
							{
								name: 'highest value',
								type: 'max',
								valueDim: 'highest'
							},
							{
								name: 'lowest value',
								type: 'min',
								valueDim: 'lowest'
							},
							{
								name: 'average value on close',
								type: 'average',
								valueDim: 'close'
							}
						],
						tooltip: {
							formatter: function (param) {
								return param.name + '<br>' + (param.data.coord || '');
							}
						}
					},
					markLine: {
						symbol: ['none', 'none'],
						data: [
							[
								{
									name: 'from lowest to highest',
									type: 'min',
									valueDim: 'lowest',
									symbol: 'circle',
									symbolSize: 10,
									label: {
										show: false
									},
									emphasis: {
										label: {
											show: false
										}
									}
								},
								{
									type: 'max',
									valueDim: 'highest',
									symbol: 'circle',
									symbolSize: 10,
									label: {
										show: false
									},
									emphasis: {
										label: {
											show: false
										}
									}
								}
							],
							{
								name: 'min line on close',
								type: 'min',
								valueDim: 'close'
							},
							{
								name: 'max line on close',
								type: 'max',
								valueDim: 'close'
							}
						]
					}
				},
				{
					name: 'Volume',
					type: 'bar',
					xAxisIndex: 1,
					yAxisIndex: 1,
					data: data.volume
				},
				{
					name: 'MA5',
					type: 'line',
					data: calculateMA(5),
					smooth: true,
					lineStyle: {
						opacity: 0.5
					}
				},
				{
					name: 'MA10',
					type: 'line',
					data: calculateMA(10),
					smooth: true,
					lineStyle: {
						opacity: 0.5
					}
				},
				{
					name: 'MA20',
					type: 'line',
					data: calculateMA(20),
					smooth: true,
					lineStyle: {
						opacity: 0.5
					}
				},
				{
					name: 'MA30',
					type: 'line',
					data: calculateMA(30),
					smooth: true,
					lineStyle: {
						opacity: 0.5
					}
				},

			]
		};

		return option
	}

	render() {
		return (
			<div>
				<Card title="Gold Futures Prices">
					<Card
						hoverable='true'
						style={{ marginTop: 16 }}
						type="inner"
						title="CandleStick"
						extra={
							<Search
								placeholder="Stock Code"
								allowClear
								value={this.state.stockId}
								onChange={(e) => { this.changeVal("stockId", e.target.value) }}
								size="large"
								onSearch={() => { this.getFromBackend() }}

							/>
						}
					>
						<RangePicker size="large"
							onChange={(dateMt) => { this.changeVal("dates", dateMt) }}
							onCalendarChange={(dateMt) => { this.changeVal("dates", dateMt) }}
							value={this.state.dates}
							defaultValue={this.state.dates}
							disabledDate={this.disabledDate}
						/>
						<ReactEcharts option={this.getOption()} style={{ height: '50em' }} />
					</Card>
				</Card>
			</div>
		);
	}
}

export default Visualization;