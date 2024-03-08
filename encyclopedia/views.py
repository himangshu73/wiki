from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST

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