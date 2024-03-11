from django.shortcuts import render

def post_list(request):
    return render(request, 'vitalogblog/blog_list.html')

