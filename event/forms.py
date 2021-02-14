from django.forms import ModelForm, DateInput
# from event.models import Event, EventMember
from event.models import Event
from django import forms

class EventForm(ModelForm):
  class Meta:
    model = Event
    fields = ['title', 'time', 'address', 'description', 'completed']
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'completed': forms.HiddenInput,
    }
    exclude = ['user']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['time'].input_formats = ('%Y-%m-%dT%H:%M',)
    # self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

