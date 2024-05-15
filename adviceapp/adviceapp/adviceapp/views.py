from django.shortcuts import render
import requests
def home(request):
    return render(request,'advice.html')
def givea(request):
    data=requests.get('https://api.adviceslip.com/advice').json()
    advice=data['slip']['advice']
    return render(request,'yes.html',{"message":advice})
