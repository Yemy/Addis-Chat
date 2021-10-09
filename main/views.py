from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import Profile
from django.views.generic import ListView
from .models import Posts


# @login_required
# def home(request):
# 	profile = Profile.objects.all()
# 	context = {
# 		'profile': profile
# 	}

# 	return render(request, 'main/home.html', context)


class Home(ListView):
	model = Profile
	context_object_name = "profile"
	template_name = 'main/home.html'
	

class PostsListView(ListView):
    model = Posts
    template_name = 'main/home.html'
    context_object_name = "posts"
    ordering = "-date_posted"
    paginate_by = "10"

