from django.template.loader import get_template
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import redirect
from datetime import datetime
from .models import Post

# Create your views here.
def homepage(request):
    # posts = Post.objects.all()
    # post_lists = list()
    # for count, post in enumerate(posts):
    #     post_lists.append("No.{}:".format(str(count)) + str(post)+ "<hr>")
        # post_lists.append("<small>"+str(post.body.encode("utf-8")+"<small><br><br>"))
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())

    # 使用HttpResponse輸出到使用者端
    return HttpResponse(html)

def showpost(request, slug):
    template = get_template('post_html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')