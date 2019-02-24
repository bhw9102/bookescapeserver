from django.shortcuts import render
from parser import parse_blog
from collector.models import BlogData


def parser(request):
    blog_data_dict = parse_blog()
    for t, l in blog_data_dict.items():
        BlogData(title=t, link=l).save()
    return ""

