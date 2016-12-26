from django import forms

from .models import _video

class _videoForm(forms.ModelForm):

    class Meta:
        model = _video
        fields = ('username', 'user_email', 'video_path')