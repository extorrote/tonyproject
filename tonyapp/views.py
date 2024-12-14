from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from .models import Song, Post_index,Event,Music,Videos,Gallery,Song, Clothing, Poster, Album, MusicSet, CoffeeMug, Cart, CartItem
from .forms import Post_indexForm ,EventForm ,MusicForm,VideoForm,GalleryForm,SongForm

def index(request):
    songs = Song.objects.all()
    posts = Post_index.objects.all()  # Fetch all posts

    return render(request, 'index.html', {'songs': songs, 'posts': posts})

from django.contrib.auth import authenticate,login,logout
def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')#ESTO ES LO QUE LE HE PUESTO EN EL NAME EN EL CAMPO DEL FORMULARIO
        user=authenticate(request,username=username,password=password)#KEYBOL ARGUMENT ES CUANDO VA UN LA PRIMERA ES LA KEIBOLNAME  NOMBRE=NOMBRE LA SEGUNDA ES LA VARIABLE QUE ESTA RECIBIENDO
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.warning (request,'No te has identificado Correctamente')


    return render (request,'login.html',{'title':'identificate'})


def logout_user(request):
    logout(request)
    return redirect ('index')





def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('music_player')  # Redirect to your music player page after saving
    else:
        form = SongForm()

    return render(request, 'upload_song.html', {'form': form})


def create_post_index(request):
    if request.method == 'POST':
        form = Post_indexForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the new post to the database
            return redirect('index')  # Redirect to the index page after posting
    else:
        form = Post_indexForm()

    return render(request, 'create_post_index.html', {'form': form})




def biography(request):
    return render(request,'biography.html')




from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages


from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            # Define a list of recipient emails
            recipient_list = ['wwwstephen95live@gmail.com']

            # Create the email subject
            subject = f'Contact Form Submission from {name}'

            # Create the HTML message
            html_message = f"""
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        margin: 0;
                        padding: 20px;
                    }}
                    .container {{
                        max-width: 600px;
                        margin: auto;
                        background: #D99F59; /* Main color */
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                    }}
                    h1 {{
                        color: #ffffff; /* White text for contrast */
                    }}
                    p {{
                        font-size: 16px;
                        color: #333; /* Dark text for readability */
                    }}
                    .footer {{
                        margin-top: 20px;
                        font-size: 14px;
                        text-align: center;
                        color: #ffffff; /* White footer text */
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Hemos Recibido tu Mensaje!</h1>
                    <p><strong>Nombre:</strong> {name}</p>
                    <p><strong>Email:</strong> {email}</p>
                    <p><strong>Teléfono:</strong> {phone}</p>
                    <p><strong>Mensaje:</strong></p>
                    <p>{message}</p>
                    <div class="footer">
                        <p>thank you for getting in touch with  www.tonylatinrascal.com,  we'll get back to you as soon as we could.</p>
                    </div>
                </div>
            </body>
            </html>
            """

            # Create and send the email
            email = EmailMultiAlternatives(subject, strip_tags(html_message), 'tonymoranmusic@gmail.com', recipient_list)
            email.attach_alternative(html_message, "text/html")
            email.send(fail_silently=False)

            messages.success(request, '¡Thank you for Getting in touch! your Message has been sent.')
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})


# views.py



def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('schedule')
    else:
        form = EventForm()

    return render(request, 'create_event.html', {'form': form})

def schedule(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'schedule.html', {'events': events})


def contact(request):
    return render(request,'contact.html')


def discography(request):
    return render (request,'discography.html')




