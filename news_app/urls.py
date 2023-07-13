from .views import NewsList, News_detail, HomePageView, ContactPage, Page404, singlePage
from django.urls import path


urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('news/all/', NewsList, name='news-list'),
    path('news/<int:pk>/', News_detail, name='news-detail'),
    path('news/contact/', ContactPage.as_view(), name='contact'),
    path('news/404/', Page404, name='page-404'),
    path('news/about/', singlePage, name='single-page'),
    # path('all/', NewsList.as_view(), name='news-list'),
    # path('<int:pk>/', News_detail.as_view(), name='news-detail'),
]


