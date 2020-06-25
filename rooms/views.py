# from math import ceil
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
# from django.urls import reverse
# from django.http import Http404
from django_countries import countries
from . import models, forms

# Create your views here.

# Django Class Based Views
class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    paginate_kwarg = "potato"
    context_object_name = "rooms"

    # django ListView, django DetailView etc have get_context_data, in which you can modify context you want to send to templates
    def get_context_data(self, *, object_list=None, **kwargs):
        # need to add "rooms" or "page_obj" which are added to context by ListView
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context

# Django Function Based Views
# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)
#     try:
#         rooms = paginator.page(int(page))
#         return render(request, "rooms/home.html", {
#             "page": rooms,
#         })
#     except EmptyPage:
#         rooms = paginator.page(1)
#         return redirect("/")

    # for pagination, get the page number from the request
    # for example, localhost:8000/?page=8
    # page = request.GET.get("page", 1)
    # page = int(page or 1)
    # page_size = 10
    # limit = page_size * page
    # offset = limit - page_size
    # all_rooms = models.Room.objects.all()[offset:limit]
    # page_count = ceil(models.Room.objects.count() / page_size)

    # # render function works on top of the HTTPResponse function.
    # # render function not only gives the http response but also compiles html file into python file and renders it
    # # context is how you send variable from view to template
    # return render(request, "rooms/home.html", context={
    #     "rooms": all_rooms,
    #     "page": page,
    #     "page_count": page_count,
    #     "page_range": range(1, page_count + 1),
    #     })


class RoomDetail(DetailView):

    """ RoomDetail definition  """

    model = models.Room
    # pk_url_kwarg = "potato"

# def room_detail(request, potato):
# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", context={
#             "room": room,
#         })
#     except models.Room.DoesNotExist:
#         # return redirect("")
#         # return redirect(reverse("core:home")
        
#         # only by raising Http404, django knows to render 404.html
#         raise Http404()

class SearchView(View):

    """ SearchView Definition """

    def get(self, request):
        country = request.GET.get("country")

        if country:
            form = forms.SearchForm(request.GET)

            if form.is_valid():
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city
                filter_args["country"] = country
                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price
                if guests is not None:
                    filter_args["guests__gte"] = guests
                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms
                if beds is not None:
                    filter_args["beds__gte"] = beds
                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True
                if superhost is True:
                    filter_args["host__superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity
                for facility in facilities:
                    filter_args["facilities"] = facility

                qs = models.Room.objects.filter(**filter_args).order_by("-created")
                paginator = Paginator(qs, 10, orphans=5)
                page = request.GET.get("page", 1)
                rooms = paginator.get_page(page)

                return render(request, "rooms/search.html", {"form": form, "rooms": rooms})
        else:
            form = forms.SearchForm()

            return render(request, "rooms/search.html", {"form": form})

# def search(request):
#     city = str.capitalize(request.GET.get("city", "Anywhere"))
#     country = request.GET.get("country", "KR")
#     room_type = int(request.GET.get("room_type", 0))
#     room_types = models.RoomType.objects.all()

#     price = int(request.GET.get("price", 0))
#     guests = int(request.GET.get("guests", 0))
#     bedrooms = int(request.GET.get("bedrooms", 0))
#     beds = int(request.GET.get("beds", 0))
#     baths = int(request.GET.get("baths", 0))

#     instant = bool(request.GET.get("instant", False))
#     superhost = bool(request.GET.get("superhost", False))

#     # for debugging in the server side
#     s_amenities = request.GET.getlist("amenities")
#     s_facilities = request.GET.getlist("facilities")
#     # # print(s_amenities, s_facilities)

#     form = {
#         "city": city,
#         "s_country": country,
#         "s_room_type": room_type,
#         "price": price,
#         "guests": guests,
#         "bedrooms": bedrooms,
#         "beds": beds,
#         "baths": baths,
#         "s_amenities": s_amenities,
#         "s_facilities": s_facilities,
#         "instant": instant,
#         "superhost": superhost,
#     }

#     room_types = models.RoomType.objects.all()
#     amenities = models.Amenity.objects.all()
#     facilities = models.Facility.objects.all()

#     choices = {
#         "countries": countries,
#         "room_types": room_types,
#         "amenities": amenities,
#         "facilities": facilities,
#     }

#     filter_args = {}

#     if city != "Anywhere":
#         # __startswith is django filter
#         filter_args["city__startswith"] = city
#     filter_args["country"] = country
#     if room_type != 0:
#         filter_args["room_type__pk"] = room_type

#     if price != 0:
#         filter_args["price__lte"] = price
#     if guests != 0:
#         filter_args["guests__gte"] = guests
#     if bedrooms != 0:
#         filter_args["bedrooms_gte"] = bedrooms
#     if beds != 0:
#         filter_args["beds__gte"] = beds
#     if baths != 0:
#         filter_args["baths__gte"] = baths
#     if instant is True:
#         filter_args["instant_book"] = True
#     if superhost is True:
#         filter_args["host__superhost"] = True

#     if len(s_amenities) > 0:
#         for s_amenity in s_amenities:
#             filter_args["amenities__pk"] = int(s_amenity)
#     if len(s_facilities) > 0:
#         for s_facility in s_facilities:
#             filter_args["facilities__pk"] = int(s_facility)

#     rooms = models.Room.objects.filter(**filter_args)


#     # ** means unpack dictionary
#     return render(request, "rooms/search.html", context={
#         **form, **choices,
#         "rooms": rooms,
#     })