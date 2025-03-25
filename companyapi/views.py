from django.shortcuts import HttpResponse

def home_page(request):
    print("Home page")
    return HttpResponse("This i s home Page")