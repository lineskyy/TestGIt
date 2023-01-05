from django.shortcuts import render,redirect
from django.views.generic import TemplateView
# def test(reauests):
#     return render(reauests,'test.html')

class Test(TemplateView):
    template_name = 'test.html'