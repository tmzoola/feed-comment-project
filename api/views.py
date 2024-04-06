from places.models import Place, Comment
from django.views import View
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import PlaceSerializer

class PlaceApiView(APIView):
    def get(self, request):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = PlaceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class PlaceDetailApiView(View):
    def get(self, request, id):
        place = Place.objects.get(id=id)

        data = {
            "id": place.id,
            "description": place.description,
            "image": place.image.url,
            "address": place.address
        }

        return JsonResponse(data)


class ReviewsApiView(View):
    def get(self, request):
        comments = Comment.objects.all().select_related('user').select_related('place')

        result = []

        for comment in comments:
            data = {
                "comment_text": comment.comment_text,
                "stars_given": comment.stars_given,
                "created_at": comment.created_at,
                "user": {
                    "user_id": comment.user.id,
                    "username": comment.user.username,
                    "user_image": comment.user.photo.url,
                },
                "place": {
                    "place_id": comment.place.id,
                    "place_image": comment.place.image.url
                }
            }

            result.append(data)

        return JsonResponse({"result": result})