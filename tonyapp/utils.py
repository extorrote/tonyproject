from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from urllib.parse import urljoin
from django.contrib.auth.models import User




def purchase_notification(property, property_url): 
    users = User.objects.all()  # Get all users (you may want to filter this)
    subject = '¡Acabamos de Agregar un Terreno en Venta!'

    # Loop through users and send them a personalized email
    for user in users:
        # Ensure we get the absolute URL for the logo image
        logo_url = urljoin(settings.SITE_URL, '/static/images/logo_agente.png')  # Update path to logo

        # Ensure we get the absolute URL for the property image
        image_url = urljoin(settings.SITE_URL, property.imagen1.url) if property.imagen1 else None

        # Prepare the context for the email, including the user and agent object
        context = {
            'user': user,               # Pass the user object to access first_name
            'property': property,       # Pass the property details
            'property_url': property_url,  # Pass the property URL
            'agent_name': property.agente.nombre,  # Assuming 'nombre' field in Agente model
            'image_url': image_url,     # Include the full image URL for property image
            'logo_url': logo_url        # Include the full URL for the logo image
        }

        # Render the email content from the template with the context
        message = render_to_string('notify_users_terrenos.html', context)

        # Send the email to the user
        send_mail(
            subject,
            message,
            'www.tonylatinrascal.com',  # Sender's email
            [user.email],  # Recipient's email
            html_message=message ) # HTML version of the email
