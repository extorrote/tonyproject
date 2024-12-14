"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tonyapp import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.index ,name="index"),
    path('index/' , views.index ,name="index"),
    
    path('upload-song/', views.upload_song, name='upload_song'),
    path('create_post_index/', views.create_post_index, name='create_post_index'), 
    
    path('biography/', views.biography,name="biography"),
    path('send_email/', views.send_email, name='send_email'),
     path('create_event/', views.create_event, name='create_event'),
    path('schedule/', views.schedule, name='schedule'),
    path('contact/', views.contact,name="contact"),
    path('discography/', views.discography, name="discography"),
    path('post_music_section/', views.post_song, name='post_music_section'),
    path('music_section_list/', views.view_songs, name="music_section_list"),
    path('post_video/', views.post_video, name="post_video"),
    path('videos_list/', views.view_videos, name="videos_list"),
    path('post_gallery/', views.post_gallery, name="post_gallery"),  # URL for the form
    path('gallery_list/', views.gallery_list, name="gallery_list"),  # URL to view all images
    path('faq/',views.faq , name="faq"),   
    path('store/', views.product_list, name='product_list'),  # Shows all products by default
    path('store/<str:product_type>/', views.product_list, name='product_list_by_type'),  # Filter products by category
    # Product list
    path('product_list/<str:product_type>/', views.product_list, name='product_list'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('add_to_cart/<str:product_type>/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart-item/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/success/', views.checkout_success, name='checkout_success'),
    path('checkout/cancel/', views.checkout_cancel, name='checkout_cancel'),
    path('create/clothing/', views.create_clothing, name='create_clothing'),
    path('create/poster/', views.create_poster, name='create_poster'),
    path('create/album/', views.create_album, name='create_album'),
    path('create/music_set/', views.create_music_set, name='create_music_set'),
    path('create/coffee_mug/', views.create_coffee_mug, name='create_coffee_mug'),
    
    path('add_to_cart/<str:product_type>/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add_to_cart/<str:product_type>/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('about_us/',views.about_us,name="about_us"),
    path('terms_and_conditions/',views.terms_and_conditions,name="terms_and_conditions"),
    path('privacy_policy/',views.privacy_policy,name="privacy_policy"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
