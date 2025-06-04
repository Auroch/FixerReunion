from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Demande
from .ai_engine import suggest_meeting

@login_required
def create_meeting(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        demande = Demande.objects.create(titre=titre, organisateur=request.user)
        date, lieu = suggest_meeting(demande)
        demande.date = date
        demande.lieu = lieu
        demande.save()
        return redirect('inviter', demande_id=demande.id)
    return render(request, 'scheduler_app/create_meeting.html')

@login_required
def inviter(request, demande_id):
    demande = get_object_or_404(Demande, id=demande_id)
    if request.method == 'POST':
        # Placeholder: add all users for simplicity
        demande.participants.set([])
        demande.save()
        return redirect('create_meeting')
    return render(request, 'scheduler_app/inviter.html', {'demande': demande})
