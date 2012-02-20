import datetime

from django.shortcuts import get_list_or_404, render
from django.template.defaultfilters import wordcount
from django.utils.html import strip_tags

from devotionals.models import Devotional

def devotional_all(request):

    devotionals = Devotional.objects.all()

    return render(request, 'devotionals/devotional_all.html', {'devotionals': devotionals})

def devotional_date(request, year, month, day):

    devotionals = get_list_or_404(Devotional, created_date__year=year, created_date__month=month, created_date__day=day)

    return render(request, 'devotionals/devotional_date.html', {'devotionals': devotionals})

def devotional_word_count(request):

    devotionals = Devotional.objects.all()
    count = 0
    for d in devotionals:
        body = strip_tags(d.body)
        count += int(wordcount(d.body))

    return render(request, 'devotionals/devotional_word_count.html', {'count': count})