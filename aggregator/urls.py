from django.urls import path

from aggregator.views import AggrecateVievs

app_name = 'aggregator'

urlpatterns = [
    path("", AggrecateVievs.as_view(), name="aggregate"),
]