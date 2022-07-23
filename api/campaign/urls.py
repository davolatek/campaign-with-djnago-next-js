from django.urls import path
from . import views

app_name = "campaign"

urlpatterns = [
    path('campaigns/', views.CampaignsListView.as_view(), name="campaign"),
    path('campaigns_details/<str:slug>/', views.CampaignsGenericView.as_view(), name="campaign_details"),
    path('subcribe/new/', views.SubscriptionListView.as_view(), name="subscription")
]
