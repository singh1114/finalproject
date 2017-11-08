# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from algorithms import pagerankalgo
from algorithms import degreecentrality

# Create your views here.
class PageRankView(View):
    def get(self, request, *args, **kwargs):
        pagerank = pagerankalgo()
        return HttpResponse(pagerank)

class DegreeCentralityView(View):
    def get(self, request, *args, **kwargs):
        degreecentrality = degreecentrality()
        return HttpResponse(degreecentrality)

