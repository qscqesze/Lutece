from django import forms

class BasicBlogForm( forms.Form ):
    title = forms.CharField( required = True , max_length = 128 )
    content = forms.CharField( required = False , max_length = 65535 )