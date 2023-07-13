from .models import News


def lastet_news(request):
    lasted_news = News.objects.all().order_by()[:10]

    context = {
        'lasted_news': lasted_news
    }
    return context


