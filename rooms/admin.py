from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    
    """ Item Admin Definition """
    
    list_display = (
        "name",
        "used_by"
    )

    def used_by(self, obj):
        return obj.rooms.count()

# Django reads the ForeignKey relations and allows you to have administration of Photo inside Room.
class PhotoInLine(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    
    """ Room Admin Definition """
    
    inlines = (PhotoInLine,)

    # admin에 소제목을 달아준다
    fieldsets = (
        (
            "Basic Info",
            {"fields": ["name", "description", "country", "address", "price"]}
        ),
        (
            "Times",
            {"fields": ["check_in", "check_out", "instant_book"]}
        ),
        (
            "Spaces",
            {"fields": ["guests", "beds", "bedrooms", "baths"]}
        ),
        (
            "More About the Space",
            {
                # 소제목을 접었다 폈다 할 수 있다
                "classes" : ["collapse", ],
                "fields": ["amenities", "facilities", "house_rules"]
            }
        ),
        (
            "Last Details",
            {"fields": ["host"]}
        )
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    ordering = (
        "name",
        "price",
        "bedrooms"
    )

    # __ is how you access foreignkey
    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        'amenities',
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    # raw id fields helps you to search something when there are too many data
    raw_id_fields = ("host",)

    # default = icontains, ^ = starts with, = = exact
    search_fields = ["=city", "^host__username"]

    filter_horizontal = [
        "amenities",
        "facilities",
        "house_rules"
    ]

    # ManyToManyField cannot be added to list_filter, so you need to created custom admin functions
    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()
    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = (
        "__str__",
        "get_thumbnail"
    )

    # By default, Django does not run any Html or Script file automatically, to prevent the server from hacking
    # mark_safe tells django that it is safe to execute
    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px"src="{obj.file.url}"" />')
    get_thumbnail.short_description = "Thumbnail"

