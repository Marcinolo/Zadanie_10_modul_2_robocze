import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TagForm, AuthorForm, QuoteForm
from .models import Tag, Author, Quote

def main(request):
    quotes = Quote.objects.filter(user=request.user).all() if request.user.is_authenticated else []
    return render(request, 'polls/index.html', {"quote": quotes})

@login_required
def set_done(request, note_id):
    Quote.objects.filter(pk=note_id, user=request.user).update(done_at=datetime.date.today())
    return redirect(to='polls:main')

@login_required
def delete_note(request, note_id):
    Quote.objects.get(pk=note_id, user=request.user).delete()
    return redirect(to='polls:main')

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save(commit=False)
            new_author.user = request.user
            new_author.save()
            return redirect(to='polls:main')
    else:
        form = AuthorForm()
    return render(request, 'polls/author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.user = request.user
            new_quote.save()
            form.save_m2m()  # Save many-to-many relationships
            return redirect(to='polls:main')
    else:
        form = QuoteForm()
    return render(request, 'polls/quote.html', {'form': form})