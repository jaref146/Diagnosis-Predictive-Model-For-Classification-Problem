from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class sale_book(models.Model):
    class Meta:
        verbose_name_plural = 'Sale Book Information'

    store_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default='1')
    store_post_book_name = models.CharField(max_length=256, blank=True, null=True)
    store_post_book_price = models.IntegerField( blank=True, null=True)
    store_post_book_user_email = models.CharField(max_length=256, blank=True, null=True)
    store_post_book_user_number = models.CharField(max_length=256, blank=True, null=True)
    store_post_book_subject = models.CharField(max_length=256, blank=True, null=True)
    store_post_book_description = models.TextField(max_length=256, blank=True, null=True)
    store_post_book_image = models.CharField(max_length=256, blank=True, null=True)

    store_post_time = models.DateTimeField(default=datetime.now(), blank=True)

    type = (

        ("Arts & Music", "Arts & Music"),
        ("Biographies", "Biographies"),
        ("Business", "Business"),
        ("Comics", "Comics"),
        ("Computers & Tech", "Computers & Tech"),
        ("Cooking", "Cooking"),
        ("Edu & Reference", "Edu & Reference"),
        ("Entertainment", "Entertainment"),
        ("Special Editions", "Special Editions"),
        ("Health & Fitness", "Health & Fitness"),
        ("History", "History"),
        ("Horror", "Horror"),
        ("Medical", "Medical"),
        ("Religion", "Religion"),
        ("Romance", "Romance"),
        ("Other", "Other"),
    )
    Books_category = models.CharField(max_length=90, choices=type,blank=True, null=True)


    def __str__(self):
        return self.store_post_book_name +self.store_post_book_user_number


class contact_info_tabel(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Info Tabel'
    contact_persions_name = models.CharField(max_length=256, blank=True, null=True)
    contact_persions_email = models.CharField(max_length=256, blank=True, null=True)
    contact_persions_subjects = models.CharField(max_length=256, blank=True, null=True)
    contact_persions_massages = models.TextField( blank=True, null=True)
    def __str__(self):
        return self.contact_persions_name +self.contact_persions_email

class wish_list_table(models.Model):
    class Meta:
        verbose_name_plural = 'Wish List Table'
    Wish_persions = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default='1')
    Wish_product = models.ForeignKey(sale_book, on_delete=models.CASCADE, blank=True, null=True, default='1')
    Wish_time = models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return self.Wish_persions.username