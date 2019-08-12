from __future__ import unicode_literals
from django.db.models import Avg, Max, Min
from django.db import models

class ScrnClass(models.Model):
    class_no = models.CharField(primary_key=True, max_length=2)
    class_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scrn_class'

    def __str__(self):
        return self.class_name


class Movie(models.Model):
    movie_no = models.AutoField(primary_key=True, max_length=4)
    movie_name = models.CharField(max_length=50, blank=True, null=True)
    scrn_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    scrn_time = models.IntegerField(blank=True, null=True)
    class_no = models.ForeignKey(ScrnClass, models.DO_NOTHING, db_column='class_no')
    dist_name = models.CharField(max_length=50, blank=True, null=True)
    director_name = models.CharField(max_length=50, blank=True, null=True)
    actor_name = models.CharField(max_length=50, blank=True, null=True)
    movie_intro = models.TextField(max_length=700, blank=True, null=True)
    poster = models.ImageField(upload_to='post_image',blank=True, null=True)
    trailer = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie'

    def __str__(self):
        return self.movie_name


class Theater(models.Model):
    theater_no = models.CharField(primary_key=True, max_length=2)
    theater_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'theater'

    def __str__(self):
        return self.theater_name

class Seat(models.Model):
    seat_no = models.CharField(primary_key=True, max_length=3)
    theater_no = models.ForeignKey(Theater, models.DO_NOTHING, db_column='theater_no', primary_key=True)

    class Meta:
        managed = False
        db_table = 'seat'
        unique_together = (('seat_no', 'theater_no'),)

    def __str__(self):
        return self.seat_no