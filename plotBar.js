function plotBar(){
    var barData = [
  {
    x: ['distance', 'fare', 'tip', 'passenger count'],
    y: list,
    name: 'Correlation',
    type: 'bar'
  }
];
    var layout = {
        width:450,
        height:250 ,
        showlegend: true};

Plotly.newPlot('myDiv2', barData, layout, {displayModeBar: false});
}