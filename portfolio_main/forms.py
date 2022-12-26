from django import forms
from .models import *

class ProjectsForm(forms.ModelForm):
    nm = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form_control',
        'placeholder': 'Nome do Projeto',
        'id':'name'}), required=True)

    img_url = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form_control',
        'placeholder': 'URL da imagem',
        'id':'image_url'}), required=True)

    tec_us = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form_control',
        'placeholder': 'Tecnologias usadas',
        'id': 'tec_us'}), required=True)

    repo = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form_control',
        'placeholder': 'Link do Repositorio',
        'id': 'repo'}), required=True)

    dep = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form_control',
        'placeholder': 'Foi feito deploy?',
        'id': 'dep'}), required=True)

    dep_link = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form_control',
        'placeholder': 'Link do Deploy',
        'id': 'dep_link'}), required=False)

    desc = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form_control',
        'placeholder': 'Descrição do Projeto',
        'id':'project_desc'}), required=True)



    class Meta:
        model = ProjectsModel
        fields = '__all__'