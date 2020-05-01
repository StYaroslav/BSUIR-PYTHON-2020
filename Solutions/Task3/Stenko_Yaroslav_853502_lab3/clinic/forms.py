from django import forms
from .models import Schedule, Comment


class ScheduleAddForm(forms.ModelForm):

    def clean(self):
        date = self.cleaned_data.get('date')
        matching_date = Schedule.objects.filter(date=date)
        if self.instance:
            matching_date = matching_date.exclude(pk=self.instance.pk)
        if matching_date.exists():
            raise forms.ValidationError("You have already created schedule for this date!")

    class Meta:
        model = Schedule
        fields = ['date']


class CommentAddForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']
