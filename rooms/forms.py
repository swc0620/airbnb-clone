from django import forms
from django_countries.fields import CountryField
from . import models

class SearchForm(forms.Form):
    # use forms similar to models, and django will fill out all the <label></label> or <select></select>
    # city = forms.CharField(initial="Anywhere", widget=forms.Textarea)
    city = forms.CharField(initial="Anywhere")
    country = CountryField(default="KR").formfield()
    room_type = forms.ModelChoiceField(
        empty_label="Any kind", 
        queryset=models.RoomType.objects.all(),
        required=False,
    )

    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)

    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)

    amenities = forms.ModelMultipleChoiceField(
        queryset=models.Amenity.objects.all(), 
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    facilities = forms.ModelMultipleChoiceField(
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )


