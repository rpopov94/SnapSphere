from django.db import models


class Photo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PhotoManager(models.Manager):
    def approved_photos(self):
        return self.filter(approved=True)

    def unapproved_photos(self):
        return self.filter(approved=False)


class Country(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)

    objects = PhotoManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'countries'


class City(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)

    objects = PhotoManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'


class Item(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)

    objects = PhotoManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Items'


class User(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)

    objects = PhotoManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Users'
