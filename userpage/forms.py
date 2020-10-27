from django import forms

class Trymsg(forms.Form):
    msg = forms.CharField(
        label='Pesan', 
        max_length=50,
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder' : 'ketikan pesan yang hendak anda kirim',
            }
        )
    )