function plot_box(){
    
    var traceFare = {
      y: selFare,
      type: 'box',
      boxpoints: false,
      name: "Selected Fair"
    };
    
    var fareInDay = {
      y: allFare,
      type: 'box',
      boxpoints: false,
      name: "Fare in day"
    };
    
    var traceTip = {
      y: selTip,
      type: 'box',
      boxpoints: false,
      name: "Selected tip"
    };
    
    var tipInDay = {
      y: allTip,
      type: 'box',
      boxpoints: false,
      name: "tip in day"
    };
    var data = [traceFare, fareInDay, traceTip, tipInDay];
    var layout1 = {
        width:400,
        height:250,
        //title: 'selected fair',
        xaxis: {
                showticklabels: false,
  },
        showlegend: true};

    Plotly.newPlot('fare', data, layout1, {displayModeBar: false});
    
// draw distance of taxi'''
    
    var traceDistance = {
      y: selDistance,
      type: 'box',
      boxpoints: false,
      name: "Selected distance"
    };
     var allDistance = {
      y: allDis,
      type: 'box',
      boxpoints: false,
      name: "distance in day"
    };
    

    var data1 = [traceDistance,allDistance];
    var layout2 = {
        width:350,
        height:250,
       // title: 'distance',
        xaxis: {
                showticklabels: false,
  },
        showlegend: true};

    Plotly.newPlot('dis', data1, layout2, {displayModeBar: false});
    
    //draw passenger Count
    
    var tracePassanger = {
      y: selPsgCnt,
      type: 'box',
      boxpoints: false,
      name: "Selected passenger"
    };
    
    var psgInDay = {
      y: allPsg,
      type: 'box',
      boxpoints: false,
      name: "passenger in a day"
    };
    
    var data2 = [tracePassanger, psgInDay];
    var layout3 = {
        width: 100,
        height:200,
       // title: 'distance',
        xaxis: {
                showticklabels: false,
  },
        showlegend: true};

    Plotly.newPlot('myDiv', data2, layout2, {displayModeBar: false});
    
}