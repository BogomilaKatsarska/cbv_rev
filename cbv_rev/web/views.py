import random
from django.views import generic as views
from django import views
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'FBV',
    }
    return render(request, 'index.html', context)


class IndexView(views.View):
    def get(self, request):
        context = {
            'title': 'CBV',
        }
        return render(request, 'index.html', context)

    def post(self, request):
        pass


class IndexViewWithTemplate(views.TemplateView):
    template_name = 'index.html'
    extra_context = {
        'title': 'Template view',
    }



# class IndexView:
#
#     def __init__(self):
#         self.values = [
#             random.randint(1, 15),
#             ]
#
#     @classmethod
#     def get_view(cls):
#         return cls().view
#
#     def view(self, request):
#         return HttpResponse(f'It works:{self.values}')
#
#
# class Index2View(IndexView):
#     def __init__(self):
#         super().__init__()
#         self.values.append(random.randint(15, 30))

