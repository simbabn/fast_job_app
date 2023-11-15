from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    ville = forms.CharField(label="", max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ville'}))
    age = forms.IntegerField(label="", required=False, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Age'}))
    experiences = forms.CharField(label="", max_length=1000, required=False, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Expériences'}))
    formations = forms.CharField(label="", max_length=1000, required=False, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Formations'}))
    metiers_recherches = forms.CharField(label="", max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Métiers Recherchés'}))
    compte_linkedin = forms.URLField(label="", required=False, widget=forms.URLInput(attrs={'class':'form-control', 'placeholder':'Compte LinkedIn'}))
    compte_twitter = forms.CharField(label="", max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Compte Twitter'}))
    compte_github = forms.URLField(label="", required=False, widget=forms.URLInput(attrs={'class':'form-control', 'placeholder':'Compte GitHub'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'ville', 'age', 'experiences', 'formations', 'metiers_recherches', 'compte_linkedin', 'compte_twitter', 'compte_github')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

  
class UserProfileForm(UserChangeForm):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ville = forms.CharField(label="Ville", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label="Age", required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    experiences = forms.CharField(label="Expériences", max_length=1000, required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    formations = forms.CharField(label="Formations", max_length=1000, required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    metiers_recherches = forms.CharField(label="Métiers Recherchés", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    compte_linkedin = forms.URLField(label="Compte LinkedIn", required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    compte_twitter = forms.CharField(label="Compte Twitter", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    compte_github = forms.URLField(label="Compte GitHub", required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'ville', 'age', 'experiences', 'formations', 'metiers_recherches', 'compte_linkedin', 'compte_twitter', 'compte_github')

class OffreEmploiFilterForm(forms.Form):
    keywords = forms.CharField(label="Mots-clés", required=False)
    type_contrat = forms.CharField(label="Type de contrat", required=False)
    lieu_travail = forms.CharField(label="Lieu de travail", required=False)
    duree_contrat = forms.CharField(label="Durée du contrat", required=False)
    alternance = forms.ChoiceField(
        label="Alternance",
        choices=[('', 'Tous'), ('Oui', 'Oui'), ('Non', 'Non')],
        required=False
    )
    
