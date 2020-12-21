MQKEY=Key='lYrP4vF3Uk5zgTiGGuEzQGwGIVDGuy24';
MQCONFIGNUMBER=1;
if(window.MQPROTOCOL===undefined){ MQPROTOCOL=window.location.protocol==='https:'?'https://':'http://'; }
MQPLATFORMSERVER=MQPROTOCOL+"www.mapquestapi.com";
MQSTATICSERVER="https://www.mapquestapi.com/staticmap/";
MQTRAFFSERVER=TRAFFSERVER="https://www.mapquestapi.com/traffic/";
MQROUTEURL="https://www.mapquestapi.com/directions/";
MQGEOCODEURL="https://www.mapquestapi.com/geocoding/";
MQNOMINATIMURL=MQPROTOCOL+"open.mapquestapi.com/";
MQSEARCHURL="https://www.mapquestapi.com/search/";
MQLONGURL=MQPLATFORMSERVER;
MQSMSURL=MQPLATFORMSERVER;
MQTOOLKIT_VERSION="v2.2".replace(/^v/, '');
MQCDN=MQIMAGEPATH="https://api-s.mqcdn.com/"+"sdk/leaflet/v2.2/";
MQCDNCOMMON="https://api-s.mqcdn.com/";
MQICONSERVER=ICONSERVER=MQPROTOCOL+'icons.mqcdn.com';
MQICONCDN=MQPROTOCOL+'api.mqcdn.com';
LOGSERVER=MQTILELOGGER="https://www.mapquestapi.com";
MQLOGURL="https://www.mapquestapi.com/logger/v1";
COVSERVER=MQCOPYRIGHT="https://tileproxy.cloud.mapquest.com";
MQCOPYRIGHT_PATH="/attribution";
MBMAP="https://{$hostrange}.tiles.mapbox.com/v4/mapquest.streets/{$z}/{$x}/{$y}.{$ext}?access_token=pk.eyJ1IjoibWFwcXVlc3QiLCJhIjoiY2Q2N2RlMmNhY2NiZTRkMzlmZjJmZDk0NWU0ZGJlNTMifQ.mPRiEubbajc6a5y9ISgydg";
MBHYB="https://{$hostrange}.tiles.mapbox.com/v4/mapquest.satellite/{$z}/{$x}/{$y}.{$ext}?access_token=pk.eyJ1IjoibWFwcXVlc3QiLCJhIjoiY2Q2N2RlMmNhY2NiZTRkMzlmZjJmZDk0NWU0ZGJlNTMifQ.mPRiEubbajc6a5y9ISgydg";
MBSAT="https://{$hostrange}.tiles.mapbox.com/v4/mapquest.satellitenolabels/{$z}/{$x}/{$y}.{$ext}?access_token=pk.eyJ1IjoibWFwcXVlc3QiLCJhIjoiY2Q2N2RlMmNhY2NiZTRkMzlmZjJmZDk0NWU0ZGJlNTMifQ.mPRiEubbajc6a5y9ISgydg";
MBLIGHT="https://{$hostrange}.tiles.mapbox.com/v4/mapquest.light/{$z}/{$x}/{$y}.{$ext}?access_token=pk.eyJ1IjoibWFwcXVlc3QiLCJhIjoiY2Q2N2RlMmNhY2NiZTRkMzlmZjJmZDk0NWU0ZGJlNTMifQ.mPRiEubbajc6a5y9ISgydg";
MBDARK="https://{$hostrange}.tiles.mapbox.com/v4/mapquest.dark/{$z}/{$x}/{$y}.{$ext}?access_token=pk.eyJ1IjoibWFwcXVlc3QiLCJhIjoiY2Q2N2RlMmNhY2NiZTRkMzlmZjJmZDk0NWU0ZGJlNTMifQ.mPRiEubbajc6a5y9ISgydg";
MBMAP_OPEN="https://{$hostrange}.tiles.mapbox.com/v4/mapquest.streets-mb/{$z}/{$x}/{$y}.{$ext}?access_token=pk.eyJ1IjoibWFwcXVlc3QiLCJhIjoiY2Q2N2RlMmNhY2NiZTRkMzlmZjJmZDk0NWU0ZGJlNTMifQ.mPRiEubbajc6a5y9ISgydg";
MBHYB_OPEN="https://{$hostrange}.tiles.mapbox.com/v4/mapquest.satellite-mb/{$z}/{$x}/{$y}.{$ext}?access_token=pk.eyJ1IjoibWFwcXVlc3QiLCJhIjoiY2Q2N2RlMmNhY2NiZTRkMzlmZjJmZDk0NWU0ZGJlNTMifQ.mPRiEubbajc6a5y9ISgydg";
MBLIGHT_OPEN="https://{$hostrange}.tiles.mapbox.com/v4/mapquest.light-mb/{$z}/{$x}/{$y}.{$ext}?access_token=pk.eyJ1IjoibWFwcXVlc3QiLCJhIjoiY2Q2N2RlMmNhY2NiZTRkMzlmZjJmZDk0NWU0ZGJlNTMifQ.mPRiEubbajc6a5y9ISgydg";
MBDARK_OPEN="https://{$hostrange}.tiles.mapbox.com/v4/mapquest.dark-mb/{$z}/{$x}/{$y}.{$ext}?access_token=pk.eyJ1IjoibWFwcXVlc3QiLCJhIjoiY2Q2N2RlMmNhY2NiZTRkMzlmZjJmZDk0NWU0ZGJlNTMifQ.mPRiEubbajc6a5y9ISgydg";
MBEXT="png";
MBTILEHI="4";
MBTILELO="1";
MBCOPYRIGHT="https://tileproxy.cloud.mapquest.com";
MBCOPYRIGHT_PATH="/attribution";
function $pv() {};  function $a() {};

