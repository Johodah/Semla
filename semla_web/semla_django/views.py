from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from django.contrib import messages
from django.utils import timezone
from .models import Semla, Rating
from .forms import RatingForm


def home(request):
    top_semlor = Semla.objects.annotate(
        avg_rating=Avg('ratings__score', default=0)
    ).order_by('-avg_rating')[:3]

    all_semlor = Semla.objects.all().annotate(
        avg_rating=Avg('ratings__score', default=0)
    )

    context = {
        'top_semlor': top_semlor,
        'all_semlor': all_semlor,
    }
    return render(request, 'semla_django/home.html', context)


def add_rating(request, semla_id):
    semla = get_object_or_404(Semla, id=semla_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.semla = semla
            rating.ip_address = request.META.get('REMOTE_ADDR', '0.0.0.0')
            rating.user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')

            try:
                if not Rating.can_rate(rating.ip_address, rating.user_agent):
                    messages.error(
                        request, 'Du har redan lagt till 5 betyg idag.')
                    return redirect('home')

                rating.save()
                messages.success(request, 'Tack för ditt betyg!')

            except Exception as e:
                messages.error(
                    request, 'Du har redan betygsatt denna semla idag.')

            return redirect('home')
    else:
        form = RatingForm()

    return render(request, 'semla_django/rate_semla.html', {
        'form': form,
        'semla': semla
    })
