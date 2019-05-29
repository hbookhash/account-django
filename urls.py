from django.conf.urls import url, include

# importing relative paths
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__))) # here account is the name of its containing parent
from .views import * 

urlpatterns = [
    # Email Sign-up ...
    url(r'^$', test),
]
