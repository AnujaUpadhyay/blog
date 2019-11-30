from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):

	post_image = models.TextField()

	post_title = models.CharField(max_length=200)

	post_date = models.DateTimeField(auto_now_add=True)

	post_auther = models.CharField(max_length=100)

	post_content = RichTextField(blank=True,null=True)

	slug = models.SlugField(null=False,unique=True)

	#some sorts of string representation in the admin site
	def __str__(self):
		return self.post_title

	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'slug':self.slug})



    # def get_absolute_url(self):
    #     return reverse("posts:detail", kwargs={"slug": self.post_slug})



