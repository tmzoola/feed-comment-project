from places.models import Place, Comment
from django.views import View
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import PlaceSerializer, ReviewSerializer

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

class PlaceDetailApiView(APIView):
    def get(self, request, id):
        place = Place.objects.get(id=id)
        serializer = PlaceSerializer(place)
        return Response(serializer.data)


class ReviewsApiView(APIView):
    def get(self, request):
        comments = Comment.objects.all().select_related('user').select_related('place')

        serializer = ReviewSerializer(comments, many=True)

        return Response(serializer.data)