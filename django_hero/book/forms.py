from django import forms

class CharacterForm(forms.Form):
    name = forms.CharField(label='Ton nom dans la street', max_length=100, required=True)
    age = forms.IntegerField(label='Ton age - 6')
    CHOICES=[
        ('', 'Choisis une marque'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
        ('default', 'NordVPN'),
    ]
    brand = forms.ChoiceField(label='Ta marque préférée (répond NordVPN le jeu est sponso)', choices=CHOICES, required=True)
