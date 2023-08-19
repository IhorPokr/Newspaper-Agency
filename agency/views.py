from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from agency.forms import RedactorCreationForm, NewspaperForm, NewspaperSearchForm
from agency.models import Newspaper, Redactor, Topic


@login_required
def index(request):
    num_newspapers = Newspaper.objects.count()
    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_newspapers": num_newspapers,
        "num_redactors": num_redactors,
        "num_topics": num_topics,
        "num_visits": num_visits + 1,
    }

    return render(request, "agency/index.html", context=context)


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 10


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    success_url = reverse_lazy("agency:redactor-list")


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    fields = "__all__"
    success_url = reverse_lazy("agency:redactor-list")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    template_name = "agency/redactor_confirm_delete.html"
    success_url = reverse_lazy("agency:redactor-list")


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = NewspaperSearchForm(initial={
            "title": title
        })

        return context

    def get_queryset(self):
        queryset = Newspaper.objects.select_related("topic")

        form = NewspaperSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                title__icontains=form.cleaned_data["title"]
            )

        return queryset


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("agency:newspaper-list")


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    template_name = "agency/topic_confirm_delete.html"
    success_url = reverse_lazy("agency:topic-list")
