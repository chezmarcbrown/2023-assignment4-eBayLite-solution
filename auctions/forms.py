
from xml.etree.ElementTree import Comment
from django import forms
from django.core.exceptions import ValidationError

from .models import Listing, Bid, Comment

class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ('title', 'description', 'starting_bid', 'categories', 'image') 
        labels = {
            'starting_bid': "Starting bid (in USD)",
        }

class BidForm(forms.ModelForm):

    class Meta:
        model = Bid
        fields = ('amount', ) 
        labels = {
            'amount': "Amount of bid (in USD)",
        }

    def set_minimum_bid(self, value):
        self.minimum_bid = value

    def clean_amount(self):
        value = int(self.cleaned_data['amount'])
        if value < self.minimum_bid:
            raise ValidationError(f'Bid is too low; must be at least ${self.minimum_bid}')
        return value
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', )

from django.contrib.auth.forms import PasswordResetForm
class MyPasswordResetForm(PasswordResetForm):
   def is_valid(self):
       email = self.data["email"]
       if sum([1 for u in self.get_users(email)]) == 0:
           self.add_error(None, "Unknown email; try again")
           return False
       return super().is_valid()
