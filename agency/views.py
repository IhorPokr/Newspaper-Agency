from django.shortcuts import render
from django.views import generic

from agency.models import Newspaper, Redactor, Topic


def index(request):
    num_newspapers = Newspaper.objects.count()
    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()

    context = {
        "num_newspapers": num_newspapers,
        "num_redactors": num_redactors,
        "num_topics": num_topics,
    }

    return render(request, "agency/index.html", context=context)


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 10


class NewspaperListView(generic.ListView):
    model = Newspaper
    paginate_by = 10


class TopicListView(generic.ListView):
    model = Topic
    paginate_by = 5


class NewspaperDetailView(generic.DetailView):
    model = Newspaper
