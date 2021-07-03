from django.urls import path, include
from file_conversion_log.api.views import log_list

urlpatterns = [
    path('names/', log_list, name='names'),
]