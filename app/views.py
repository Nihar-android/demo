from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# def index(TemplateView):
#     template_name = "index.html"

class HomePageView(TemplateView):
    template_name = "index.html"


class PlayerPageView(TemplateView):
    template_name = "player.html"

# class algorithmPageView(TemplateView):
    # template_name = "algorithm.html"


# Add this view
class algorithmPageView(TemplateView):
    def get(self, request, **kwargs):
        # we will pass this context object into the
        # template so that we can access the data
        # list in the template
        context = {
            'data': [
                {
                    'name': 'Celeb 1',
                    'worth': '3567892'
                },
                {
                    'name': 'Celeb 2',
                    'worth': '23000000'
                },
                {
                    'name': 'Celeb 3',
                    'worth': '1000007'
                },
                {
                    'name': 'Celeb 4',
                    'worth': '456789'
                },
                {
                    'name': 'Celeb 5',
                    'worth': '7890000'
                },
                {
                    'name': 'Celeb 6',
                    'worth': '12000456'
                },
                {
                    'name': 'Celeb 7',
                    'worth': '896000'
                },
                {
                    'name': 'Celeb 8',
                    'worth': '670000'
                }
            ]
        }

        return render(request, 'algoithm.html', context)

# def product(request, parameter): # it's just passed as kwarg into view
#     return render(request, 'algorithm.html')