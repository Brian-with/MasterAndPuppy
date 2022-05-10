import json

from django.http import JsonResponse
from django.views import View

from .models import Owner, Dog

class UserinfoView(View):

    # def GET(self, request):
    #     return HttpResponse("common page get")

	def POST(self, request):
		# Client에서 전송한 데이터를 데이터베이스에 저장한다.
		"""
        # http -v POST http://localhost:8000/common
        # name = 홍길동 email = hgd@gmail.com age = 80
        # dog_name = 백구 dog_age = 15
		"""
		input = json.loads(request.body)
		
		owner = Owner.objects.create(
			name = input["name"],
			email = input["email"],
			age	= input["age"])
			
		dog = Dog.objects.create(
			name = input["dog_name"],
			age	= input["dog_age"],
			owner_id = owner.id)
		
		return JsonResponse({"message" : "SUCCESS"}, status = 201)
