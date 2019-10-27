
var init_height;
var init_width;
var init_selected;

function clearPies() {
    $('#company').empty();
    $('#company').removeAttr("style");
    $('#device').empty();
    $('#device').removeAttr("style");   
}

function visCompanyPie(data, name) {
    var text = "";

    var width = 200;
    var height = 200;
    var thickness = 40;
    var duration = 750;
    var padding = 10;
    var opacity = .8;
    var opacityHover = 1;
    var otherOpacityOnHover = .8;
    var tooltipMargin = 13;
    data = Object.keys(data).map((d) => [d, data[d]])

    var width = 500,
        height = 280,
        radius = Math.min(width, height) / 3;

    //var color = d3.scaleOrdinal()
        //.range(["#98abc5", "#8a89a6", "#7b6888"]);
    var color = d3.scaleOrdinal(d3.schemeCategory20);

    var arc = d3.arc()
        .outerRadius(radius*1.5)
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
        .attr("transform", "translate(" + width/3 + "," + height / 2 + ")");


    var g = svg.selectAll(".arc")
        .data(pie(data))
        .enter().append("g")
        .attr("class", "arc");
    

        var path = g.selectAll('path')
        .data(pie(data))
        .enter()
        .append("g")  
        .append('path')
        .attr('d', arc)
        .attr('fill', (d,i) => color(i))
        .style('opacity', opacity)
        .style('stroke', 'white')
        .on("mouseover", function(d) {
            d3.selectAll('path')
              .style("opacity", otherOpacityOnHover);
            d3.select(this) 
              .style("opacity", opacityHover);
      
            let g = d3.select("svg")
              .style("cursor", "pointer")
              .append("g")
              .attr("class", "tooltip")
              .style("opacity", 0);
            g.append("text")
              .attr("class", "name-text")
              .text(`${d.data[0]} (${d.data[1]})`)
              .attr('text-anchor', 'middle');
          
            let text = g.select("text");
            let bbox = text.node().getBBox();
            let padding = 2;
            g.insert("rect", "text")
              .attr("x", bbox.x - padding)
              .attr("y", bbox.y - padding)
              .attr("width", bbox.width + (padding*2))
              .attr("height", bbox.height + (padding*2))
              .style("fill", "white")
              .style("opacity", 0.75);
          })
        .on("mousemove", function(d) {
              let mousePosition = d3.mouse(this);
              let x = mousePosition[0] + width/2;
              let y = mousePosition[1] + height/2 - tooltipMargin;
          
              let text = d3.select('.tooltip text');
              let bbox = text.node().getBBox();
              if(x - bbox.width/2 < 0) {
                x = bbox.width/2;
              }
              else if(width - x - bbox.width/2 < 0) {
                x = width - bbox.width/2;
              }
          
              if(y - bbox.height/2 < 0) {
                y = bbox.height + tooltipMargin * 2;
              }
              else if(height - y - bbox.height/2 < 0) {
                y = height - bbox.height/2;
              }
          
              d3.select('.tooltip')
                .style("opacity", 1)
                .attr('transform',`translate(${x}, ${y})`);
          })
        .on("mouseout", function(d) {   
            d3.select("svg")
              .select(".tooltip").remove();
          d3.selectAll('path')
              .style("opacity", opacity);
          })
        .each(function(d, i) { this._current = i; });

    g.append("path")
        .attr("d", arc)
        .style("fill", function(d) { return color(d.data); });

    
    
}
