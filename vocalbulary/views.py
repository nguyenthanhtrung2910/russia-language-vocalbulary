"""
view funtions
"""
from django.shortcuts import render

from vocalbulary.models import Vocalbulary

def index(request):
    """
    render main page
    """
    return render(request, "index.html")


def show_words(request):
    """
    render table of saved words
    """
    rows = Vocalbulary.objects.all()
    row_styles = [row.pk % 6 for row in rows]
    return render(request,
                  "show_words.html",
                  context={'pairs': zip(rows, row_styles)})


def show_stats(request):
    """
    render statitics
    """
    num_words = Vocalbulary.objects.all().count()
    ratio_typed_words = Vocalbulary.objects.exclude(word_type='').exclude(
        word_type__isnull=True).count() * 100 / num_words
    ratio_commented_words = Vocalbulary.objects.exclude(example='').exclude(
        example__isnull=True).count() * 100 / num_words
    return render(request,
                  "show_stats.html",
                  context={
                      'num_words': num_words,
                      'ratio_typed_words': ratio_typed_words,
                      'ratio_commented_words': ratio_commented_words
                  })


def add_word(request):
    """
    render add word form
    """
    return render(request, "add_word.html")


def add_word_processing(request):
    """
    process adding word
    """
    if request.method == "POST":
        ru_word = request.POST.get("ru_word")
        if ru_word in Vocalbulary.objects.values_list('ru_word', flat=True):
            return render(request, "add_word.html", context={'error': True})
        en_word = request.POST.get("en_word")
        word_type = request.POST.get("word_type", "")
        example = request.POST.get("example", "")
        pair = Vocalbulary(en_word=en_word,
                           ru_word=ru_word,
                           word_type=word_type,
                           example=example)
        pair.save()
        return render(request, "add_word.html", context={'success': True})
    return render(request, "add_word.html")


def update_word(request):
    """
    render update word form
    """
    return render(request, "update_word.html")


def update_word_processing(request):
    """
    processing updating word
    """
    if request.method == "POST":
        ru_word = request.POST.get("ru_word")
        en_word = request.POST.get("en_word")
        word_type = request.POST.get("word_type")
        example = request.POST.get("example")
        pair = Vocalbulary.objects.filter(ru_word=ru_word)
        if pair.exists():
            if en_word:
                pair.update(en_word=en_word)
            if word_type:
                pair.update(word_type=word_type)
            if example:
                pair.update(example=example)
            return render(request,
                          "update_word.html",
                          context={'success': True})
        return render(request, "update_word.html", context={'error': True})
    return render(request, "update_word.html")
