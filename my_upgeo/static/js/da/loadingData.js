//The Editing part
  function loadingData(){
    var layerToEditm= geoLayers[document.getElementById('layersToEdit').value];
    //get copy of layer
    var layerToEdit={
      ...layerToEditm
    }
    function getFeatureEdited(feature,layer){

      layer.on('click',function(){
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
  mymap.fitBounds(L.geoJson(layerToEdit).getBounds());
  var myFeature=L.geoJSON(layerToEdit,{
      onEachFeature:getFeatureEdited
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
    var AddedFeatures={}
    //Add New Feature
    document.getElementById('addFeature').addEventListener('click',xc)
    function xc(){
      document.getElementById('mydiv').style.display='block'
      var oldFeature=layerToEdit.features[0]
      var newFeature=  JSON.parse(JSON.stringify(oldFeature));
      document.getElementById('movingTable').innerHTML=''
      var Thead="<tr >"
      for (key in attributes){
        Thead+='<th>'+attributes[key]+'</th>'
        '<tr>'+attrValues[attributes[key]]+'</tr>'
      }
      Thead+="</tr>"
      var feat='<tr>'
      for (key in attributes){
            feat+='<td> <input class="newInputs" type="'+typeof(oldFeature.properties[attributes[key]])+'" data="" value="" /> </td>'
            }
        feat +='</tr>'
     document.getElementById('movingTable').innerHTML+='<table >'+Thead+feat+'</table>'
     document.getElementById('mydiv2').innerHTML='<button type="button" id="draw"name="button">Add Polygon</button>'
     if(newFeature.geometry.type=="MultiLineString"){
       document.getElementById('draw').innerHTML="Add PolyLine"
     }
     document.getElementById('draw').addEventListener('click',function(){
       if(newFeature.geometry.type=="MultiPolygon"){
      mymap.editTools.stopDrawing()
          mymap.editTools.startPolygon();
        }else{
          document.getElementById('draw').innerHTML="Add PolyLine"
           mymap.editTools.startPolyline()

        }
          newFeature.geometry.coordinates[0]=[[],]
          let coordinates=[]

        mymap.on('editable:drawing:end',function xyz(e){
            coordinates=[...e.layer._latlngs]
            //get coordinates of drawn layer and make it suitable to add to the real layer
            if(newFeature.geometry.type=="MultiPolygon"){
            for (let k=0;k<coordinates[0].length;k++){
                  newFeature.geometry.coordinates[0][0].push([parseFloat(coordinates[0][k].lng.toFixed(6)),parseFloat(coordinates[0][k].lat.toFixed(6))])
            }
          }else{
            newFeature.geometry.coordinates[0]=[]
            for (let k=0;k<coordinates.length;k++){
                  newFeature.geometry.coordinates[0].push([parseFloat(coordinates[k].lng.toFixed(6)),parseFloat(coordinates[k].lat.toFixed(6))])
            }
          }
            for(let i=0;i<attributes.length;i++){
              if(typeof(oldFeature.properties[attributes[i]])=='string'){
              newFeature.properties[attributes[i]]=document.getElementsByClassName('newInputs')[i].value
            }else{
              newFeature.properties[attributes[i]]=parseFloat(document.getElementsByClassName('newInputs')[i].value)
            }

            }

            mymap.editTools.stopDrawing()

            cNewFeature=JSON.parse(JSON.stringify(newFeature))
            layerToEdit.features.push(cNewFeature)
            var addfeat='<tr>'
            for (key in attributes){
                addfeat+='<td> <input class="inputs" type="text" data="'+cNewFeature+'" value='+cNewFeature.properties[attributes[key]]+' /> </td>'
                  }
              addfeat +='</tr>'
            document.getElementById('Table').innerHTML+=addfeat

            mymap.off('editable:drawing:end',xyz)
            document.getElementById('mydiv').style.display='none'
            // mymap.eachLayer(function(layer) {
              //           if (!!layer.toGeoJSON) {
              //                mymap.removeLayer(layer);
              //           }
              //
              //            });

            clearToRedraw()
            loadingData()
             L.geoJSON(layerToEdit,{
                    onEachFeature:getFeatureEdited
                  }).addTo(mymap)


          })
        })
    }
    // delet
    document.getElementById('delFeature').addEventListener('click',function(){
      document.getElementById('delFeature').style.background='red'
    clearToRedraw()


      L.geoJSON(layerToEdit,{
             onEachFeature:(feature,layer)=>{
               layer.on('click',function(e){
                 console.log(e.target.feature);
                 layer.remove(e.target.feature)
                 let arr=layerToEdit.features
                  for( var i = 0; i < arr.length; i++){
                    if ( arr[i] === e.target.feature) {
                       arr.splice(i, 1);
                    }
                  }
                  loadingData()
                  document.getElementById('delFeature').style.backgroundImage='linear-gradient(  #bbd2c5, #536976,#292e49  )';
                 console.log(layerToEdit);
               })
             }
           }).addTo(mymap)

    })
    // console.log("kj",inputs.length);
  function Misk(){
    var inputs=document.getElementsByClassName('inputs')
    for (let i=0;i<inputs.length;i++){
       inputs[i].addEventListener('change',function xx(e){
          //get the edited attribute
          var EditedAttr=attributes[i%attributes.length];
          var EFeature=layerFeatures[this.attributes.data.value]
          if(typeof(layerFeatures[this.attributes.data.value].properties[EditedAttr])=='number'){
              layerFeatures[this.attributes.data.value].properties[EditedAttr]=parseFloat(inputs[i].value)
          }else{
              layerFeatures[this.attributes.data.value].properties[EditedAttr]=inputs[i].value
          }
       latLong = []
           // mymap.removeLayer(myFeature)
           if (layerFeatures[this.attributes.data.value].geometry.type=='MultiPolygon'){
             layerFeatures[this.attributes.data.value].geometry.coordinates[0].forEach(function(locationArray){
                    locationArray.forEach(function(location){
                        latLong.push([location[1] , location[0]]);
                    });
                   });
              var Epolygon = L.polygon(latLong,{
               style:{fillColor:'red'}
             }).addTo(mymap);
                }else{
                  // latLong=layerFeatures[this.attributes.data.value].geometry.coordinates[0]
                  console.log('important',layerFeatures[this.attributes.data.value].geometry.coordinates[0]);
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
               if(EFeature.geometry.type=='MultiPolygon'){
                 EFeature.geometry.coordinates[0][0]=[]
                 for(let i=0;i<Epolygon._latlngs[0].length;i++){
                   EFeature.geometry.coordinates[0][0].push([Epolygon._latlngs[0][i].lng,Epolygon._latlngs[0][i].lat])
                      }
                    }else{
                        EFeature.geometry.coordinates[0]=[]
                        for(let i=0;i<Epolygon._latlngs.length;i++){
                            EFeature.geometry.coordinates[0].push([Epolygon._latlngs[i].lng,Epolygon._latlngs[i].lat])
                            }

                            }

              console.log(',,,,',layerToEdit)
              // mymap.eachLayer(function(layer) {
              //  if (!!layer.toGeoJSON) {
              //    mymap.removeLayer(layer);
              //
              //  }
              //
              //
              // });
              clearToRedraw()



              L.geoJSON(layerToEdit,{
                onEachFeature:getFeatureEdited
              }).addTo(mymap)


                   })
             latLong = [];


      })
    }

}
Misk()
document.getElementById('postFeature').addEventListener('click',function(){
  fetch("{% url 'recieve' %}", {
  method: 'POST', // or 'PUT'
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrftoken,
          },
          body: JSON.stringify(layerToEdit),
        })
        .then(response => response.json())
        .then(data => {
          console.log('Success:', data);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
})
  }
