from django.shortcuts import render
from django.contrib import messages
from django import forms 
import random

from . import util

from markdown2 import Markdown
import difflib
markdowner = Markdown()

####utils variables and functions ###########
#status messages dict
status = {
    'save_s' : 'Saved Successfully',
    'save_w' : 'Already Exists',
    'save_e' : 'Error Saving',
    'edit_s' : 'Edited Successfully',
    'edit_e' : 'Error Editing',
    'form_e' : 'invalid Form',
    'exist_e': "Dont't exists",

}


# entries list
entries = util.list_entries()

#form object from django
class NewTaskForm(forms.Form):
    title = forms.CharField(label='title')
    content = forms.CharField(label='content')


#convert md to html
def get_html_from_md(md_title):
    html = util.get_entry(md_title)
    if html != None:
        html =  markdowner.convert(html)
    elif html == None:
        html = f" <img style='width:70%;' alt='Not Found' src='https://http.cat/404'>"
        status = False
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
                    messages.error(request,  f"{status['save_e']} {title}")                
                    return render(request , "encyclopedia/create.html")

                messages.success(request,  f"{title} {status['save_s']} ")    
                return entry(request, title)            
            #else entry already exists
            else:
                messages.error(request, f'{ title } {status["save_w"]} ')
                return render(request, "encyclopedia/create.html")

        ##else form is not valid        
        else:
            messages.error(request, f" {status['form_e']} ")
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
            ##edit if only wiki already exists
            if title in entries:
                try:
                    util.save_entry(title, content)
                except:
                    messages.error(request,  f" {status['edit_e']} {title} ")                
                    return render(request , "encyclopedia/edit.html")

                messages.success(request, f"{title}  {status['edit_s']} " )
                return entry(request, title=title)

            else:
                messages.error(request, f" wiki {status['exist_e']} ")
                return entry(request, title=title)

        else:
            messages.error(request, f" {status['form_e']} ")
            return render(request, "encyclopedia/edit.html")

    content =  util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        'title': title,
        'content' : content
    } )