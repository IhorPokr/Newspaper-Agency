from django.urls import path

from agency.views import (
    index,
    RedactorListView,
    RedactorCreateView,
    NewspaperListView,
    TopicListView,
    NewspaperDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list"
    ),
    path(
        "redactors/create/",
        RedactorCreateView.as_view(),
        name="redactor-list-create"
    ),
    path(
        "newspapers/",
        NewspaperListView.as_view(),
        name="newspaper-list"
    ),
    path(
        "newspapers/<int:pk>",
        NewspaperDetailView.as_view(),
        name="newspaper-detail"
    ),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list"
    )
]

app_name = "agency"
