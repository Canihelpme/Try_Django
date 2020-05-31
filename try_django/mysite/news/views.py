from django.shortcuts import render

from .models import article

def year_archive(request, year):
    a_list = article.objects.filter(pub_date_year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

def month_archive(request, year, month):
    a_list = article.objects.filter(pub_date_month=month)
    context = {'month': month, 'article_list': a_list}
    return render(request, 'news/month_archive.html', context)