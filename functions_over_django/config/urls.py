from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    # path("", root, name="root"),
    path("hey/", hey_views, name="hey_views"),
    path("age/", how_old, name="how_old"),
    path("order/", take_order, name="take_order"),
    path("admin/", admin.site.urls),
]

