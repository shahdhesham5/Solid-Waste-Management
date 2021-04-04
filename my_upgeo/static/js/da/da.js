function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');





















function spinner(x,y){
x.onreadystatechange = function () {
  var state = x.readyState
  if (state == 'interactive') {
       x.getElementById('mapid').style.visibility="hidden";
  } else if (state == 'complete') {
      setTimeout(function(){
         x.getElementById('interactive');
         x.getElementById(y).style.visibility="hidden";
         x.getElementById('mapid').style.visibility="visible";
      },1000);
  }
}
}
spinner(document,'load')




//EditingLayer
var EditLayer=document.getElementById('EditLayer')
EditLayer.addEventListener('click',function(){

  document.getElementById('EditingLayerContainer').innerHTML='<div class="">'+
  '<label for="attr1"><span class="label" style="margin-right:21px">Choose layer:</span></label>'+
  '<select name="attr1" id="layersToEdit" form="carform" >'+
  '    {% for item in  layers%}'+
  '  <option value="{{item.name}}">{{item.name}} </option>'+
  '           {% endfor%}'+
  '</select>'+
  '<button type="button" id="EditLayerbtn" name="button"> Edit</button>'+
  '</div>'
  addEventToEditBtn()
  })

  function addEventToEditBtn(){
  var Editbtn=document.getElementById("EditLayerbtn")
  Editbtn.addEventListener('click',function(){
    loadingData()
  })
}
  function loadingData(){
    var layerToEditm= geoLayers[document.getElementById('layersToEdit').value];
    //get copy of layer
    var layerToEdit={
      ...layerToEditm
    }
    var myFeature=L.geoJSON(layerToEdit,{
      onEachFeature:function(feature,layer){
        // console.log(feature);
        layer.on('click',function(){
          console.log(feature);
          console.log(document.getElementsByTagName('tr').length)
          for (let i=1;i<document.getElementsByTagName('tr').length;i++){
            for (let j=0;j<document.getElementsByTagName('tr')[9].cells.length;j++){
              document.getElementsByTagName('tr')[i].cells[j].style.backgroundColor='white'
            }
          if(document.getElementsByTagName('tr')[i].cells[0].firstElementChild.value==feature.properties.fid){
          document.getElementsByTagName('tr')[i].scrollIntoView({
                      behavior: 'smooth',
                      block: 'center'
                  });
          for (let j=0;j<document.getElementsByTagName('tr')[9].cells.length;j++){
            document.getElementsByTagName('tr')[i].cells[j].style.backgroundColor='green'
          }
        }
      }
        })
      }
    }).addTo(mymap)

    var attributes=Object.keys(layerToEdit.features[0].properties)
    //get layer features
    var layerFeatures=layerToEdit.features
    var attrValues=layerToEdit.features[0].properties
    console.log(attrValues);
    document.getElementById('th').innerHTML=''
    document.getElementById('Table').innerHTML="<tr id='th'> </tr>"
    for (key in attributes){
      document.getElementById('th').innerHTML+='<th>'+attributes[key]+'</th>'
     '<tr>'+attrValues[attributes[key]]+'</tr>'
    }
    for (feature in layerFeatures){
      var feat='<tr>'
      for (key in attributes){
          feat+='<td> <input class="inputs" type="text" data="'+feature+'" value='+layerFeatures[feature].properties[attributes[key]]+' /> </td>'
            }
        feat +='</tr>'

      document.getElementById('Table').innerHTML+=feat
    }



    var inputs=document.getElementsByClassName('inputs')
    for (let i=0;i<inputs.length;i++){
       inputs[i].addEventListener('change',function(e){
          //get the edited attribute
          var EditedAttr=attributes[i%attributes.length];
          var EFeature=layerFeatures[this.attributes.data.value]
          layerFeatures[this.attributes.data.value].properties[EditedAttr]=inputs[i].value


       latLong = []
           // mymap.removeLayer(myFeature)
           if (layerFeatures[this.attributes.data.value].geometry.type=='MultiPolygon'){
             layerFeatures[this.attributes.data.value].geometry.coordinates[0].forEach(function(locationArray){
                    locationArray.forEach(function(location){
                        latLong.push([location[1] , location[0]]);
                    });
                   });
               console.log("polygon",latLong);
             var Epolygon = L.polygon(latLong,{
               style:{fillColor:'red'}
             }).addTo(mymap);
                }else{
                  // latLong=layerFeatures[this.attributes.data.value].geometry.coordinates[0]
                  layerFeatures[this.attributes.data.value].geometry.coordinates[0].forEach(function(location){
                                 latLong.push([location[1] , location[0]]);

                        });
                  console.log("polyline",latLong);
                  var Epolygon = L.polyline(latLong,{
                    style:{color:'red'}
                  }).addTo(mymap);
                }
             Epolygon.editing.enable();
             Epolygon.on('dblclick',function(){
               EFeature.geometry.coordinates[0]=Epolygon._latlngs
              console.log(',,,,',layerToEdit)
               // mymap.removeLayer(myFeature)
               // var myEditedFeature=L.geoJSON(layerToEdit).addTo(mymap)


                   })
             latLong = [];



                   // console.log(e.target);



      })
    }

  }




