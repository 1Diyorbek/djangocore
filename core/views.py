from django.http import HttpResponse


def text_reward(request):
    """Terminal orqali kiritilgan teksni brouzerda ko'rsatish"""
    return HttpResponse(input("text kiriting: "))


def greet(request):
    """Bosh oynada salomlashish uchun"""
    return HttpResponse("Hi, on behalf of our group")