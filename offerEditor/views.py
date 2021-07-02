from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView ,ListView
from .models import *
# Create your views here.
def addOffer(request):
    if request.method=='POST':
        pass
    return render (request,'offerEditor/addOffer.html')

def updateOffer(request,pk):
    pass


def DeleteOffer(request,pk):
    pass


def acceptOffer(request,pk):
    pass

def rejectOffer(request,pk):
    pass


class OffersListView(ListView):
    model = Offer
    context_object_name = 'Offer_list'
    # queryset = Book.objects.filter(publisher__name='ACME Publishing')
    template_name = 'offerEditor/offer_list.html'

class offerDetailView(DetailView):
    model= Offer
    context_object_name = 'offer'
    template_name = 'offerEditor/offer_details.html'


# def showSubmittedOffers(request):
class SubmittedOffersListView(ListView):
    model = SubmittedForReview
    context_object_name = 'Submitted_Offer_list'
    template_name = 'offerEditor/Submitted_Offer_list.html'

# def submittedOfferDetails(request,pk):
class  SubmittedOfferDetailView(DetailView):
    model= SubmittedForReview
    context_object_name = 'Submitted_Offer'
    template_name = 'offerEditor/Submitted_Offer_details.html'

# def showAcceptedOffers(request):
class AcceptedListView(ListView):
    model = Acceptedlist
    context_object_name = 'Acceptedlist'
    template_name = 'offerEditor/Acceptedlist.html'

# def AcceptedOfferDetails(request,pk):
class  AcceptedOfferDetailView(DetailView):
    model= Acceptedlist
    context_object_name = 'Accepted_list_Offer'
    template_name = 'offerEditor/Accepted_list_Offer_details.html'
