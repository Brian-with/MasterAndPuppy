from django.db import models

class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.first_name

class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.TimeField()

    def __str__(self):
        return self.title

class Actor_Movie(models.Model):
    actor_id = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)