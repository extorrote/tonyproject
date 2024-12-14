


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    product_type = models.CharField(max_length=20)  # Could be 'clothing', 'poster', etc.
    product_id = models.IntegerField()  # ID of the product (Clothing, Poster, etc.)
    quantity = models.PositiveIntegerField(default=1)
    
    # These fields are only relevant for clothing items
    size = models.CharField(max_length=10, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X-Large')], null=True, blank=True)
    color = models.CharField(max_length=20, choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('black', 'Black')], null=True, blank=True)

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
        elif self.product_type == 'music_set':
            return get_object_or_404(MusicSet, id=self.product_id)
        elif self.product_type == 'coffee_mug':
            return get_object_or_404(CoffeeMug, id=self.product_id)
        return None
    
    
    
    
    
    ### VISTA VIEW_CART 
    
    from django.shortcuts import render, redirect
from .models import Cart, CartItem

def view_cart(request):
    # Get the cart ID from the session
    cart_id = request.session.get('cart_id')
    
    # Check if the cart ID exists and is valid
    if not cart_id:
        return render(request, 'view_cart.html', {'cart_items': [], 'cart': None})
    
    try:
        cart = Cart.objects.get(id=cart_id)
        cart_items = cart.cart_items.all()
    except Cart.DoesNotExist:
        # If the cart does not exist, clear the session and show an empty cart
        del request.session['cart_id']  # Remove invalid cart ID from session
        return render(request, 'view_cart.html', {'cart_items': [], 'cart': None})

    # Handle POST request to update the cart
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        size = request.POST.get('size')
        color = request.POST.get('color')
        quantity = int(request.POST.get('quantity'))

        try:
            item = CartItem.objects.get(id=item_id)
            if item.product_type == 'clothing':  # Only update size and color for clothing
                if size:
                    item.size = size
                if color:
                    item.color = color
            item.quantity = quantity
            item.save()
        except CartItem.DoesNotExist:
            pass  # Handle item not found

        # Redirect to avoid resubmitting the form on page refresh
        return redirect('view_cart')

    return render(request, 'view_cart.html', {'cart_items': cart_items, 'cart': cart})








### TEMPLEATE

<h1>Your Cart</h1>

{% if cart_items %}
    {% for item in cart_items %}
        <div>
            <h3>{{ item.get_product.title }}</h3>
            <p>Price: ${{ item.total_price }}</p>
            
            <!-- Check if the product is of type 'clothing' -->
            {% if item.product_type == 'clothing' %}
                <form action="{% url 'update_cart_item' item.id %}" method="POST">
                    {% csrf_token %}
                    <label for="size">Size:</label>
                    <select name="size" id="size">
                        <option value="S" {% if item.size == 'S' %}selected{% endif %}>Small</option>
                        <option value="M" {% if item.size == 'M' %}selected{% endif %}>Medium</option>
                        <option value="L" {% if item.size == 'L' %}selected{% endif %}>Large</option>
                        <option value="XL" {% if item.size == 'XL' %}selected{% endif %}>X-Large</option>
                    </select>

                    <label for="color">Color:</label>
                    <select name="color" id="color">
                        <option value="red" {% if item.color == 'red' %}selected{% endif %}>Red</option>
                        <option value="blue" {% if item.color == 'blue' %}selected{% endif %}>Blue</option>
                        <option value="green" {% if item.color == 'green' %}selected{% endif %}>Green</option>
                        <option value="black" {% if item.color == 'black' %}selected{% endif %}>Black</option>
                    </select>

                    <label for="quantity">Quantity:</label>
                    <input type="number" name="quantity" value="{{ item.quantity }}" min="1">

                    <button type="submit">Update</button>
                </form>
            {% else %}
                <!-- Non-clothing products (only quantity selector) -->
                <form action="{% url 'update_cart_item' item.id %}" method="POST">
                    {% csrf_token %}
                    <input type="number" name="quantity" value="{{ item.quantity }}" min="1">
                    <button type="submit">Update Quantity</button>
                </form>
            {% endif %}

            <!-- Remove Item Form -->
            <form action="{% url 'remove_from_cart' item.id %}" method="POST">
                {% csrf_token %}
                <button type="submit">Remove</button>
            </form>
        </div>
    {% endfor %}
    
    <h2>Total Price: ${{ cart.total_price }}</h2>

    <!-- Checkout Button -->
    <form action="{% url 'checkout' %}" method="POST">
        {% csrf_token %}
        <button type="submit" id="checkout-button">Proceed to Checkout</button>
    </form>
{% else %}
    <p>Your cart is empty. Add some items to your cart before proceeding to checkout.</p>
{% endif %}
