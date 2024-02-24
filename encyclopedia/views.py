from django.shortcuts import render

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

