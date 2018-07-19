from .models import Category

def menu_links(request):
    # links = set(Category.objects.values_list('tag', flat=True))
    links = Category.objects.values('tag').order_by('tag').distinct('tag')
    return dict(links=links)


def all_obj(request):
    obj = Category.objects.all()
    return dict(obj=obj)