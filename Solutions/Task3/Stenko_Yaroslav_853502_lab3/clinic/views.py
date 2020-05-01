from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Schedule, Comment
from users.models import Doctor, Patient
from .forms import ScheduleAddForm, CommentAddForm
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required


class DoctorListView(ListView):
    model = Doctor
    template_name = 'home.html'


def doctor_detail_view(request, doctor_id):
    schedules = Schedule.objects.filter(doctor__user_id=doctor_id)
    return render(request, 'doctor_detail.html', context={'schedules': schedules})


@login_required(login_url='/accounts/login')
def schedule_create_view(request):
    doctor = get_object_or_404(Doctor, pk=request.user.pk)  # Doctor.objects.get(pk=request.user.pk)
    schedule_form = ScheduleAddForm(request.POST)
    if schedule_form.is_valid():
        schedule = schedule_form.save(commit=False)
        schedule.doctor = doctor
        schedule.save()
        return HttpResponseRedirect('/')
    return render(request, 'schedule_add.html', context={"schedule_form": schedule_form})


def schedule_edit_view(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)

    if request.method == "POST":
        schedule_form = ScheduleAddForm(request.POST, instance=schedule)
        if schedule_form.is_valid():
            schedule_form.save()
        return HttpResponseRedirect('/doctors/' + str(schedule.doctor.pk))
    else:
        schedule_form = ScheduleAddForm(instance=schedule)
    context = {
        "schedule_form": schedule_form
    }
    return render(request, 'schedule_add.html', context)


def schedule_delete_view(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    if request.method == "POST":
        schedule.delete()
        return HttpResponseRedirect('/doctors/' + str(schedule.doctor.pk))
    context = {
        'schedule': schedule,
    }
    return render(request, 'schedule_delete.html', context)


def comment_create_view(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)  # Doctor.objects.get(pk=request.user.pk)
    form = CommentAddForm(request.POST)
    patient = get_object_or_404(Patient, pk=request.user.pk)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.patient = patient
        comment.doctor = doctor
        comment.save()
        return HttpResponseRedirect('/')
    return render(request, 'comment_add.html', context={"form": form})


def comment_edit_view(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        form = CommentAddForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = CommentAddForm(instance=comment)
    context = {
        'form': form
    }
    return render(request, 'comment_add.html', context)


def comment_delete_view(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        comment.delete()
        return redirect('/')
    context = {
        'comment': comment
    }
    return render(request, 'comment_delete.html', context)