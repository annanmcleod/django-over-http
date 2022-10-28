from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("near-hundred/", near_hundred, name="near_hundred"),
    path("string-splosion/", string_splosion, name="string-splosion"),
    path("cat-dog/", cat_dog, name="cat-dog"),
    path("lone-sum/", lone_sum ,name="lone_sum"),
    path("admin/", admin.site.urls),
]
