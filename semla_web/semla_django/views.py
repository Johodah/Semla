from django.shortcuts import render, redirect
from django.db.models import Avg
from django.contrib import messages
from django.utils import timezone
from .models import Semla, Rating
from .forms import RatingForm


def home(request):
    top_semlor = Semla.objects.annotate(
        avg_rating=Avg('ratings__score')
    ).order_by('-avg_rating')[:3]

    all_semlor = Semla.objects.all()

    context = {
        'top_semlor': top_semlor,
        'all_semlor': all_semlor,
    }
    return render(request, 'semla_django/home.html', context)


def add_rating(request, semla_id):
    semla = Semla.objects.get(id=semla_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.semla = semla
            rating.ip_address = request.META.get('REMOTE_ADDR')
            rating.user_agent = request.META.get('HTTP_USER_AGENT', '')

            # Check daily limit using the model method
            if not Rating.can_rate(rating.ip_address, rating.user_agent):
                messages.error(request, 'Du har redan lagt till 5 betyg idag.')
                return redirect('home')

            try:
                rating.save()
                messages.success(request, 'Tack för ditt betyg!')
            except:
                messages.error(
                    request, 'Du har redan betygsatt denna semla idag.')
            return redirect('home')
    else:
        form = RatingForm()

    return render(request, 'semla_django/rate_semla.html', {
        'form': form,
        'semla': semla
    })
