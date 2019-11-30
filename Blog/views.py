from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
# Create your views here.

#homepage view
class HomePageView(ListView):
	model = Post
	template_name = 'Blog/index.html'
	context_object_name = 'post_entries'
	ordering = ('-post_date')
	paginate_by = 5


	#sidebar view
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		side_view = Post.objects.all().order_by('-post_date')[0:5]
		context['side_view'] = side_view
		return context




class PostDetailView(DetailView):
	model = Post
	template_name = 'Blog/post_detail.html'
	context_object_name = 'post_detail'
	slug_url_kwarg = 'slug'

	#sidebar view
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		side_view = Post.objects.all().order_by('-post_date')[0:5]
		context['side_view'] = side_view
		return context


	

