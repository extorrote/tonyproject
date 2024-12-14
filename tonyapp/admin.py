from django.contrib import admin
from .models import (
    Song, 
    Post_index, 
    Event, 
    Music, 
    Videos, 
    Gallery, 
    Clothing, 
    Poster, 
    Album, 
    MusicSet, 
    CoffeeMug, 
    Cart, 
    CartItem
)

# Registering models in Django admin

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'background_image')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Post_index)
class PostIndexAdmin(admin.ModelAdmin):
    list_display = ('title', 'picture', 'description')
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'venue_name', 'created_at')
    search_fields = ('title', 'venue_name')
    list_filter = ('date',)


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'dropbox_link')
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'dropbox_link', 'youtube_link')
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'picture')
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    list_display = ('title', 'size', 'color', 'price', 'image')
    search_fields = ('title', 'size', 'color')
    list_filter = ('size', 'color', 'price')


@admin.register(Poster)
class PosterAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'image')
    search_fields = ('title',)
    list_filter = ('price',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'price', 'image')
    search_fields = ('title', 'artist')
    list_filter = ('price',)


@admin.register(MusicSet)
class MusicSetAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'image')
    search_fields = ('title',)
    list_filter = ('price',)


@admin.register(CoffeeMug)
class CoffeeMugAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'image')
    search_fields = ('title',)
    list_filter = ('price',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    search_fields = ('id',)
    list_filter = ('created_at',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product_type', 'product_id', 'quantity', 'size', 'color')
    search_fields = ('product_type', 'product_id')
    list_filter = ('cart', 'product_type', 'quantity', 'size', 'color')

