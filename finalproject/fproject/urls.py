from django.conf.urls import url, include
from django.views.generic import TemplateView
from fproject.views import PageRankView
urlpatterns = [
    url(r'^pagerank/?', PageRankView.as_view(), name='pagerank'),
    url(r'^degreecentrality/?', DegreeCentralityView.as_view(), name='degreecentrality'),
    url(r'^index/', TemplateView.as_view(template_name="fproject/index.html")),
]
