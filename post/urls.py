from django.urls import path

from . import views

app_name = 'post'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('', views.CategoryView.as_view(), name='home'),
    path('detail/<int:pk>/', views.DetailPostView.as_view(), name='detail'),
    path('detail/like/<int:pk>/', views.likes, name='likes'),
    path('create/', views.CreatePostView.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdatePostView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeletePostView.as_view(), name='delete'),
    path('category/<str:cat>/', views.category, name='category'),
    path('list-category/', views.categoryList, name='list-category'),
    path('add-category/', views.CreateCategoryView.as_view(), name='add-category'),
    path('comment/<int:pk>/', views.AddCommentView.as_view(), name='comment'),
]
