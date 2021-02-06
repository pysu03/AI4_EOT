from django.shortcuts import render, redirect
from .models import Board
from .forms import BaseBulletinBoard

# Create your views here.

def boardView(request):
    template_name = 'bulletin_board.html'
    board_object = Board.objects.all()
    context = {
        'boardobject':board_object
    }
    return render(request, template_name, context)

def bulletin(request):
    return render(request, 'bulletin_base.html')

def index(request):
    template_name = 'index.html'
    board_object = Board.objects.all()
    context = {
        'boardobject':board_object
    }
    return render(request, template_name, context)

def boardWrite(request):
    return render(request, 'bulletin_base.html')

def calendar(request):
    return render(request, 'calendar.html')



def writePageView(request):
    template_name = 'bulletin_write.html'
    if request.method == 'POST':
        form = BaseBulletinBoard(request.POST)
        if form.is_vaild():
            form.save()
            return redirect('/view')
    else:
        form = BaseBulletinBoard()
        context = {
            'form':form,
        }

    return render(request, template_name, context)