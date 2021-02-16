<<<<<<< HEAD
from django.forms import ModelForm, DateInput
# from event.models import Event, EventMember
from event.models import Event
from django import forms

class EventForm(ModelForm):
  class Meta:
    model = Event
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      # 'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    exclude = ['user']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
=======
from django.forms import ModelForm, DateInput
from event.models import Event
from django import forms

class EventForm(ModelForm):
  class Meta:
    model = Event
    fields = ['title', 'time', 'address', 'description', 'completed']
    widgets = {
      'time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'completed': forms.HiddenInput,
    }
    exclude = ['user']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    self.fields['time'].input_formats = ('%Y-%m-%dT%H:%M',)


>>>>>>> remotes/origin/feature/todo/skj
