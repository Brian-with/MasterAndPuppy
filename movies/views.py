import json
from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Actor, Movie, Actor_Movie


def index(request):
    return HttpResponse("this is index of movies")

class ActorInfoView(View):

    def get(self, request):

        results = []
        actors = Actor.objects.all()

        for actor in actors:
            actor_movies = Actor_Movie.objects.filter(actor_id=actor.id)
            
            result_movie = []
            for actor_movie in actor_movies:
                result_movie.append(actor_movie.movie_id.title)
                
            results.append(
                {
                    "이름"  :   actor.last_name + " " + actor.first_name,
                    "출현영화"  : result_movie,
                })        
        
        return JsonResponse({"배우정보" : results}, status=200)

class MovieInfoView(View):

    def get(self, request):
        results = []
        movies = Movie.objects.all()
        for movie in movies:
            movies_info = Actor_Movie.objects.filter(movie_id=movie.id)

            list_actor = []
            for movie_info in movies_info:
                list_actor.append(movie_info.actor_id.first_name)

            results.append(
                {
                "영화제목"  :   movie.title,
                "상영시간"  :   movie.running_time,
                "출연배우 목록" :   list_actor
                })

        return JsonResponse({"영화정보" : results}, status=200)