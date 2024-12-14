from django import forms
from .models import Song, Post_index,Music,Videos,Gallery

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'file', 'background_image']
        
        
        
        


class Post_indexForm(forms.ModelForm):
    class Meta:
        model = Post_index  # Update model reference
        fields = ['title', 'picture', 'description']
        
        
        
        
        
        
        
        
from django import forms
from django.core.validators import RegexValidator
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()    
    phone = forms.CharField(
        max_length=15, 
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$', 
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )]
    )
    message = forms.CharField(widget=forms.Textarea)
    
    
    
    # forms.py

from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    # Adding a separate field for time
    time = forms.TimeField(widget=forms.TextInput(attrs={'class': 'timepicker'}))  # Custom class for timepicker

    class Meta:
        model = Event
        fields = ['title', 'date', 'time', 'venue_name', 'venue_address', 'ticket_link', 'description', 'duration', 'special_notes', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Standard date input
        }
        
        
        
        
        


from django.core.exceptions import ValidationError
import re

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'image', 'description', 'dropbox_link']

    def clean_dropbox_link(self):
        dropbox_link = self.cleaned_data['dropbox_link']

        # Check if the URL contains 'dropbox.com' and allow various formats
        if "dropbox.com" not in dropbox_link:
            raise ValidationError("This is not a valid Dropbox link.")
        
        # Check if the URL is a valid shared link (including ?dl=0 or ?raw=1)
        if not any(param in dropbox_link for param in ["?dl=", "?raw=", "?e=", "?preview="]):
            raise ValidationError("The Dropbox link must contain proper parameters like '?dl=0' or '?raw=1'.")
        
        return dropbox_link









class VideoForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ['title', 'image', 'description', 'dropbox_link', 'youtube_link']

    youtube_link = forms.CharField(required=False, widget=forms.Textarea, label="Link de YouTube (Iframe)")

    def clean_dropbox_link(self):
        dropbox_link = self.cleaned_data.get('dropbox_link')  # Use get to handle None safely

        # Only validate the dropbox link if it is provided (i.e., not empty)
        if dropbox_link:
            # Check if the URL contains 'dropbox.com' and allow various formats
            if "dropbox.com" not in dropbox_link:
                raise ValidationError("This is not a valid Dropbox link.")
            
            # Check if the URL is a valid shared link (including ?dl=0 or ?raw=1)
            if not any(param in dropbox_link for param in ["?dl=", "?raw=", "?e=", "?preview="]):
                raise ValidationError("The Dropbox link must contain proper parameters like '?dl=0' or '?raw=1'.")

        # If no dropbox link is provided, just return the data as-is (allowing empty)
        return dropbox_link

    def clean_youtube_link(self):
        link = self.cleaned_data.get('youtube_link')
        if link:  # Only validate if there's a link
            # Validate if it's a proper YouTube URL
            if not link.startswith("https://www.youtube.com/") and "youtube.com" not in link:
                raise forms.ValidationError('Invalid YouTube link. Ensure it is a valid YouTube URL.')
        return link





class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'picture']
        
        
        
        


from .models import Clothing, Poster, Album, MusicSet, CoffeeMug

# Form for Clothing
class ClothingForm(forms.ModelForm):
    class Meta:
        model = Clothing
        fields = ['title', 'description', 'price', 'image', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8']

# Form for Poster
class PosterForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = ['title', 'measures' ,'description', 'price', 'image',]

# Form for Album
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields= '__all__'
        labels= {'title':'Title', 'artist':'Artist', 'description':'Description', 'price':'Price', 'image':'Album Cover', 'songs':'Songs list', 'preview_link':'Dropbox Preview Link'}

# Form for MusicSet
class MusicSetForm(forms.ModelForm):
    class Meta:
        model = MusicSet
        fields = '__all__'
        labels= {'title':'Title', 'price':'Price', 'image':'Cover Image', 'songs':'Song List','duration':'Set Duration', 'description':'Description','preview_link': 'Dropbox Preview Link'}
        

# Form for Coffee Mug
class CoffeeMugForm(forms.ModelForm):
    class Meta:
        model = CoffeeMug
        fields = ['title', 'description', 'price', 'image']
        
        
        
        


class UserInfoForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    city = forms.CharField(max_length=100, required=True)
    state = forms.CharField(max_length=100, required=True)
    postal_code = forms.CharField(max_length=20, required=True)
    country = forms.CharField(max_length=100, required=True)
    any_extra_information=forms.CharField(max_length=100, required=False)
