from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    """ Custom User Module"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "other"),

    )
    """ 그냥 집어넣음, 언어, 화폐 단위"""

    # LANGUAGE_ENGLISH = "en"
    # LANGUAGE_KOREAN = "kr"
    # LANGUAGE_CHOICES = (
    #     (LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "korean"))

    # CURRENCY_DOLLAR = "usd"
    # CURRENCY_KR = "krw"
    # CURRENCY_CHOICES = ((CURRENCY_DOLLAR, "USD"), (CURRENCY_KR, "KRW"))

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"),
                        (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_DOLLAR = "usd"
    CURRENCY_USD = "krw"
    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_USD, "KRW"))

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10, null=True, blank=True)
    bio = models.TextField(default="", blank=True)
    # birthday = models.DateTimeField(null=True)
    # language = models.CharField(
    #     choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True)
    # currency = models.CharField(
    #     choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True)
    # superhost = models.BooleanField(default=False)

    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True
    )
    superhost = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.username