def post_song(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the Music object to the database
            return redirect('music_section_list')  # Redirect to a success page or list view

    else:
        form = MusicForm()

    return render(request, 'post_music_section.html', {'form': form})





def view_songs(request):
    songs = Music.objects.all()
    
    # Preprocess the Dropbox links to add the necessary modification
    for song in songs:
        # Replace the Dropbox domain to get the raw file URL
        if "dropbox.com" in song.dropbox_link:
            song.raw_dropbox_link = song.dropbox_link.replace("www.dropbox.com", "dl.dropboxusercontent.com") + "?raw=1"
        else:
            song.raw_dropbox_link = song.dropbox_link  # Keep original if already in correct format
    
    return render(request, 'music_list.html', {'songs': songs})






def post_video(request):
    if request.method == 'POST':
        form=VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('index')
    else:
        form=VideoForm()
    return render(request,'post_video.html',{'form': form})


def view_videos(request):
    videos=Videos.objects.all()
    return render (request,'display_youtube_video.html', {'videos':videos})




def post_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery_list')  # After saving, redirect to the gallery list view
    else:
        form = GalleryForm()
    return render(request, 'post_gallery.html', {'form': form})


# views.py
def gallery_list(request):
    galleries = Gallery.objects.all()
    return render(request, 'gallery_list.html', {'galleries': galleries})


def faq(request):
    return render(request,'faq.html')







from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from .models import Cart, CartItem, Clothing, Poster, Album, MusicSet, CoffeeMug

def product_list(request, product_type=None):
    # If no specific product_type is passed, show all products
    if not product_type:
        clothing = Clothing.objects.all()
        posters = Poster.objects.all()
        albums = Album.objects.all()
        musicsets = MusicSet.objects.all()
        coffeemugs = CoffeeMug.objects.all()

        # Combine all products into a single list
        products = list(clothing) + list(posters) + list(albums) + list(musicsets) + list(coffeemugs)
    else:
        # Filter products based on the category selected
        if product_type == 'clothing':
            products = Clothing.objects.all()
        elif product_type == 'poster':
            products = Poster.objects.all()
        elif product_type == 'album':
            products = Album.objects.all()
        elif product_type == 'musicset':  # Changed from 'music_set' to 'musicset'
            products = MusicSet.objects.all()
        elif product_type == 'coffeemug':  # Changed from 'coffee_mug' to 'coffeemug'
            products = CoffeeMug.objects.all()
        else:
            return JsonResponse({'error': 'Invalid product type'}, status=400)

    # Add product type to each product
    for product in products:
        product.product_type = product.__class__.__name__.lower()  # Add the class name as a lowercase string

    context = {
        'products': products,
        'product_type': product_type,
    }
    return render(request, 'store.html', context)


def add_to_cart(request, product_type, product_id):
    # Get or create a cart (without requiring login, use session)
    cart, created = Cart.objects.get_or_create(id=request.session.get('cart_id'))

    # Get the correct product
    if product_type == 'clothing':
        product = Clothing.objects.get(id=product_id)
    elif product_type == 'poster':
        product = Poster.objects.get(id=product_id)
    elif product_type == 'album':
        product = Album.objects.get(id=product_id)
    elif product_type == 'musicset':
        product = MusicSet.objects.get(id=product_id)
    elif product_type == 'coffeemug':
        product = CoffeeMug.objects.get(id=product_id)
    else:
        return JsonResponse({'error': 'Invalid product type'}, status=400)

    # Handle multiple quantities
    quantity = int(request.POST.get('quantity', 1))
    size = request.POST.get('size', None)
    color = request.POST.get('color', None)

    # Create new CartItems based on the quantity, size, and color selected
    for _ in range(quantity):
        CartItem.objects.create(
            cart=cart,
            product_type=product_type,
            product_id=product_id,
            size=size,  # Size for each new item
            color=color,  # Color for each new item
            quantity=1  # Each CartItem represents one unit, so quantity is 1
        )

    # Save cart in session for persistent access
    request.session['cart_id'] = cart.id

    return redirect('view_cart')



def view_cart(request):
    cart_id = request.session.get('cart_id')

    if not cart_id:
        return render(request, 'view_cart.html', {'cart_items': [], 'cart': None})

    try:
        cart = Cart.objects.get(id=cart_id)
        cart_items = cart.cart_items.all()
    except Cart.DoesNotExist:
        del request.session['cart_id']
        return render(request, 'view_cart.html', {'cart_items': [], 'cart': None})

    if request.method == 'POST':
        # Handle size and color updates for clothing items
        item_id = request.POST.get('item_id')
        size = request.POST.get('size')
        color = request.POST.get('color')

        try:
            cart_item = CartItem.objects.get(id=item_id, cart=cart)
            if cart_item.product_type == 'clothing':
                if size:
                    cart_item.size = size
                if color:
                    cart_item.color = color
                cart_item.save()
        except CartItem.DoesNotExist:
            return HttpResponse("Cart item not found", status=404)

        return redirect('view_cart')  # Refresh the page to see updates

    # Create a list of indices for each unit of the product based on quantity
    for item in cart_items:
        item.unit_indices = list(range(1, item.quantity + 1))  # Create list from 1 to quantity

    return render(request, 'view_cart.html', {'cart_items': cart_items, 'cart': cart})






def update_cart_item(request, item_id): 
    try:
        cart_item = CartItem.objects.get(id=item_id)
    except CartItem.DoesNotExist:
        return HttpResponse("Cart item not found", status=404)

    if request.method == 'POST':
        # Get the new quantity from the POST data, default to the current quantity if not specified
        new_quantity = int(request.POST.get('quantity', cart_item.quantity))

        # If the quantity has increased and the product is clothing, create additional items
        if new_quantity > cart_item.quantity:
            additional_quantity = new_quantity - cart_item.quantity

            # If the product is clothing, add new CartItems for each extra quantity
            if cart_item.product_type == 'clothing':
                for _ in range(additional_quantity):
                    CartItem.objects.create(
                        cart=cart_item.cart,
                        product_type=cart_item.product_type,
                        product_id=cart_item.product_id,
                        size=cart_item.size,  # Copy size from original
                        color=cart_item.color,  # Copy color from original
                        quantity=1  # New item will have quantity 1
                    )
            else:
                # For non-clothing products, simply update the quantity
                cart_item.quantity = new_quantity
                cart_item.save()

        # If the quantity is decreased, update the original CartItem's quantity
        elif new_quantity < cart_item.quantity:
            cart_item.quantity = new_quantity
            cart_item.save()

        else:
            # No quantity change needed, just save the existing CartItem
            cart_item.save()

        # Handle size and color updates if provided (only applicable for clothing)
        size = request.POST.get('size')
        color = request.POST.get('color')

        # Update size and color if provided by the user, only for clothing items
        if cart_item.product_type == 'clothing':
            if size:
                cart_item.size = size
            if color:
                cart_item.color = color

        # Save the updated CartItem
        cart_item.save()

    return redirect('view_cart')













# Remove item from cart
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()

    return redirect('view_cart')








import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Cart, CartItem
from .forms import UserInfoForm  # Assuming you placed the form in forms.py

stripe.api_key = settings.STRIPE_LIVE_SECRET_KEY

def checkout(request):
    # Retrieve the cart from the session
    cart_id = request.session.get('cart_id')
    if not cart_id:
        return redirect('view_cart')  # Redirect to cart if no cart is found
    
    cart = Cart.objects.get(id=cart_id)
    cart_items = cart.cart_items.all()

    # Calculate the total price of the cart
    total_price = cart.total_price()

    # Handle the form submission
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            # Save user info to the session
            user_info = form.cleaned_data
            request.session['user_info'] = user_info

            # Create a new Checkout Session
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': item.get_product().title,
                            },
                            'unit_amount': int(item.get_product().price * 100),  # Stripe requires price in cents
                        },
                        'quantity': item.quantity,  # Stripe automatically handles quantity
                    }
                    for item in cart_items
                ],
                mode='payment',
                success_url=request.build_absolute_uri('/checkout/success/'),
                cancel_url=request.build_absolute_uri('/checkout/cancel/'),
            )

            return redirect(session.url, code=303)
        else:
            # Form is invalid, re-render the checkout page with the form errors
            return render(request, 'checkout.html', {
                'cart_items': cart_items,
                'total_price': total_price,
                'stripe_public_key': settings.STRIPE_LIVE_PUBLIC_KEY,
                'form': form,
            })
    
    # If it's a GET request, just render the form
    else:
        form = UserInfoForm()

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'stripe_public_key': settings.STRIPE_LIVE_PUBLIC_KEY,
        'form': form,
    })








