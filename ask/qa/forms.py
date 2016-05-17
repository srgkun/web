from django import forms

class AskForm(forms.Form):
    title=forms.CharField(max_length=200)
    text=forms.CharField()

class AnswerForm(forms.Form):
    text=forms.CharField()
    question=forms.CharField()
