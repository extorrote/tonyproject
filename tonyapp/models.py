from django.db import models
from django.shortcuts import get_object_or_404




# Song model
class Song(models.Model):
    name = models.CharField(max_length=255)  # Name of the song
    file = models.FileField(upload_to='songs/')  # The actual audio file (MP3, etc.)
    background_image = models.ImageField(upload_to='song_images/', blank=True, null=True)  # Optional background image for each song

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"


# Post Index model
class Post_index(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    picture = models.ImageField(upload_to='posts_pictures/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


# Event model
class Event(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(blank=True, null=True)  # Only store the date
    time = models.TimeField(blank=True, null=True)  # Separate time field
    venue_name = models.CharField(max_length=200, blank=True, null=True)
    venue_address = models.CharField(max_length=300, blank=True, null=True)
    ticket_link = models.URLField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    special_notes = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"


# Music model
class Music(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='music_images/')
    description = models.TextField(blank=True, null=True)
    dropbox_link = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Music"
        verbose_name_plural = "Music"


# Videos model
class Videos(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='music_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    dropbox_link = models.URLField(max_length=1000, blank=True, null=True)
    youtube_link = models.TextField(default="", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"


# Gallery model
class Gallery(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    picture = models.ImageField(upload_to='posts_pictures/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Gallery Item"
        verbose_name_plural = "Gallery Items"


# Clothing model
class Clothing(models.Model):
    SIZES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]

    COLORS = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Black', 'Black'),
        ('White', 'White'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=2, choices=SIZES , blank=True,null=True)
    color = models.CharField(max_length=20, choices=COLORS, blank=True,null=True)
    image = models.ImageField(upload_to='clothing/',blank=True,null=True)
    image2=models.ImageField(upload_to='clothing/',blank=True,null=True)
    image3=models.ImageField(upload_to='clothing/',blank=True,null=True)
    image4=models.ImageField(upload_to='clothing/',blank=True,null=True)
    image5=models.ImageField(upload_to='clothing/',blank=True,null=True)
    image6=models.ImageField(upload_to='clothing/',blank=True,null=True)
    image7=models.ImageField(upload_to='clothing/',blank=True,null=True)
    image8=models.ImageField(upload_to='clothing/',blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Clothing Item"
        verbose_name_plural = "Clothing Items"


# Poster model
class Poster(models.Model):
    title = models.CharField(max_length=255)
    measures=models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='posters/',blank=True,null=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Poster"
        verbose_name_plural = "Posters"


# Album model
class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='albums/')
    songs = models.TextField(blank=True, null=True)  # List of songs in the album
    preview_link = models.URLField(blank=True, null=True)  # Preview link

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"


# Music Set model
class MusicSet(models.Model):
    title = models.CharField(max_length=255,blank=True, null=True)    
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='music_sets/')
    songs = models.TextField(blank=True, null=True)  # List of songs in the set
    duration = models.CharField(max_length=300 ,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    preview_link = models.URLField(blank=True, null=True)  # Preview link

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Music Set"
        verbose_name_plural = "Music Sets"


# Coffee Mug model
class CoffeeMug(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='coffeemugs/')  # Changed folder name from 'coffee_mugs' to 'coffeemugs'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Coffee Mug"
        verbose_name_plural = "Coffee Mugs"


# Cart Model
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id}"

    # Get total price of the cart
    def total_price(self):
        return sum(item.total_price() for item in self.cart_items.all())

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"


# CartItem Model
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    product_type = models.CharField(max_length=20)  # Could be 'clothing', 'poster', etc.
    product_id = models.IntegerField()  # ID of the product (Clothing, Poster, etc.)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=2, choices=Clothing.SIZES, null=True, blank=True)  # Size for clothing
    color = models.CharField(max_length=20, choices=Clothing.COLORS, null=True, blank=True)  # Color for clothing

    def __str__(self):
        return f"Item {self.product_type} {self.product_id} (x{self.quantity})"

    def total_price(self):
        # Calculate the total price of this item (unit price * quantity)
        product = self.get_product()
        return product.price * self.quantity

    def get_product(self):
        # Return the product based on the product type and id
        if self.product_type == 'clothing':
            return get_object_or_404(Clothing, id=self.product_id)
        elif self.product_type == 'poster':
            return get_object_or_404(Poster, id=self.product_id)
        elif self.product_type == 'album':
            return get_object_or_404(Album, id=self.product_id)
        elif self.product_type == 'musicset':  # Changed from 'music_set' to 'musicset'
            return get_object_or_404(MusicSet, id=self.product_id)
        elif self.product_type == 'coffeemug':  # Changed from 'coffee_mug' to 'coffeemug'
            return get_object_or_404(CoffeeMug, id=self.product_id)
        
        return None

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"
