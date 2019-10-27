
var init_height;
var init_width;
var init_selected;

function clearPies() {
    $('#company').empty();
    $('#company').removeAttr("style");
    $('#device').empty();
    $('#device').removeAttr("style");   
}

function visDevicePie(data, name) {
    data = Object.keys(data).map((d) => [d, data[d]])

var width = 500,
    height = 280,
    radius = Math.min(width, height) / 3;

var color = d3.scaleOrdinal()
    .range(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);

var arc = d3.arc()
    .outerRadius(radius*.9)
    .innerRadius(radius*.2);

var labelArc = d3.arc()
    .outerRadius(radius*.8)
    .innerRadius(radius*.8);

var pie = d3.pie()
    .sort(null)
    .value(function(d) { return d[1]; });

var svg = d3.select("#device")
    .attr("width", width)
    .attr("height", height)
  .append("g")
    .attr("transform", "translate(" + width/4 + "," + height / 2+ ")");

  var g = svg.selectAll(".arc")
      .data(pie(data))
    .enter().append("g")
      .attr("class", "arc");

  g.append("path")
      .attr("d", arc)
      .style("fill", function(d) { return color(d.data); });

      
  g.append("text")
      //.attr("transform", function(d) { return "translate(" + labelArc.centroid(d)[0]+10 + ',' + labelArc.centroid(d)[1] + ")"; })
      .attr("x", function(d) {
        var a = d.startAngle + (d.endAngle - d.startAngle)/2 - Math.PI/2;
        d.cx = Math.cos(a) * (radius - 45);
        return d.x = Math.cos(a) * (radius+30);
    })
    .attr("y", function(d) {
        var a = d.startAngle + (d.endAngle - d.startAngle)/2 - Math.PI/2;
        d.cy = Math.sin(a) * (radius - 45);
        return d.y = Math.sin(a) * (radius + 30);
    })
      .attr("dy", ".1em")
      .text(function(d) {
        if (d.data[1] > 1) {
            return d.data[0];
        } else{
          return ""; 
        }
      })
      .each(function(d) {
        if(d.data[1] > 1) {
            var bbox = this.getBBox();
            d.sx = d.x - bbox.width/2 - 2;
            d.ox = d.x + bbox.width/2 + 2;
            d.sy = d.oy = d.y + 5;
        }
        
    });
      g.append("path")
      .attr("class", "pointer")
      .style("fill", "none")
      .style("stroke", "black")
      
      .attr("d", function(d) {
       console.log(d);
          if(d.cx > d.ox) {
              return "M" + d.sx + "," + d.sy + "L" + d.ox + "," + d.oy + " " + d.cx + "," + d.cy;
          } else {
              return "M" + d.ox + "," + d.oy + "L" + d.sx + "," + d.sy + " " + d.cx + "," + d.cy;
          }
      });
      var outstring = "";
if (name == "") {
    outstring = "Device Interest";
} else {
    outstring = name+"\'s Device Interest"; 
}
svg.append("text")
    .attr("x", 0)
    .attr("y", height/2)
    .attr("text-anchor", "middle")  
    .style("font-size", "16px") 
    .text(outstring);
}

function visCompanyPie(data, name) {
    data = Object.keys(data).map((d) => [d, data[d]])

    var width = 500,
        height = 280,
        radius = Math.min(width, height) / 3;

    var color = d3.scaleOrdinal()
        .range(["#98abc5", "#8a89a6", "#7b6888"]);

    var arc = d3.arc()
        .outerRadius(radius*.9)
        .innerRadius(radius*.2);

    var labelArc = d3.arc()
        .outerRadius(radius*.8)
        .innerRadius(radius*.8);

    var pie = d3.pie()
        .sort(null)
        .value(function(d) { return d[1]; });

    var svg = d3.select("#company")
        .attr("width", width)
        .attr("height", height)
    .append("g")
        .attr("transform", "translate(" + width/4 + "," + height / 2 + ")");

    var g = svg.selectAll(".arc")
        .data(pie(data))
        .enter().append("g")
        .attr("class", "arc");

    g.append("path")
        .attr("d", arc)
        .style("fill", function(d) { return color(d.data); });

        g.append("text")
        //.attr("transform", function(d) { return "translate(" + labelArc.centroid(d)[0]+10 + ',' + labelArc.centroid(d)[1] + ")"; })
        .attr("x", function(d) {
            var a = d.startAngle + (d.endAngle - d.startAngle)/2 - Math.PI/2;
            d.cx = Math.cos(a) * (radius - 45);
            return d.x = Math.cos(a) * (radius+30);
        })
        .attr("y", function(d) {
            var a = d.startAngle + (d.endAngle - d.startAngle)/2 - Math.PI/2;
            d.cy = Math.sin(a) * (radius - 45);
            return d.y = Math.sin(a) * (radius + 30);
        })
        .attr("dy", ".1em")
        .text(function(d) {
            if (d.data[1] > 5) {
                return d.data[0];
            } else{
            return ""; 
            }
        })
        .each(function(d) {
            if(d.data[1] > 5) {
                var bbox = this.getBBox();
                d.sx = d.x - bbox.width/2 - 2;
                d.ox = d.x + bbox.width/2 + 2;
                d.sy = d.oy = d.y + 5;
            }
        });
        g.append("path")
        .attr("class", "pointer")
        .style("fill", "none")
        .style("stroke", "black")
        
        .attr("d", function(d) {
        console.log(d);
            if(d.cx > d.ox) {
                return "M" + d.sx + "," + d.sy + "L" + d.ox + "," + d.oy + " " + d.cx + "," + d.cy;
            } else {
                return "M" + d.ox + "," + d.oy + "L" + d.sx + "," + d.sy + " " + d.cx + "," + d.cy;
            }
        });
        if (name == "") {
            outstring = "Brand Interest";
        } else {
            outstring = name+"\'s Brand Interest"; 
        }
    svg.append("text")
        .attr("x", 0)             
        .attr("y", height/2)
        .attr("text-anchor", "middle")  
        .style("font-size", "16px") 
        .text(outstring);

    
}
