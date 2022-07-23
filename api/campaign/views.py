from django.shortcuts import render
from rest_framework import generics, response, status
from .models import Campaigns, Subcription
from .serializer import CampaignSerializer, SubscriptionSerializer

# Create your views here.

class CampaignsListView(generics.ListAPIView):
    def get_queryset(self):
        return Campaigns.objects.all()

    serializer_class = CampaignSerializer


class CampaignsGenericView(generics.GenericAPIView):
    serializer_class = CampaignSerializer
    def get(self, request, slug):
        
        query_set = Campaigns.objects.filter(slug = slug).first()

        if query_set:
            return response.Response(self.serializer_class(query_set).data)

        else:
            return response.Response("Not found", status=status.HTTP_404_NOT_FOUND)



class SubscriptionListView(generics.CreateAPIView):
    def get_queryset(self):
        return Subcription.objects.all()

    serializer_class = SubscriptionSerializer
    
    