// adding Rule
var addRule = document.getElementById('addRule')
var ruleContainer=document.getElementById('ruleContainer')

addRule.addEventListener('click',function(){

  ruleContainer.innerHTML+="<div class='rule'>"+"<select name='attra' class='attra' form='carform' ><option value='2'>2</option></select>"+
                              "<select name='attrb' class='attrb' form='carform' ><option value='1'>1</option></select>"+
                              '<input type="text" class="result" value="0"> %'+
                              '<input type="color" class="colorpicker" value="#0000ff">'+"</div>"
  addAttr(layerName)
  addLayer(temp)
  b()
  formattingLayers()

})

var clearRules=document.getElementById('clearRule')
  // var rules=document.getElementsByClassName('rule')
clearRules.addEventListener('click',function(){
  var rules=document.getElementsByClassName('rule')
  while(rules.length > 0) {
    rules[0].remove();
}

})




// enableEditing
var showbtn=document.getElementById('hideshow')
var editingContainer=document.getElementById('editingContainer')
showbtn.addEventListener('click',function(){
  if(editingContainer.style.display=="none"){
    editingContainer.style.display = "block"
    showbtn.value='Stop Editing'
    temp=geoLayers[layerName]
    addLayer(temp)
    addAttr(layerName)
    b()

  }else{
    editingContainer.style.display="none"
    showbtn.value='Edit'

}
})




//initiate map
var mymap = L.map('mapid',{editable: true}).setView([51.505, -0.09], 4);

//initiate base map
var baeMap=L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);
var LayerList='{list:'+'{{layers}}'+',}'

// initiate the basemao and overlay layers in the controller
var baemap={'base':baeMap}
var overlayMaps = {};


// get the layer info from backend
var layerName=document.getElementById('layers').value
var geoLayers={{geolayers | safe}}
var lays='{{ layers | safe }}'

var temp = geoLayers[layerName]
if(!temp){
  {% for layer in layers%}
  var layName= '{{layer.name}}'
  var fetching=fetch('http://localhost/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName='+layName+'&maxFeatures=50&srsName=EPSG:4326&outputFormat=json')
                 .then(response => response.json())
                 .then(function(data){
                  geoLayers['{{layer.name}}']=data

                }).catch((error) => {
                    console.error('Error:', error);
                  });

{% endfor %}

window.onload = async () => {
    let someData = await fetching;
    console.log("onload");
};
}



function addLayer(temp){
  console.log(temp);
var geolayer= L.geoJSON(temp,{
  onEachFeature: onEachFeature
})
}

var attr1 = document.getElementById('attr1')
var attr2 = document.getElementById('attr2')
var attra=document.getElementsByClassName('attra')
var attrb=document.getElementsByClassName('attrb')

