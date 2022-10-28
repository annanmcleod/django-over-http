from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

from app.forms import CatForm, LoneForm, NearForm, StringForm


def near_hundred(request):
    form = NearForm(request.GET)
    if form.is_valid():
        n = form.cleaned_data["n"]
        if (abs(100 - n) <= 10) or (abs(200 - n) <= 10):
            # return HttpResponse(True)
            return render(request, "near.html", {"form": form, "n": n})
        
        return render(request, "near.html", {"form": form})   
    else:
        return render(request, "near.html", {"form": form})


def string_splosion(request):
    form = StringForm(request.GET)
    if form.is_valid():
        str = form.cleaned_data["str"]
        result = ""
        for i in range(len(str)):
            result = result + str[: i + 1]
        return render(request, "string.html", {"form": form, "result": result})
    else:
        return render(request, "string.html", {"form": form})


def cat_dog(request):
    form = CatForm(request.GET)
    if form.is_valid():
        str = form.cleaned_data["str"]
        return render(request, "cat.html", {"form": form, "str": str})
        # return HttpResponse(str.count("cat") == str.count("dog"))
    else:
        return render(request, "cat.html", {"form": form})


def lone_sum(request):
    form = LoneForm(request.GET)
    if form.is_valid():
        a = form.cleaned_data["a"]
        b = form.cleaned_data["b"]
        c = form.cleaned_data["c"]
        if a == b and a == c and b == c:
            result = 0
            return render(request, "lone.html", {"form": form, "result": result})
        elif a == b:
            result = c
            return render(request, "lone.html", {"form": form, "result": result})
        elif b == c:
            result = a
            return render(request, "lone.html", {"form": form, "result": result})
        elif c == a:
            result = b
            return render(request, "lone.html", {"form": form, "result": result})

        result = a + b + c
        return render(request, "lone.html", {"form": form, "result": result})

    else:
        return render(request, "lone.html", {"form": form})
