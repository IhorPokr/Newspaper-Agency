from django.urls import path

from agency.views import (
    index,
    RedactorListView,
    RedactorCreateView,
    RedactorUpdateView,
    RedactorDeleteView,
    NewspaperListView,
    NewspaperDetailView,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
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
        "redactors/<int:pk>/update/",
        RedactorUpdateView.as_view(),
        name="redactor-list-update"
    ),
    path(
        "redactors/<int:pk>/delete/",
        RedactorDeleteView.as_view(),
        name="redactor-list-delete"
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
    ),
    path(
        "topics/create/",
        TopicCreateView.as_view(),
        name="topic-list-create"
    ),
    path(
        "topics/<int:pk>/update/",
        TopicUpdateView.as_view(),
        name="topic-list-update"
    ),
    path(
        "topics/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-list-delete"
    ),
]

app_name = "agency"