from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from email.mime.image import MIMEImage
from django.shortcuts import render, redirect
from django.contrib.staticfiles import finders
from .models import Cart

def checkout_success(request):
    # Retrieve the cart ID and user information from the session
    cart_id = request.session.get('cart_id')
    user_info = request.session.get('user_info')

    if cart_id and user_info:
        # Get the cart and its items
        try:
            cart = Cart.objects.get(id=cart_id)
            cart_items = cart.cart_items.all()  # Retrieve cart items
            
            # Calculate the total price of the cart
            total_price = cart.total_price()  # Assuming you have a method to calculate total price

            # Render the HTML email template with user and cart details
            email_subject = 'Order Confirmation - Thank you for your purchase!'
            email_body = render_to_string('user_notification.html', {
                'user_info': user_info,
                'cart_items': cart_items,
                'total_price': total_price,
            })

            # Find the logo image using the static files finder
            logo_path = finders.find('images/logo_latin_rascals.png')

            if not logo_path:
                raise FileNotFoundError('Logo image not found in the static directory.')

            # Create an EmailMessage object
            email = EmailMessage(
                email_subject,  # Subject of the email
                email_body,     # Body of the email
                settings.DEFAULT_FROM_EMAIL,  # Sender's email
                [user_info.get('email'), 'tonymoranmusic@gmail.com'],  # Recipient email
            )

            # Attach the logo image as inline (static) image
            with open(logo_path, 'rb') as logo_file:
                logo_image = MIMEImage(logo_file.read())
                logo_image.add_header('Content-ID', '<logo>')  # Use a unique content ID to refer in HTML
                email.attach(logo_image)  # Attach the image to the email

            # Send the email with the embedded logo
            email.content_subtype = "html"  # Set the content type to HTML
            email.send()

            # Clear the cart and session data after the purchase
            cart.cart_items.all().delete()  # Remove all items from the cart
            cart.delete()  # Delete the cart itself

            # Clear session variables
            del request.session['cart_id']
            del request.session['user_info']

            # Return the success page with the purchase details
            return render(request, 'checkout_success.html', {
                'cart_items': cart_items,
                'total_price': total_price,
                'user_info': user_info,
                'message': 'Your payment was successful! Thank you for your purchase.',
            })
        except Cart.DoesNotExist:
            # Handle the case when the cart is not found
            return redirect('view_cart')
    else:
        # Redirect to the cart if session data is missing
        return redirect('view_cart')








