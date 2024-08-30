from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import HelpMod
from .forms import HelpForm


# Create your views here.

@login_required
def help_view(request):
    if request.method == 'POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            try:
                help_instance = form.save(commit=False)
                help_instance.user = request.user
                help_instance.save()
            except Exception as e:
                return JsonResponse({
                    'msg': str(e)
                }, status=400)
            return redirect('helped')
    else:
        form = HelpForm()
    return render(request, 'help/helps.html', {'form': form})


def help_accessed(request):
    return render(request,'help/helped.html')
