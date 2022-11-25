from django.shortcuts import render
from django.contrib import messages
from django import forms 
import random

from . import util

from markdown2 import Markdown
import difflib
markdowner = Markdown()

####utils variables and functions ###########
entries = util.list_entries()

class NewTaskForm(forms.Form):
    title = forms.CharField(label='title')
    content = forms.CharField(label='content')


def get_html_from_md(md_title):
    html = util.get_entry(md_title)
    if html != None:
        html =  markdowner.convert(html)
    elif html == None:
        html = '<img style="width:100%; alt="Not Found" src="https://http.cat/404">'
    return html

##############################################

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def entry(request, title):
    html = get_html_from_md(title)
    return render(request, "encyclopedia/entry.html", {
        "title" : title,
        "content": html
    } )


def search(request):
    if request.method == "POST":
        query = request.POST['q']
        close_matchs = difflib.get_close_matches(query, entries , cutoff=0.6)
        if query in entries:
            html = get_html_from_md(query)
            return render(request, "encyclopedia/entry.html", {
                "title" : query,
                "content": html
            } )

        else :
            return render(request, "encyclopedia/search.html", {
                "query" : query,
                "results": close_matchs
            } )




def create(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            #### if entry don't already exists
            if title not in entries:
                #### create it
                try:
                    util.save_entry(title, content)
                except:
                    messages.error(request,  f"Error saving the entry")                
                    return render(request , "encyclopedia/create.html")

                messages.success(request,  f"{title} saved successfully ")    
                return entry(request, title)            
            #else entry already exists
            else:
                messages.error(request, f'{ title } already exists')
                return render(request, "encyclopedia/create.html")

        ##else form is not valid        
        else:
            messages.error(request, " form is not valid")
            return render(request, "encyclopedia/create.html")
    else:
        return render(request, "encyclopedia/create.html")


########## Random
def random_page(request):
    page = random.choice(entries)
    return entry(request, title=page)


########## Edit

def edit(request, title):
    ##get request
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            try:
                util.save_entry(title, content)
            except:
                messages.error(request,  f"Error saving the entry")                
                return render(request , "encyclopedia/edit.html")

            messages.success(request, f"{title} edited successfully" )
            return entry(request, title=title)

        else:
            messages.error(request, "form not valid")
            return render(request, "encyclopedia/edit/html")

    content =  util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        'title': title,
        'content' : content
    } )