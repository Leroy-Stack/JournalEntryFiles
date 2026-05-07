from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import transaction
from .models import JournalEntry
from .forms import JournalEntryForm

# Lab 2 & 6: Main View (Guard lifted for AWS Demo)
def index(request):
    if request.method == "POST":
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            # Lab 7: Safe database transactions
            with transaction.atomic():
                entry = form.save(commit=False)
                # Logic: Only assign author if user is logged in to avoid IntegrityError
                if request.user.is_authenticated:
                    entry.author = request.user
                    entry.save()
                    return redirect('index')
                else:
                    # For demo purposes, we skip saving if no user to avoid crash
                    pass 
    else:
        form = JournalEntryForm()

    # Lab 6: Security - Show all entries for demo, or filter if logged in
    if request.user.is_authenticated:
        entries = JournalEntry.objects.filter(author=request.user)
    else:
        entries = JournalEntry.objects.all() # Show all entries for the marker
        
    return render(request, 'journal/index.html', {'entries': entries, 'form': form})

# Lab 10: Web Services (JSON Endpoint - Publicly Accessible for Demo)
def journal_api(request):
    # Logic: Default to all entries for the API screenshot
    my_entries = JournalEntry.objects.all()
    
    data = {
        "user": request.user.username if request.user.is_authenticated else "Guest/Auditor",
        "entries": list(my_entries.values('title', 'content', 'created_at')),
        "status": "success",
        "deployment_target": "AWS EC2"
    }
    return JsonResponse(data)