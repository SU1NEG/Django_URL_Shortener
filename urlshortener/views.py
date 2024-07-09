# urlshortener/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import URL, Click
from .utils import generate_short_url

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home(request):
    ctx = {}
    if request.method == 'POST':
        original_url = request.POST['original_url']
        short_url = generate_short_url()
        while URL.objects.filter(short_url=short_url).exists():
            short_url = generate_short_url()
        url = URL(original_url=original_url, short_url=short_url)
        url.save()
        ctx['original_url'] = original_url
        ctx['short_url'] = short_url
    return render(request, 'shortener/home.html', context=ctx)

def redirect_to_original(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)

    # Click kaydı oluştur
    client_ip = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    timestamp = timezone.now()

    Click.objects.create(
        url=url,
        ip_address=client_ip,
        user_agent=user_agent,
        timestamp=timestamp
    )

    return redirect(url.original_url)
