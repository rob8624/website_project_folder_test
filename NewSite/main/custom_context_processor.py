from .models import Profile, Category, BlogPost, Post_Category, Tags
from django.contrib.auth.decorators import user_passes_test

def user_info(request):

    user = request.user
    if user.is_authenticated:
        current_user = Profile.objects.get(user=user)
        return {'user': current_user }
    else:
        return {'user': Profile.objects.get(user='1')}

def post_info(request):
  popular_posts = BlogPost.objects.filter(status='published').order_by('-created')[0:3]
  return {'popular_posts': popular_posts}

def category_info(request):
  categories = Post_Category.objects.all()[0:2]
  return {'categories': categories}


def category_info(request):
  tags = Tags.objects.all()
  return {'tags': tags}

