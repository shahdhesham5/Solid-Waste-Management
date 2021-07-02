import json
import os
from datetime import datetime

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin



class IDSCAdmin(LoginRequiredMixin,View):

    def get(self, request):
        # if not request.user.is_authenticated:
        #     return redirect('login')
        #
        return render(request, 'demos/demos/idsc_admin.html')







class GeoJSON(View):
    points_path = os.path.join(settings.LOCAL_ROOT, 'static', 'demos','json', 'points.geojson')
    poly_path = os.path.join(settings.LOCAL_ROOT, 'static', 'demos','json', 'poly.geojson')

    def get(self, request):
        with open(self.points_path, 'r') as points:
            obj = json.load(points)
            return JsonResponse(obj, safe=False)

    def post(self, request):
        changed = json.loads(request.POST['changed'])
        features = {}

        # Get the features from the GeoJSON file
        points_obj = {}
        with open(self.points_path, 'r') as points:
            points_obj = json.load(points)
            features = points_obj['features']

        # Adjust the features obj
        for index, feature in enumerate(features):
            if feature['properties']['GOV_CODE'] in changed.keys():
                feature['properties']['Confirmed_'] = changed[feature['properties']['GOV_CODE']]['Confirmed_']
                feature['properties']['Recovered'] = changed[feature['properties']['GOV_CODE']]['Recovered']
                feature['properties']['Deathes'] = changed[feature['properties']['GOV_CODE']]['Deathes']

        points_obj['features'] = features

        with open(self.points_path, 'w') as points:
            points.write(json.dumps(points_obj))
        return JsonResponse({'res': 'success'}, safe=False)


class Timeseries(LoginRequiredMixin,View):
    points_path = os.path.join(settings.LOCAL_ROOT, 'static', 'demos','json', 'points.geojson')
    timeseries_file = os.path.join(settings.LOCAL_ROOT, 'static','demos', 'json', 'timeseries.json')

    def get(self, request):
        with open(self.timeseries_file, 'r') as timeseries:
            return JsonResponse(json.loads(timeseries.read()), safe=False)


    def post(self, request):
        diff = json.loads(request.POST['diff'])

        with open(self.timeseries_file, 'r') as timeseries:
            data = json.load(timeseries)
            timestamp = datetime.timestamp(datetime.now())

            record = {}

            # add just last records
            last_record = data['timeseries'][-1]
            if data['timeseries'] and datetime.fromtimestamp(last_record['date']).date() == datetime.today().date():
                record = {'date': timestamp, 'infected': last_record['infected'] + diff['infected'], 'recovered': last_record['recovered'] + diff['recovered'], 'death': last_record['death'] + diff['death']}
                data['timeseries'].pop(-1)
            else:
                record = {'date': timestamp, 'infected': diff['infected'], 'recovered': diff['recovered'], 'death': diff['death']}

            data['timeseries'].append(record)

        with open(self.timeseries_file, 'w') as timeseries:
            timeseries.write(json.dumps(data))

        return JsonResponse({'code': 'ok'}, safe=False)


class Hospital(View):
    hospitals_path = os.path.join(settings.LOCAL_ROOT, 'static','demos', 'json', 'hospitals')

    def get(self, request):
        data = {}
        for file in os.listdir(self.hospitals_path):
            fn, fx = os.path.splitext(file)
            with open(os.path.join(self.hospitals_path, file), 'r', encoding='utf-8') as content:
                data[fn] = json.load(content)
        return JsonResponse({'data': data}, safe=False)


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
