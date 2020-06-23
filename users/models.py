from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# AbstractUser already has a lot of stuff. We can expand it.
# Whatever you write in the model, Django will make you into a form. And Django will ask the database to fill in the form with information.
class User(AbstractUser):
    """ Custom User Model """

    # Choices does not affect database, since it is just changing the form
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    # for the database
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    # for the form
    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    # two options : default="" or null=True
    # null is for the database, blank is for the form
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True
    )
    superhost = models.BooleanField(default=False)

    def __str__(self):
        return self.username
