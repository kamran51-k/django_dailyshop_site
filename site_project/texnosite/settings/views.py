from django.shortcuts import render

from settings.models import CategoryModel, StyleModel

# Create your views here.
def home_view(request):
    context ={}
    category_queryset = CategoryModel.objects.all()
    context['category_queryset'] = category_queryset

    return render(request,'index.html',context)


def style_view(request):
    context  = {}
    style_queryset = StyleModel.objects.all()
    context['style_queryset'] = style_queryset

    return render(request,'men_dropdown.html',context)