function addAttr(layerName){

  attr1.innerHTML=""
  attr2.innerHTML=""
  if (attra.length>0){
    for(j=0;j<attra.length;j++){
    attra[j].innerHTML=""
    attrb[j].innerHTML=""
  }
  }
  var activeLayer=geoLayers[layerName]
  // if(!activeLayer){
  //   fetch('http://localhost/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName='+layerName+'&maxFeatures=50&outputFormat=json')
  //                .then(response => response.json())
  //                .then(function(activeLayer){
  //                  var keyList=Object.keys(activeLayer.features[1].properties);
  //                  var items=""
  //                  for (let i=0;i<keyList.length;i++){
  //                      attr1.innerHTML  += "<option value="+keyList[i]+">"+keyList[i]+"{{item}}</option>"
  //                      attr2.innerHTML  += "<option value="+keyList[i]+">"+keyList[i]+"{{item}}</option>"
  //                      if (attra.length>0){
  //                      for(j=0;j<attra.length;j++){
  //                        attra[j].innerHTML  += "<option value="+keyList[i]+">"+keyList[i]+"{{item}}</option>"
  //                        attrb[j].innerHTML  += "<option value="+keyList[i]+">"+keyList[i]+"{{item}}</option>"
  //                      }
  //                      }
  //                  }
  //
  //                   });
  // }
  var keyList=Object.keys(activeLayer.features[1].properties);
  var items=""
  for (let i=0;i<keyList.length;i++){
      attr1.innerHTML  += "<option value="+keyList[i]+">"+keyList[i]+"{{item}}</option>"
      attr2.innerHTML  += "<option value="+keyList[i]+">"+keyList[i]+"{{item}}</option>"
      if (attra.length>0){
      for(j=0;j<attra.length;j++){
        attra[j].innerHTML  += "<option value="+keyList[i]+">"+keyList[i]+"{{item}}</option>"
        attrb[j].innerHTML  += "<option value="+keyList[i]+">"+keyList[i]+"{{item}}</option>"
      }
      }
  }


}






{% for layer in layers %}
overlayMaps[ '{{layer.name}}' ] =L.geoJSON(geoLayers[ '{{layer.name}}' ],  {
    onEachFeature:showFeatureInfo
  })
{% endfor %}
function showFeatureInfo(feature,layer){
  if (feature.properties ) {

      layer.bindPopup('<div>'+feature.id+'</div>'  );

  }
}



document.getElementById('layers').addEventListener('change',function(){

   layerName=document.getElementById('layers').value
   temp = geoLayers[layerName]
   console.log(temp);
    addLayer(temp)
    addAttr(layerName)
    b()
  }
  )


function b(){

  mymap.eachLayer(function(layer) {
     if (!!layer.toGeoJSON) {

       mymap.removeLayer(layer);
     }
    });
  var geolayer=L.geoJSON(temp,{
        onEachFeature: onEachFeature
      }).addTo(mymap);
    }


function formattingLayers(){
  if(attra.length>0){
    for (let j=0;j<attra.length;j++){
      document.getElementsByClassName('attra')[j].addEventListener('change',b)
      document.getElementsByClassName('attrb')[j].addEventListener('change',b)
      document.getElementsByClassName('colorpicker')[j].addEventListener('change',b)
      document.getElementsByClassName('result')[j].addEventListener('change',b)
      document.getElementsByClassName('attra')[j].style.display='none'
      document.getElementsByClassName('attrb')[j].style.display='none'
  }
}
}


document.getElementById('attr1').addEventListener('change',b)
document.getElementById('attr2').addEventListener('change',b)
document.getElementById('colorpicker').addEventListener('change',b)
document.getElementById('result').addEventListener('change',b)
//
function zoomTo(s){
  console.log(s.sourceTarget.feature);
  s.sourceTarget.feature.properties.STATE_NAME="Mohamed"
  console.log(s.sourceTarget.feature.geometry.coordinates[0]);
  mymap.fitBounds(s.sourceTarget.feature.geometry.coordinates[0])
  mymap.setMaxZoom(8);
console.log(  mymap.getBoundsZoom(s.sourceTarget.feature.geometry.coordinates[0]))

}
function highlightFeature(e) {
   var layer = e.target;
   latLong = []
    layer.feature.geometry.coordinates[0].forEach(function(locationArray){

          locationArray.forEach(function(location){

              latLong.push([location[1] , location[0]]);
          });
         });



         console.log("down",Epolygon);

         var Epolygon = L.polygon(latLong).addTo(mymap);
         console.log("Epolygon",Epolygon);
         // Epolygon.enableEdit();
         Epolygon.editing.enable();
         Epolygon.on('click',function(){
           console.log(Epolygon);
         })
         latLong = [];

}

var selectedFeature = null;
 var Epolygon =null;
