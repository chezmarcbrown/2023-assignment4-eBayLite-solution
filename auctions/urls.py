from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),

    #path("", views.index, name="index"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("bid/<int:listing_id>", views.bid, name="bid"),
    path("my_listings", views.my_listings, name="my-listings"),
    path("my_watchlist", views.my_watchlist, name="my-watchlist"),
    #path("create_listing", views.create_listing, name="create-listing"),
    #path("categories", views.categories, name="categories"),
    #path("category/<int:category_id>", views.category, name="category"),
    path("comment/<int:listing_id>", views.add_comment, name="add-comment"),
    
    path("api/status", views.api_status, name="api-status"),

    path('', views.ListingsView.as_view(), name="index"),
    path("create_listing", views.ListingCreateView.as_view(), name="create-listing"),
    path('categories', views.CategoriesView.as_view(), name='categories'),
    path('category/<int:category_id>', views.CategoryView.as_view(), name='category'),
    path('create_category', views.CategoryCreateView.as_view(), name='create-category'),
    path('category/update/<int:pk>', views.CategoryEditView.as_view(), name='update-category'),
    path('category/delete/<int:pk>', views.CategoryDeleteView.as_view(), name='delete-category'),


]
