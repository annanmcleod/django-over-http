from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

from app.forms import AddForm, AgeForm, HeyForm, OrderForm


def hey_views(request) -> HttpResponse:
    form = HeyForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data["name"]
        return render(request, "hey.html", {"form": form, "name": name})
    else:
        return render(request, "hey.html", {"form": form})


def how_old(request):
    form = AgeForm(request.GET)
    if form.is_valid():
        death = form.cleaned_data["death"]
        birth = form.cleaned_data["birth"]
        age = death - birth
        return render(
            request,
            "age.html",
            {"form": form, "death": death, "birth": birth, "age": age},
        )
    else:
        return render(request, "age.html", {"form": form})


def take_order(request):
    form = OrderForm(request.GET)
    if form.is_valid():
        bt = form.cleaned_data["bt"]
        ft = form.cleaned_data["ft"]
        dt = form.cleaned_data["dt"]
        total = (bt * 4.50) + (ft * 1.5) + (dt * 1)
        return render(
            request,
            "order.html",
            {"form": form, "bt": bt, "ft": ft, ",dt": dt, "total": total},
        )
    else:
        return render(request, "order.html", {"form": form})
