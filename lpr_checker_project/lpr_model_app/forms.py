from django import forms


class ImageUploadForm(forms.Form):
    """
    Form to upload an image.
    """

    image = forms.ImageField()
