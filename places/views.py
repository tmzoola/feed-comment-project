from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from .models import Place, Comment
from .forms import PlaceCommentForm


class PlaceListView(View):
    def get(self, request):

        places = Place.objects.all()
        search_query = request.GET.get("q", "")

        if search_query:
            places = places.filter(name__icontains=search_query)

        return render(request, 'places/list.html', {"places": places, "search_query": search_query})


class PlaceDetailView(View):

    def get(self, request, pk):
        form = PlaceCommentForm()

        place = get_object_or_404(Place, pk=pk)

        return render(request, 'places/detail.html', {"place": place, "form": form})


class AddCommentView(LoginRequiredMixin,View):

    def post(self, request, id):
        place = Place.objects.get(id=id)
        form = PlaceCommentForm(request.POST)

        if form.is_valid():
            Comment.objects.create(
                user=request.user,
                place=place,
                comment_text=form.cleaned_data['comment_text'],
                stars_given=form.cleaned_data['stars_given']

            )

            return redirect(reverse("places:detail", kwargs={"pk": place.id}))

        return render(request, 'places/detail.html', {"place": place, "form": form})