def checkout_cancel(request):
    return render(request, 'checkout_cancel.html', {
        'message': 'Your payment was canceled. Please try again.'
    })







from .forms import ClothingForm, PosterForm, AlbumForm, MusicSetForm, CoffeeMugForm

# Create Clothing Product
def create_clothing(request):
    if request.method == 'POST':
        form = ClothingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list', product_type='clothing')  # Redirect to the clothing list page
    else:
        form = ClothingForm()
    return render(request, 'create_product.html', {'form': form, 'product_type': 'Clothing'})

# Create Poster Product
def create_poster(request):
    if request.method == 'POST':
        form = PosterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list', product_type='poster')  # Redirect to the posters list page
    else:
        form = PosterForm()
    return render(request, 'create_product.html', {'form': form, 'product_type': 'Poster'})

# Create Album Product
def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list', product_type='album')  # Redirect to the albums list page
    else:
        form = AlbumForm()
    return render(request, 'create_product.html', {'form': form, 'product_type': 'Album'})

# Create Music Set Product
def create_music_set(request):
    if request.method == 'POST':
        form = MusicSetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the music sets list page
    else:
        form = MusicSetForm()
    return render(request, 'create_product.html', {'form': form, 'product_type': 'Music Set'})

# Create Coffee Mug Product
def create_coffee_mug(request):
    if request.method == 'POST':
        form = CoffeeMugForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list', product_type='coffee_mug')  # Redirect to the coffee mugs list page
    else:
        form = CoffeeMugForm()
    return render(request, 'create_product.html', {'form': form, 'product_type': 'Coffee Mug'})






def about_us(request):
    return render(request,'about_us.html')


def terms_and_conditions(request):
    return render (request, 'terms_and_conditions.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')
