from django import forms
from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['rating', 'headline', 'body']
        CHOICES = (
            (0, ' 0'),
            (1, ' 1'),
            (2, ' 2'),
            (3, ' 3'),
            (4, ' 4'),
            (5, ' 5'),
        )
        widgets = {
            'rating': forms.RadioSelect(
                choices=CHOICES,
                attrs={'class': 'form-check-inline'}),
            # 'rating': forms.IntegerField(widget=Stars),
            'headline': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }


class FollowForm(forms.ModelForm):
    class Meta:
        model = models.UserFollows
        fields = ['user', 'followed_user']
