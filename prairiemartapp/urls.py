from django.urls import path
from django.conf.urls import url
from prairiemartapp import views

app_name = 'prairiemartapp'

urlpatterns = [
    path('about-page/', views.about, name='about'),
    path('contact-page/', views.contact, name='contact'),
    path('blog-page/', views.blog, name='blog'),
    path('blog-details/', views.blog_details, name='blogpost'),
    path('checkout/', views.checkout, name='checkout'),
    path('product-page/', views.product, name='product'),
    path('order-page/', views.order, name='order'),
    path('compare-page/', views.compare, name='compare'),
    path('wishlist-page/', views.wishlist, name='wishlist'),
    path('category_grid-page/', views.category_grid, name='category_grid'),
<<<<<<< HEAD
    url(r'^category_list-page/(?P<category_slug>[-\w]+)/$', views.category_list, name='category_list'),
    # url(r'^shop/(?P<category_slug>[-\w]+)/$', views.shop, name='product_list_by_category'),
    path('dashboard-page/', views.dashboard, name='dashboard'),
    path('login-page/', views.login, name='login'),
    
=======
    path('category_list-page/', views.category_list, name='category_list'),
    path('cutomer-dashboard-page/', views.cutomer_dashboard, name='cutomer_dashboard'),
    path('change-password-page/', views.change_password, name='change_password'),
    path('view-profile-page/', views.view_profile, name='view_profile'),
    path('edit-form-page/', views.edit_form, name='edit_form'),
>>>>>>> benedict
]
