function plotLine(){
    //temp
    var trace1 = {
       x: hour,
       y: tempList,
       name: 'temperature',
       mode: 'lines+markers'
    };
    var data =[trace1];
    var layout = {
        width:450,
        height:300,
        showlegend: true};
    Plotly.newPlot('tempVis', data,layout, {displayModeBar: false});
    
    //vsb
     var trace2 = {
       x: hour,
       y: vsbList,
       name: 'visibility in miles',
        mode: 'lines+markers'
    };
    var data1 =[trace2];
    Plotly.newPlot('tempVis1', data1,layout, {displayModeBar: false});

  //rain
   var trace3 = {
       x: hour,
       y: pcpList,
       name:'liquid precip in hour',
        mode: 'lines+markers'
    };
    var data2 =[trace3];
    Plotly.newPlot('tempVis2', data2,layout, {displayModeBar: false});
}