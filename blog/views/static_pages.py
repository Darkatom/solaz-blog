from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse

from blog.models import BlogSettings
from blog.forms import BlogAboutForm, BlogContactForm
from blog.views.renderers import static_page_renderer, dashboard_renderer
from django.contrib.auth.decorators import login_required

def about(request):
    blog = BlogSettings.objects.get(pk=1)
    return static_page_renderer(request, {'page_text': blog.about})

def contact(request):
    blog = BlogSettings.objects.get(pk=1)
    return static_page_renderer(request, {'page_text': blog.contact_data})

@login_required          
def edit_about(request):
    blog = get_object_or_404(BlogSettings, pk=1)

    context = {
        'template_path': "./blog/statics/_edit-static-page.html",
        'form_title': "Sobre nosotras",
        'form': BlogAboutForm()
    }

    if request.method == "POST":
        form = BlogAboutForm(request.POST, instance=blog)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect(reverse('blog:dashboard_static'))
        else:
            context['form'] = form
    else:
        context['form'] = BlogAboutForm(instance=blog)

    return dashboard_renderer(request, context)

@login_required          
def edit_contact(request):
    blog = get_object_or_404(BlogSettings, pk=1)

    context = {
        'template_path': "./blog/statics/_edit-static-page.html",
        'form_title': "Contacto",
        'form': BlogContactForm()
    }

    if request.method == "POST":
        form = BlogContactForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:dashboard_static'))
        else:
            context['form'] = form
    else:
        context['form'] = BlogContactForm(instance=blog)

    return dashboard_renderer(request, context)
