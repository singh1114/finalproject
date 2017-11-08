# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView

from algorithms import pagerankalgo
from algorithms import degreecentrality

from fproject.forms import Area

# Create your views here.
class EnterAreaView(FormView):
    template_name = 'fproject/fillform.html'
    form_class = Area
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if(form.is_valid()):
            area = request.POST['area']
            # run_script here
            # create file
            # save the file
            return HttpResponse('')


class PageRankView(View):
    def get(self, request, *args, **kwargs):
        pagerank = pagerankalgo()
        return HttpResponse(pagerank)


class DegreeCentralityView(View):
    def get(self, request, *args, **kwargs):
        degcentrality = degreecentrality()
        return HttpResponse(degcentrality)
