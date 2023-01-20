from django.shortcuts import render 
from mma.views import get_csv_data
posts = [
    {
        "author": "CoreyMs",
        "title": "Blog Post 1",
        "content": "UFC Lightweight Fighters",
        "date_posted": "August 27, 2018"
    },
    {
        "author": "Yooniverse",
        "title": "Blog Post 2",
        "content": "UFC Featherweight Fighters",
        "date_posted": "August 28, 2018"
    },
    { "name": "Conor McGregor",
      "nickname": "The Notorious",
      "record": {"wins": 22,
                 "losses": 5,
                 "draws": 0
                },
      "height": 5_9,
      "weight": 155,
      "reach": 74,
      "stance": "Southpaw",
      "division": "Lightweight",
      "age": 32,
      "striking_accuracy": 55.0,
      "grappling_accuracy": 48.0,
      "striking_defense": 66.0,
      "takedown_defense": 70.0,
      "knockout_ratio": 0.59,
      "submission_ratio": 0.18
    }
]

def home(request):
    context = {
        "posts": posts
    }
    return render(request, "stats/home.html", context)

def about(request):
    return render(request, "stats/about.html", {"title": "About"})

def fighters(request):
    return render(request, "stats/fighters.html", {"title": "Fighters"})

def api(request):
    return render(request, "stats/api.html", {"title": "api"})

def csv_data(request):
    data_list = get_csv_data()
    context = {'data': data_list}
    return render(request, 'stats/csv_data.html', context)