from django.shortcuts import render


def mainpage(request):
	return render(request, 'mainpage/main_page.html')
