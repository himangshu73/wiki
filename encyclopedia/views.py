from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
import random
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request,title):
    title_uppercase = title.upper()
    entry = util.get_entry(title)
    return render(request,"encyclopedia/page.html",{
        "title_description":entry,
        "title":title_uppercase
    })

def search(request):
    query = request.GET.get('q','')
    


    if util.get_entry(query):
        return redirect('page',title=query)
    
    else:
        matching_entries = []
        for entry in util.list_entries():
            if query.lower() in entry.lower():
                matching_entries.append(entry)
        return render(request, "encyclopedia/search.html",{
            "query":query,
            "entries":matching_entries,
        })
    
def new_page(request):
    return render(request,'encyclopedia/new_page.html')   

@require_POST
def save_new_page(request):
    if request.method == "POST":
        post_title = request.POST.get('post_title').upper()
        post_description = request.POST.get('post_description')
        if util.get_entry(post_title):
            return render(request, 'encyclopedia/new_page.html',{'error':'Page with this title already exist.'})
        if post_title and post_description:
            util.save_entry(post_title,post_description)
            return redirect('new_page')
        else:
            return render(request,'encyclopedia/new_page.html',{'error':'Title and description are required'})
    else:
        return redirect('new_page')  

def edit_page(request,title):
    entry_content = util.get_entry(title)
    if request.method == "POST":
        new_content = request.POST.get('post_description')
        util.save_entry(title,new_content)
        return redirect('page',title=title)
    return render(request,'encyclopedia/edit_page.html',{'title':title,'entry_content':entry_content})          

def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return redirect('page',title=random_entry)