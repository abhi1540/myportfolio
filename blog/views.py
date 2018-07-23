from django.shortcuts import render, get_object_or_404, redirect, Http404
from .models import Category
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# Create your views here.


def about_me(request):
    return render(request, "aboutme.html", {})


class AllBlog(ListView):
    queryset = Category.objects.all()
    template_name = "home.html"
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super(AllBlog, self).get_context_data(*args, **kwargs)

        paginator = Paginator(self.queryset, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        context['queryset'] = queryset
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