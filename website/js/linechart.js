function clearLineChart() {

}

function visLineChart(data, field, out_id) {
    field_string = field[0].toUpperCase() + field.slice(1); 
    var inputTitle = field_string + " Level History";
    var yaxis = "Level";
    var xaxis = "Time";
    if (data[field] == undefined) {
        debugger;
    }
    datalist = data[field].map((x)=> {
        return [parseInt(x.timestamp)*1000, x[field]];
    });
    if (field == "volume") { 
        maxVal = 100;
        minVal = 0;
    } 
    if (field == "bass") {
        maxVal = 0;
        minVal = -9;
    }


    Highcharts.setOptions({
        global: { 
            useUTC: false // true by default
        }
    });
    
    Highcharts.chart(out_id, {
        title: {
            text: inputTitle
        },
    
        yAxis: {
            title: {
                text: yaxis
            },
            max: maxVal,
            min: minVal
        },
        xAxis: {
            title: {
                text: xaxis
            },
            type: "datetime"
        },

    /*
        plotOptions: {
            series: {
                label: {
                    connectorAllowed: false
                },
                pointStart: 2010
            }
        },
    */
        series: [{
            name: field_string,
            data: datalist,
            type: 'spline'
        }],
    
    
    });
    var creds = document.getElementsByClassName("highcharts-credits");
    for (var i = 0; i < creds.length; i++) {
        creds[i].remove();
    }
    var button = document.getElementsByClassName("highcharts-exporting-group");
    for (var i = 0; i < button.length; i++) {
        button[i].remove();
    }

}