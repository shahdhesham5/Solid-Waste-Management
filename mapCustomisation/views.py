from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from geoserver.catalog import Catalog
from geonode.geoserver.helpers import  gs_catalog
from geonode.geoserver.helpers import (ogc_server_settings,
                                       set_layer_style)
from django.conf import settings
from owslib.wfs import WebFeatureService
import geoserver.util
import json
import base64
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import urllib
from django.core import serializers

from .models import *
from geonode.layers import models as m
from geonode.layers.views import *
from django.http import JsonResponse


from django.contrib.auth import get_user_model
User = get_user_model()


baseURL = "http://localhost/geoserver/gwc/rest/seed/"
descURL = "https://localhost/geoserver/gwc/rest/layers/"

un = 'admin'
pw = 'geoserver'
# url='http://localhost/geoserver/wfs?request=GetFeature&service=WFS&version=1.0.0&typeName='+geonode:states+'&outputFormat=application/json'

def recieve(request):
    data=json.loads(request.body)
    try:
        x=editedLyr.objects.get(name=data['name'] , editor=request.user.editor)
        x.layer=data['layer']
        x.save()
        msg='edited'
    except:
        Layer=editedLyr()
        Layer.name=data['name']
        Layer.layer=data['layer']
        print("the error belwo me")
        Layer.editor = request.user.editor
        Layer.save()
        msg='created'

    context={
        'msg':msg
    }
    return JsonResponse(context)





def AcceptLayer(request):
    data=json.loads(request.body)
    try:
        x=AcceptedLyr.objects.get(name=data['name'])
        x.layer=data['layer']
        x.save()
    except:
        Layer=AcceptedLyr()
        Layer.name=data['name']
        Layer.layer=data['layer']
        Layer.editor = Editor.objects.get(user__username=data['user_name'])
        Layer.superviser = request.user.superviser
        Layer.save()
    #deleting it from edited layers
    y=editedLyr.objects.get(name=data['name'] , editor=Editor.objects.get(user__username=data['user_name']) )
    y.delete()
    layEdited=editedLyr.objects.all()
    layers=[]
    for layer in layEdited:
        layers.append({'{} by: {}'.format(layer.name,layer.editor):layer.layer})
    context={
        'layers':layers
    }
    return  JsonResponse(context)



def RejectedEdits(request):
    data=json.loads(request.body)
    try:
        x=RejectedLyr.objects.get(name=data['name'], editor=Editor.objects.get(user__username=data['user_name']))
        x.layer=data['layer']
        x.save()
        msg='Not the first time to be rejected from the same user'
    except:
        Layer=RejectedLyr()
        Layer.name=data['name']
        Layer.layer=data['layer']
        Layer.editor = Editor.objects.get(user__username=data['user_name'])
        Layer.note = data['note']
        Layer.superviser = request.user.superviser
        Layer.save()
        msg='first time to be rejected from this user'
    #deleting it from edited layers
    try:
        current_editor=Editor.objects.get(user__username=data['user_name'])
        y=editedLyr.objects.get(name=data['name'] , editor=current_editor)
    except:
        prev_editor=Editor.objects.get(user__username=data['prev_user'])
        y=editedLyr.objects.get(name=data['name'] , editor=prev_editor)
    y.delete()
    layEdited=editedLyr.objects.all()
    layers=[]
    for layer in layEdited:
        layers.append({'{} by: {}'.format(layer.name,layer.editor):layer.layer})
    context={
        'layers':layers,
        'msg':msg
    }
    return  JsonResponse(context)


@login_required
def assignEdit(request):
    print (request.user)
    try:
        data=RejectedLyr.objects.filter(editor=request.user.editor)
        layers=[]
        for layer in data:
            layers.append({layer.name+' by: '+ layer.editor.user.username:layer.layer })
    except:
        layers=[]
    context={
        'layers':json.dumps(layers)
        }
    return render(request,'da/rejectedandassignedLayers.html',context)


