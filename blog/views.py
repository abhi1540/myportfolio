from django.shortcuts import render, get_object_or_404, redirect, Http404
from .models import Category
from django.views.generic import ListView, DetailView


# Create your views here.


# def home_page(request):
#     return render(request, "home.html", {})


class AllBlog(ListView):
    queryset = Category.objects.all()
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(AllBlog, self).get_context_data(*args, **kwargs)
        return context


class TagListView(ListView):
    queryset = Category.objects.all()
    template_name = "home.html"

    def get(self, tag=None, *args, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        if tag != None:
            context['products'] = get_object_or_404(Category, tag=tag)
            context['products_list'] = Category.objects.filter(tag=tag).distinct()
            print(context)
        return context


class TagDetailView(ListView):
    model = Category
    template_name = 'tag_details.html'

    def get_context_data(self, tag=None, **kwargs):

        # Call the base implementation first to get a context
        context = super(TagDetailView, self).get_context_data(**kwargs)
        tag = self.kwargs.get("tag")
        if tag:
            context.update(({'object_list': Category.objects.filter(tag__icontains=tag)}))
        return context

    # def get_queryset(self):
    #     tag = self.kwargs.get("tag")
    #     if tag:
    #         queryset = Category.objects.filter(tag__icontains=tag)
    #     else:
    #         queryset = Category.objects.all()
    #     return queryset


# class SlugDetailView(ListView):
#     model = Category
#     template_name = 'detailview.html'
#
#
#     def get_context_data(self, pk=id, slug=None, **kwargs):
#         products_list = None
#         # id = Category.objects.get(pk=id)
#         # slug = Category.objects.get(slug=slug)
#         context = super(SlugDetailView, self).get_context_data(**kwargs)
#         if slug is not None and id:
#             products_list = Category.objects.filter(slug=slug, pk=id)
#         else:
#             products_list = Category.objects.all()
#         print(id, slug)
#         context.update(({'object_list': products_list}))
#
#         return context

# def SlugDetailView(request, slug, tag):
#     product = get_object_or_404(Category, tag=tag, slug=slug)
#     return render(request, 'detailview.html',  {'product': product})
#

class SlugDetailView(ListView):
    queryset = Category.objects.all()
    template_name = "detailview.html"

    def get_context_data(self, slug=None, tag=None, **kwargs):
        context = super(SlugDetailView, self).get_context_data(**kwargs)
        tag = self.kwargs.get("tag")
        slug = self.kwargs.get("slug")
        product = get_object_or_404(Category, tag=tag, slug=slug)
        context.update(({'object_list': product}))
        return context