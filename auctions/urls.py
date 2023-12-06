from django.urls import path, reverse
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from . import views, forms

urlpatterns = [
    #path("login/", views.login_view, name="login"),
    #path("logout/", views.logout_view, name="logout"),
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

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(form_class=forms.MyPasswordResetForm), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
