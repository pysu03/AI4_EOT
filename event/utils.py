# calendarapp/utils.py
from calendar import HTMLCalendar
from .models import Event


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, user, day, events):
        d = ''

        if user != None:
            events_per_day = events.filter(time__day=day, user=user)

            for event in events_per_day:
                d += f'<li> {event.get_html_url} </li>'

        if day != 0:
            return f"<td style='width: 14%; font-size:1.1rem'><p class='date'>{day}</p><ul style='margin: 0;  padding: 0; list-style:none;'> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, user, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(user, d, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, user, withyear=True):
        events = Event.objects.filter(time__year=self.year, time__month=self.month)
        cal = f'<table class="table table-bordered" style="height: 100%; min-height:568px" >\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(user, week, events)}\n'
        return cal