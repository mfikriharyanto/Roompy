from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TopicsForm
from .models import Topics, TopicsManager

# Create your views here.

@login_required
def create_topic(request):
    form = TopicsForm()
    if request.method == 'POST':
        print(request)
        form = TopicsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/topics/all-topic')
    
    context = {'form': form}
    return render(request,'create-topic.html', context)

def all_topic(request):
    
    return render(request,'all-topic.html')

def trending_topic(request):
    
    return render(request,'trending-topic.html')

def detail_topic(request, pk):
  topic = TopicsManager.get_topics(pk)

  if topic == None:
    return redirect('/topics/all-topic')

  context = {'topic':topic}
  return render(request,'detail-topic.html', context)