from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from bharu.models import Post,AboutUs
from django.http import Http404
from django.core.paginator import Paginator
from bharu.forms import ContactForm
# Create your views here.
# posts = [
#         {'id':1,'title':'pizza','content':'yummy1'},
#         {'id':2,'title':'salad','content':'yummy2'},
#         {'id':3,'title':'biriyani','content':'yummy3'},
#         {'id':4,'title':'dessert','content':'yummy4'}
#     ]

def index(request):
    bharu_title = "WELCOME CUSTOMER"
    Post.objects.all()
    return render(request,'index.html',{'bharu_title':bharu_title})

def menus(request,post_id):
    all_posts=Post.objects.all()
    paginator=Paginator(all_posts,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    # posts =Post.objects.get(pk=post_id)
    # post = next((item for item in post if item['id'] == int(post_id)), None)
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post variable is {posts}')
    return render(request,'menu.html',{'page_obj':page_obj,'id':post_id})

def details(request,post_id):
    try:
        post=Post.objects.get(pk=post_id)
        related_posts=Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404 ("Post Does not Exist!")    
    return render(request,'details.html',{'post':post,'related_posts':related_posts})
  
def old_url_redirect(request):
    return redirect(reverse("bharu:new_page_url"))

def new_url_view(request):
    return HttpResponse("This is the new url")

def contact_view(request):
    if request.method =='POST':
        form=ContactForm(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        logger=logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f'post  Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
            success_message='your email has been sent!'
            return render(request,'contact.html',{'form':form,'success_message':success_message})
        else:
            logger.debug('form validation failure')
            return render(request,'contact.html',{'form':form,'name':name,'email':email,'message':message})   
    return render(request,'contact.html')
def about_view(request):
    about_content=AboutUs.objects.first().content
    return render(request,'about.html',{'about_content':about_content})