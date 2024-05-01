from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import UploadedFile


def index(request):
    return render(request, "index.html")


@csrf_exempt
def upload_files(request):
    if request.method == 'POST':
        files = request.FILES.getlist('images[]')
        uploaded_ids = []
        for file in files:
            uploaded_file = UploadedFile(file=file)
            uploaded_file.save()
            uploaded_ids.append(uploaded_file.pk)
        request.session['last_upload_ids'] = uploaded_ids
        return redirect('creating')
    else:
        return JsonResponse({'status': 'error'})


def creating(request):
    uploaded_files = UploadedFile.objects.filter(id__in=request.session.get('last_upload_ids', []))
    context = {'uploaded_files': uploaded_files}
    return render(request, "creating.html", context)


def about(request):
    return HttpResponse("О сайте")


def contact(request):
    return HttpResponse("Контакты")
