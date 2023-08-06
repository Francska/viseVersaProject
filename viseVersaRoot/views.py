from django.http import HttpResponse
from django.shortcuts import render


def viseversa (request):
	return render (request, 'viseversa.html')