from django import forms


class PostForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'required': True,
                'maxlength': 100
            }
        ),
        max_length=100
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'required': True,
                'rows': 4,
                'cols': 50
            }
        )
    )


class CommentForm(forms.Form):
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'required': False,
                'rows': 5,
                'cols': 25
            }
        ),
        max_length=100
    )
