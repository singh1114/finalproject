from django.conf.urls import url, include
from django.views.generic import TemplateView
from fproject.views import PageRankView
from fproject.views import DegreeCentralityView
from fproject.views import EnterAreaView
urlpatterns = [
    url(r'^pagerank/?', PageRankView.as_view(), name='pagerank'),
    url(r'^fillform/?', EnterAreaView.as_view(), name='enterarea'),
    url(r'^degreecentrality/?', DegreeCentralityView.as_view(), name='degreecentrality'),
    url(r'^index/', TemplateView.as_view(template_name="fproject/index.html")),
]
