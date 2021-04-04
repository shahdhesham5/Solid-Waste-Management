# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.conf.urls import url, include
from django.views.generic import TemplateView

from geonode.urls import urlpatterns
from geonode.monitoring import register_url_event
from django.urls import path
from main import views as main
urlpatterns += [
 url(r'^main/?$', main.main, name='main'),
]

from da import views as dd
urlpatterns += [
    path("dd",dd.index,name='dd'),
    path("ddd",dd.index2,name='ddd'),

     path('apii/',include('apii.urls')),
     path("geoleaflet",include('geoleaflet.urls')),
     path("Learning",include('Learning.urls')),

]


from sw import views as views
urlpatterns += [
## include your urls here
url(r'^new/?$', views.index, name='new'),
 url(r'^dashboard/?$', views.dashboard, name='dashboard'),
   url(r'^swmap/?$', views.map, name='mapexample'),
   url(r'^database/?$', views.database, name='database'),
   url(r'^ads/?$', views.ads, name='ads'),
   url(r'^properties/?$', views.properties, name='properties'),
   url(r'^data/?$', views.data, name='data'),
   url(r'^historical/?$', views.historical, name='historical'),
   url(r'^public/?$', views.public, name='public'),
   url(r'^swm/?$', views.swm, name='swm'),
   url(r'^test/?$', views.test, name='test'),
   url(r'^signup/?$', views.signup, name='signup'),
   url(r'^login/?$', views.login, name='login')

]

homepage = register_url_event()(TemplateView.as_view(template_name='site_index.html'))

urlpatterns = [
    url(r'^gig/?$',
        homepage,
        name='home'),
 ] + urlpatterns
