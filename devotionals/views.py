import datetime

from django.shortcuts import get_list_or_404, render

from devotionals.models import Devotional

def devotional_all(request):

    devotionals = Devotional.objects.all()

    return render(request, 'devotionals/devotional_all.html', {'devotionals': devotionals})

def devotional_date(request, year, month, day):

    devotionals = get_list_or_404(Devotional, created_date__year=year, created_date__month=month, created_date__day=day)

    return render(request, 'devotionals/devotional_date.html', {'devotionals': devotionals})
