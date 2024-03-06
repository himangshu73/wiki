from django.shortcuts import render,redirect

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

