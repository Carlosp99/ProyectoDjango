from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

class HelloWorld(View):
    def get(self, request):
        data = {
            'name': 'Carlos Piñeros',
            'Years': 28,
            'Codes': ['Python','Django','React','Vue']
        }
        return render(request, 'hello_wordl.html',context=data)