def resubmitedLayers(request):
    data=json.loads(request.body)
    try:
        x=editedLyr.objects.get(name=data['name'] , editor=request.user.editor)
        x.layer=data['layer']
        x.save()
        msg='edited'
    except:
        Layer=editedLyr()
        Layer.name=data['name']
        Layer.layer=data['layer']
        Layer.editor = request.user.editor
        Layer.save()
        msg='created'
    y=RejectedLyr.objects.get(name=data['name'] , editor=request.user.editor)
    y.delete()
    rest_data=RejectedLyr.objects.filter(editor=request.user.editor)
    layers=[]
    for layer in rest_data:
        layers.append({layer.name+' by: '+ layer.editor.user.username:layer.layer })
    context={
        'layers':layers,
        }
    return JsonResponse(context)









def Layers_Edited(request):
    users= User.objects.exclude(username='AnonymousUser')
    try:
        if(request.user.superviser ):
            data = editedLyr.objects.all()
            layers=[]
            # cat2= gs_catalog
            #    cat = Catalog("http://localhost/geoserver/rest/", username="admin", password="geoserver")
            for layer in data:
                layers.append({layer.name+' by: '+ layer.editor.user.username:layer.layer })
                # xlayer = cat.get_layer(layer.name)
                # topp = cat.get_workspace("geonode")
                # ds=cat.get_stores()[0]
                #    new_source=ds.get_resources()[1]
                #    xlayer.set_resource=new_source
                # cat.save(xlayer)
                # cat.reload()

            context={
                    'layers':json.dumps(layers),
                        'users':users
                    }
            return render(request,'da/LayersEdited.html',context)
    except:
        ## TODO: prepare un authorized page
        return HttpResponse('No')








def index2(request):
    # url='http://localhost/geoserver/wfs?request=GetFeature&service=WFS&version=1.0.0&typeName='+that_layer.name+'&outputFormat=application/json'
    # curl -X PUT http://localhost/geoserver/rest/layers/geonode%3Aline_water -H  "accept: application/json" -H  "content-type: application/xml" -d "<?xml version=\"1.0\" encoding=\"UTF-8\"?><layer>\t<name>string</name>\t<path>string</path>\t<type>VECTOR</type>\t<defaultStyle>\t\t<name>string</name>\t</defaultStyle>\t<styles>\t\t<@class>linked-hash-set</@class>\t\t<style>\t\t\t<name>string</name>\t\t</style>\t</styles>\t<resource>\t\t<@class>featureType</@class>\t\t<name>string</name>\t</resource>\t<opaque>true</opaque>\t<metadata>\t\t<@key>buffer</@key>\t\t<$>string</$>\t</metadata>\t<attribution>\t\t<title>string</title>\t\t<href>string</href>\t\t<logoURL>string</logoURL>\t\t<logoWidth>0</logoWidth>\t\t<logoHeight>0</logoHeight>\t\t<logoType>string</logoType>\t</attribution>\t<authorityURLs>\t\t<name>string</name>\t\t<href>string</href>\t</authorityURLs>\t<identifiers>\t\t<authority>string</authority>\t\t<identifier>string</identifier>\t</identifiers></layer>"
    return HttpResponse('k')




import requests

