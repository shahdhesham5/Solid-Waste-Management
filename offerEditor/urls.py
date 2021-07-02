from django.urls import path
from .views import *


urlpatterns=[
    # add & update & DeleteOffer
    path('addOffer',addOffer,name='addOffer'),
    path('updateOffer/<int:pk>',updateOffer,name='updateOffer'),
    path('DeleteOffer/<int:pk>',DeleteOffer,name='DeleteOffer'),


    # move them to accepted or send them back to offers
    path('acceptOffer/<int:pk>',acceptOffer,name='acceptOffer'),
    path('rejectOffer/<int:pk>',rejectOffer,name='rejectOffer'),


    # show list from models
    path('OffersListView',OffersListView.as_view(),name='OffersListView'),
    path('offerDetailView/<int:pk>',offerDetailView.as_view(),name='offerDetailView'),
    path('SubmittedOffersListView',SubmittedOffersListView.as_view(),name='SubmittedOffersListView'),
    path('SubmittedOfferDetailView/<int:pk>',SubmittedOfferDetailView.as_view(),name='SubmittedOfferDetailView'),
    path('AcceptedListView',AcceptedListView.as_view(),name='AcceptedListView'),
    path('AcceptedOfferDetailView/<int:pk>',AcceptedOfferDetailView.as_view(),name='AcceptedOfferDetailView'),
]
