# from django.urls import path
# from news.api.views import article_detail_view,article_list_create_api_view
#
# urlpatterns = [
#     path('articles/', article_list_create_api_view, name='article-list'),
#     path('articles/<int:pk>/', article_detail_view, name='article-detail'),
# ]


from django.urls import path
#from news.api.views import ArticleDetailAPIView, ArticleListCreateAPIView, JournalistListCreateAPIView
from news.api.views import ArticleDetail, ArticleList, JournalistList
urlpatterns = [
    path('articles/', ArticleList.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
    path('journalists/', JournalistList.as_view(), name='journalist-list'),
]
