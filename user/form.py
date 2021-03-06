from django import forms
from user.models import User
from annoying.functions import get_object_or_None

class UserLoginForm( forms.Form ):
    username = forms.CharField( required = True )
    password = forms.CharField( required = True )

    def clean( self ):
        cleaned_data = super().clean()
        username = cleaned_data.get( 'username' )
        password = cleaned_data.get( 'password' )
        s = get_object_or_None( User , username = username )
        if username and s is None:
            self.add_error( 'username' , 'Username not exists.' )
        if password and s and not s.check_password( password ):
            self.add_error( 'password' , 'Password is wrong' )

class UserSignupForm( forms.Form ):
    username = forms.CharField( required = True , max_length = 16 , min_length = 4 )
    password = forms.CharField( required = True , max_length = 20 , min_length = 6 )
    email = forms.EmailField( required = True )
    display_name = forms.CharField( required = True , max_length = 12 )
    school = forms.CharField( required = False , max_length = 60 )
    company = forms.CharField( required = False , max_length = 32 )
    location = forms.CharField( required = False , max_length = 32 )

    def clean( self ):
        from re import compile, search
        cleaned_data = super().clean()
        email = cleaned_data.get( 'email' )
        username = cleaned_data.get( 'username' )
        password = cleaned_data.get( 'password' )
        display_name = cleaned_data.get( 'display_name' )
        if username and get_object_or_None( User , username = username ) is not None:
            self.add_error( 'username' , 'Username already exists.' )
        if password and compile( '[a-zA-Z]' ).search( password ) is None:
            self.add_error( 'password' , 'Password should contain at least one lowercase or uppercase letter.' )
        if email and get_object_or_None( User , email = email ) is not None:
            self.add_error( 'email' , 'Email already exists.' )
        if display_name and get_object_or_None( User , display_name = display_name ) is not None:
            self.add_error( 'display_name' , 'Display name already exists.' )

class UserinfoForm( forms.Form ):
    about = forms.CharField( required = False , max_length = 256 )
    school = forms.CharField( required = False , max_length = 60 )
    company = forms.CharField( required = False , max_length = 32 )
    location = forms.CharField( required = False , max_length = 32 )
    display_name = forms.CharField( required = True , max_length = 16 )

    def _clean( self , pre_display_name ):
        cleaned_data = super().clean()
        display_name = cleaned_data.get( 'display_name' )
        if display_name and display_name != pre_display_name and get_object_or_None( User , display_name = display_name ) is not None:
            self.add_error( 'display_name' , 'Display name already exists.' )
            return False
        return True