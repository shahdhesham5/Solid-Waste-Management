

var chart_labels=[]
var chart_data=[]
var line_length=[]

fetch('http://localhost/geoserver/geonode/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode%3Aline_water&maxFeatures=50&outputFormat=application%2Fjson')
.then((response)=>response.json())
.then((data)=>
 {
 for(let i=0;i< data.features.length;i++){
   var line= data.features[i]
   // console.log(line);
   var diameter=line.properties.Diameter
   var name = line.properties.Markaz_Nam+line.id
   var length=line.properties.Shape_Leng
   chart_data.push(diameter)
   chart_labels.push(name)
   line_length.push(length)
    // console.log(diameter,name);
 }



   // console.log(chart_data);
   // console.log(chart_labels);
    //var chart_labels = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'];
    //var chart_data = [100, 70, 90, 70, 85, 60, 75, 60, 90, 80, 110, 100];


    var ctx = document.getElementById("chartBig1").getContext('2d');

    var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(72,72,176,0.1)');
    gradientStroke.addColorStop(0.4, 'rgba(72,72,176,0.0)');
    gradientStroke.addColorStop(0, 'rgba(119,52,169,0)'); //purple colors
    var config = {
      type: 'line',
      data: {
        labels: chart_labels,
        datasets: [{
          label: "Diameters of line water",
          fill: false,
          backgroundColor: gradientStroke,
          borderColor: '#d346b1',
          borderWidth: 2,
          borderDash: [],
          borderDashOffset: 0.0,
          pointBackgroundColor: '#d346b1',
          pointBorderColor: 'rgba(255,255,255,0)',
          pointHoverBackgroundColor: '#d346b1',
          pointBorderWidth: 20,
          pointHoverRadius: 6,
          pointHoverBorderWidth: 15,
          pointRadius: 4,
          data: chart_data,
        }]
      },
      options: {
          scales: {
              yAxes: [{
                  ticks: {
                      beginAtZero: true
                  }
              }]
          }
     },
      // options: gradientChartOptionsConfigurationWithTooltipPurple
    };
    var myChartData = new Chart(ctx, config);
    $("#0").click(function() {
      var data = myChartData.config.data;
      data.datasets[0].data = chart_data;
      data.labels = chart_labels;
      myChartData.update();
    });
    $("#1").click(function() {
      var chart_data = line_length;
      var data = myChartData.config.data;
      data.datasets[0].data = chart_data;
      data.labels = chart_labels;
      myChartData.update();
    });

    $("#2").click(function() {
      var chart_data = [60, 80, 65, 130, 80, 105, 90, 130, 70, 115, 60, 130];
      var data = myChartData.config.data;
      data.datasets[0].data = chart_data;
      data.labels = chart_labels;
      myChartData.update();
    });
  }
  );