function onEachFeature(feature, layer) {

      // editableLayers.addLayer(layer);


      // layer.on('click', function(e){
      //   if (e.target.feature.geometry.type=='MultiPolygon'){
      //   document.getElementById('featureTable').innerHTML=e.target.feature.properties['STATE_NAME']
      //   highlightFeature(e)
      //   }else{
      //
      //       if(selectedFeature)
      //            selectedFeature.editing.disable();
      //
      //       selectedFeature = e.target;
      //       e.target.editing.enable();
      //
      //     }
      //  });
     // document.getElementById('featureTable').innerHTML+='<div>' +'</div>'+
     //    '<button type="button" name="button" onclick="zoomTo('+layer+')" >ZoomTOFeatue</button>'

    // does this feature have a property named popupContent?
    // for states layer
    if (feature.geometry.type=='MultiPolygon'){
    if (feature.properties ) {
          layer.bindPopup('<div>'+feature.properties.mhfz+'</div>'+document.getElementById('attr1').value+":"
               +feature.properties[document.getElementById('attr1').value]
               +'<div>'+document.getElementById('attr2').value+":"+feature.properties[document.getElementById('attr2').value]+'</div>'
               +'<div>'+"percentage" +':'+100*(feature.properties[document.getElementById('attr1').value]/feature.properties[document.getElementById('attr2').value]).toFixed(4)+' % </div>'
      );

    }
    if (feature.properties && feature.properties[document.getElementById('attr1').value]/
    feature.properties[document.getElementById('attr2').value] > document.getElementById('result').value/100)
    {
        layer.setStyle({ fillColor :document.getElementById('colorpicker').value, opacity: 0.5, weight: 5 })
    }  else if (feature.properties) {

        layer.setStyle({fillColor :'green'})
    }
    if(attra.length>0){
      for(j=0;j<attra.length;j++){
       document.getElementsByClassName('attra')[j].value=document.getElementById('attr1').value
       document.getElementsByClassName('attrb')[j].value=document.getElementById('attr2').value
       if (feature.properties && feature.properties[document.getElementsByClassName('attra')[j].value]/
        feature.properties[document.getElementsByClassName('attrb')[j].value] > document.getElementsByClassName('result')[j].value/100)
        {
            layer.setStyle({ fillColor :document.getElementsByClassName('colorpicker')[j].value, opacity: 0.5, weight: 5 })
        }
      }
    }
                    }

  else if((feature.geometry.type=='MultiLineString')){
    // for other layersGeojson
    if (feature.properties ) {
          // console.log(feature.geometry.coordinates[0].length);
          layer.bindPopup('<div>'+ feature.properties.Markaz_Nam +" "+feature.properties.fid+'</div>'
                        +'<div>'+document.getElementById('attr1').value+':'+feature.properties[document.getElementById('attr1').value]+"</div>"
                        +'<div>'+document.getElementById('attr2').value+':'+feature.properties[document.getElementById('attr2').value]+"</div>"
                        +'<div>'+"percentage" +':'+100*(feature.properties[document.getElementById('attr1').value]/
                              feature.properties[document.getElementById('attr2').value]).toFixed(4)+' % </div>'
                      )




      }if (feature.properties && feature.properties[document.getElementById('attr1').value]
      /feature.properties[document.getElementById('attr2').value] > document.getElementById('result').value/100)
      {
           layer.setStyle({ stroke:true,color :document.getElementById('colorpicker').value, opacity: 0.7, weight: 5 })
      }
      if(attra.length>0){
        for(j=0;j<attra.length;j++){
             document.getElementsByClassName('attra')[j].value=document.getElementById('attr1').value
             document.getElementsByClassName('attrb')[j].value=document.getElementById('attr2').value
             if (feature.properties && feature.properties[document.getElementsByClassName('attra')[j].value]/
              feature.properties[document.getElementsByClassName('attrb')[j].value] > document.getElementsByClassName('result')[j].value/100)
              {
                  layer.setStyle({  stroke:true,color  :document.getElementsByClassName('colorpicker')[j].value, opacity: 0.5, weight: 5 })
              }
            }
          }



}
}
// function zoomTo(e){
//   console.log(e);
//   lalo = L.GeoJSON.coordsToLatLng(e[0])
//   mymap.setView(lalo, 18);
// }
// overlayMaps['statess']=layersGeojson
   // console.log(overlayMaps);
   L.control.layers( baemap,overlayMaps).addTo(mymap);
   // set parameters needed for GetFeatureInfo WMS request
   var sw = mymap.options.crs.project(mymap.getBounds().getSouthWest());
   var ne = mymap.options.crs.project(mymap.getBounds().getNorthEast());
   var BBOX = sw.x + "," + sw.y + "," + ne.x + "," + ne.y;
   var WIDTH = mymap.getSize().x;
   var HEIGHT = mymap.getSize().y;
   console.log(WIDTH,HEIGHT);
