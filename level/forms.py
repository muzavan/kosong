from django import forms

class NewLevelForm(forms.Form):
	image = forms.FileField(label='Image (*.png, *.jpg)')
	answer = forms.CharField(label='Answer',widget=forms.TextInput(attrs={"class" : "form-control","placeholder" :"What song is represented by the image?","required" :"true"}))
	hint = forms.CharField(label='Hint',widget=forms.TextInput(attrs={"class" : "form-control","placeholder" :"What can you say to help people guess?","required" :"true"}))
	name = forms.CharField(label='Your Name',widget=forms.TextInput(attrs={"class" : "form-control","placeholder" :"Your name here","required" :"true"}))
	linkProfile = forms.CharField(label='Your Twitter Username',widget=forms.TextInput(attrs={"class" : "form-control","placeholder" :"yourusername (not using @)","required" :"true"}))

