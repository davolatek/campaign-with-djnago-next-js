from rest_framework import serializers
from .models import Campaigns, Subcription

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaigns
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcription
        fields = "__all__"