@login_required
def index(request):
    cat = Catalog("http://localhost/geoserver/rest/", username="admin", password="geoserver")
    cat2= gs_catalog
    # shapefile_plus_sidecars = geoserver.util.shapefile_and_friends('cat.get_layer("states")')
    # myResource = cat.get_resources()
    try:
        all_layers = cat.get_layers()
    except:
        # layersFromJson=requests.get('http://localhost/geoserver/rest/layers/').json()
        cat2= gs_catalog
        all_layers = cat2.get_layers()
        # return HttpResponse(all_layers[0])

        # print(layersFromJson)
        # all_layers= layersFromJson.layers.layer
    layers={}
    for layer in all_layers:
        try:
            jsonLayer=(requests.get('http://localhost/geoserver/wfs?request=GetFeature&service=WFS&version=1.0.0&typeName='+layer.name+'&srsName=EPSG:4326&outputFormat=application/json').json())
        except:
            continue
            context_dict = {}
            bb = cat2.get_layer(layer.name)
            x = bb.read()
            x = json.loads(x)
            data_dict = layer.name#json.loads(request.POST.get('json_data'))
            layername = layer.name
            filtered_attributes = ''
            if not isinstance(data_dict['filtered_attributes'], string_types):
                filtered_attributes = [x for x in data_dict['filtered_attributes'] if '/load_layer_data' not in x]
            name = layername if ':' not in layername else layername.split(':')[1]
            location = "{location}{service}".format(** {
                'location': settings.OGC_SERVER['default']['LOCATION'],
                'service': 'wms',
            })
            access_token = None
            if request and 'access_token' in request.session:
                access_token = request.session['access_token']
            if access_token and 'access_token' not in location:
                location = '%s?access_token=%s' % (location, access_token)
            try:
                wfs = WebFeatureService(
                    location,
                    version='1.1.0')
                response = wfs.getfeature(
                    typename=layername,
                    outputFormat='application/json')
                return HttpResponse("No")

                x = response.read()
                x = json.loads(x)

                features_response = json.dumps(x)
                decoded = json.loads(features_response)

                decoded_features = decoded['features']
                properties = {}
                for key in decoded_features[0]['properties']:
                    properties[key] = []

                # loop the dictionary based on the values on the list and add the properties
                # in the dictionary (if doesn't exist) together with the value
                from collections.abc import Iterable
                for i in range(len(decoded_features)):
                    for key, value in decoded_features[i]['properties'].items():
                        if value != '' and isinstance(value, (string_types, int, float)) and (
                                (isinstance(value, Iterable) and '/load_layer_data' not in value) or value):
                            properties[key].append(value)

                for key in properties:
                    properties[key] = list(set(properties[key]))
                    properties[key].sort()

                context_dict["feature_properties"] = properties
            except Exception:
                x=1
                traceback.print_exc()
                logger.error("Possible error with OWSLib.")

            jsonLayer=x
            #
            #json.dumps(context_dict)
            # continue
        layers[layer.name]=jsonLayer



    # that_layer = cat2.get_layer("states")
    # print(type(that_layer))
    # resource = that_layer.resource#cat.get_resource(that_layer.name)


    # print("sddd",resource.keys())
    # resource = that_layer.resource
    # url='http://localhost/geoserver/wfs?request=GetFeature&service=WFS&version=1.0.0&typeName=states&srsName=EPSG:4326&outputFormat=application/json'
    url='http://localhost/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:states&maxFeatures=50&outputFormat=json'
    # response = requests.get(url)
    # data = json.loads(response.read())
    # r = requests.get(url)
    # geoJsonLayer=r.json()

    # print(layers.keys())
    # print ([method for method in dir(that_layer) if callable(getattr(that_layer, method))])
    # layerrrrrrrr dict_keys(['dom', 'dirty', 'catalog', 'name', 'gs_version'])
# ['__class__', '__delattr__', '__dir__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__'
#  , '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__'
#  , '__str__', '__subclasshook__', '_get_alternate_styles', '_get_attr_attribution', '_get_default_style', '_resolve_style', '_set_alternate_styles'
#  , '_set_attr_attribution', '_set_default_style', 'clear', 'fetch', 'message', 'refresh', 'serialize']

    # print (that_layer.dom.__dict__.keys())



    context={
        # "layerw":that_layer,
        "layers":all_layers,
        # "shape":shapefile_plus_sidecars['shp'],
        "link":url,
        # "layersGeojson":geoJsonLayer,
        'url':url,
        'geolayers':json.dumps(layers)
    }

    return render(request,'da/index.html',context)

#first feature of the shapefile
