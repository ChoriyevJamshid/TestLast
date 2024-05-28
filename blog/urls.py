from django.urls import path

from . import views


urlpatterns = [
    path('', views.PostListAPI.as_view()),
    path('<slug:slug>/<int:pk>/', views.PostDetailAPI.as_view()),
    path('<slug:slug>/<int:pk>/update/', views.PostUpdateAPI.as_view()),
    path('<slug:slug>/<int:pk>/delete/', views.PostDeleteAPI.as_view()),
    path('post/create/', views.PostCreateAPI.as_view()),

    path('mostviewed/posts/', views.MostViewedPostsAPI.as_view()),
    path('onweek/posts/', views.MostViewedOnWeekPostsAPI.as_view()),
    path('onmonth/posts/', views.MostViewedOnMonthPostsAPI.as_view()),
    path('recommended/posts/', views.RecommendedPostsAPI.as_view()),

    path('<slug:post_slug>/<int:post_id>/comments/', views.PostCommentsAPI.as_view()),
    path('comment/create/', views.CommentCreateAPI.as_view())
]