/**
 * MapQuest tiled map toolkit.
 * Copyright 2014, MapQuest Inc.  All Rights Reserved.
 * Copying, reverse engineering, or modification is strictly prohibited.
 * v2.2
 */
MQ.Geocode=L.Class.extend({includes:L.Mixin.Events,options:{key:null,map:null,icon:null,mapFitBounds:true,maxResults:-1,bounds:null},initialize:function(B){L.setOptions(this,B);MQ.mapConfig.setAPIKey(this.options)},_getOptionParameters:function(){var E={};if(this.options.maxResults!=-1){E.maxResults=this.options.maxResults}if(this.options.bounds){var D=this.options.bounds.getNorthWest();var F=this.options.bounds.getSouthEast();E.boundingBox=D.lat+","+D.lng+","+F.lat+","+F.lng}return E},search:function(E){var H;var G={};G.options=this._getOptionParameters();if(Object.prototype.toString.call(E)==="[object Array]"){H="batch?key="+this.options.key;G.locations=E}else{H="address?key="+this.options.key;G.location=E}H+="&json="+MQ.util.stringifyJSON(G);var F=this;MQ.mapConfig.ready(function(){MQ.util.doJSONP(MQ.mapConfig.getConfig("geocodeAPI")+H,{},L.Util.bind(F._onResult,F))});return this},reverse:function(E){var D="reverse?key="+this.options.key;D+="&lat="+E.lat+"&lng="+E.lng;var F=this;MQ.mapConfig.ready(function(){MQ.util.doJSONP(MQ.mapConfig.getConfig("geocodeAPI")+D,{},L.Util.bind(F._onResult,F))});return this},_onResult:function(O){if(O&&O.info&&O.info.statuscode==0&&O.results){var I=[];for(var M=0;M<O.results.length;M++){var H=O.results[M].locations;for(var N=0;N<H.length;N++){H[N].latlng=new L.LatLng(H[N].latLng.lat,H[N].latLng.lng);delete H[N].latLng}var J={best:H[0],matches:H};if(O.results[M].providedLocation.location){J.search=O.results[M].providedLocation.location}else{if(O.results[M].providedLocation.json){J.search=O.results[M].providedLocation.json}else{if(O.results[M].providedLocation.street){J.search=O.results[M].providedLocation.street}else{J.search=O.results[M].providedLocation}}}I.push(J)}if(this.options.map){this._placeOnMap(I)}if(I.length==1){this.fire("success",{result:I[0],data:O})}else{this.fire("success",{result:I,data:O})}}else{var K=null;if(O&&O.info){K={code:O.info.statuscode};if(O.info.messages&&O.info.messages.length>0){K.message=O.info.messages[0]}}this.fire("error",K)}},_placeOnMap:function(M){var K=(this.options.map.getZoom()!==undefined)?this.options.bounds||this.options.map.getBounds():null;var J={};if(this.options.icon){J.icon=this.options.icon}for(var N=0;N<M.length;N++){var I=L.marker(M[N].best.latlng,J).addTo(this.options.map);I.bindPopup(this.describeLocation(M[N].best));if(this.options.mapFitBounds){if(K){K.extend(M[N].best.latlng)}else{var O=0.01;var P=new L.LatLng(M[N].best.latlng.lat-O,M[N].best.latlng.lng-O);var Q=new L.LatLng(M[N].best.latlng.lat+O,M[N].best.latlng.lng+O);K=new L.LatLngBounds(P,Q)}}}if(this.options.mapFitBounds&&K){this.options.map.fitBounds(K)}},describeLocation:function(C){var D="";if(C.street){D+=C.street+"<br/>"}if(C.adminArea5){if(C.adminArea3){D+=C.adminArea5+", "+C.adminArea3+"<br/>"}else{D+=C.adminArea5+"<br/>"}}else{if(C.adminArea3){D+=C.adminArea3+"<br/>"}}return D}});MQ.geocode=function(B){if(B==null){B={}}if(!B.key&&MQKEY){B.key=MQKEY}if(B.icon==null){B.icon=L.icon({iconUrl:MQ.mapConfig.getConfig("imagePath")+"poi.png",iconRetinaUrl:MQ.mapConfig.getConfig("imagePath")+"poi@2x.png",iconSize:[36,35],iconAnchor:[15,35],popupAnchor:[-1,-30]})}return new MQ.Geocode(B)};
