from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('show_words', views.show_words, name="show_words"),
    path('show_stats', views.show_stats, name="show_stats"),
    path('add_word', views.add_word, name="add_word"),
    path('add_word_processing',
         views.add_word_processing,
         name="add_word_processing"),
    path('update_word', views.update_word, name="update_word"),
    path('update_word_processing',
         views.update_word_processing,
         name="update_word_processing")
]
