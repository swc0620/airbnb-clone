# from math import ceil
# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView, DetailView
from django.utils import timezone
# from django.urls import reverse
# from django.http import Http404
from . import models

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