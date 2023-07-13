from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import TemplateView, ListView
from .models import News, Category, Contact
from .forms import ContactForm
# Create your views here.


def NewsList(request):
    news_list = News.objects.filter(status=News.Status.Published)
    context = {
        'news_list': news_list
    }
    return render(request, 'news/news_list.html', context)


def News_detail(request, pk):
    news = get_object_or_404(News, pk=pk, status=News.Status.Published)
    context = {
        'news': news
    }
    return render(request, 'news/news_detail.html', context)


def homePageView(request):
    news = News.objects.all().order_by('-publish_time')[:4]
    category = Category.objects.all()
    local_news = News.objects.filter(category__name="JAHON").order_by('-publish_time')
    context = {
        'news': news,
        'category': category,
        'local_news': local_news,
    }
    return render(request, 'index.html', context=context)


class HomePageView(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.model.objects.all()
        context['local_news'] = News.objects.filter(category__name="JAHON").order_by('-publish_time')
        return context

# def contactPage(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return HttpResponse('<h2> Biz bilan boglanganingiz uchun tashakkur!!!')
#     context = {
#         'form': form
#     }
#     return render(request, 'news/contact.html', context)

class ContactPage(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse('<h2> Biz bilan boglanganingiz uchun tashakkur!!!')
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)


def Page404(request):
    return render(request, 'news/404.html')


def singlePage(request):
    return render(request, 'news/single_page.html')

