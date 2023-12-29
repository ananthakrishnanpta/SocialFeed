from ast import Delete
from typing import Any
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# ListView helps us list query set into the db and returns a list
# DetailView gives us one result from query

from .models import Message
from .forms import MessageForm, EditForm
from django.urls import reverse_lazy, reverse
# Create your views here.

#def home(request):
#    return render(request, 'home.html', {})

# Utilizing Class based views

class FeedView(ListView):
    model = Message
    template_name = 'feed.html'
    ordering = ['-id']
    
    
class MessageDetailView(DetailView):
    model = Message
    template_name = 'message_details.html' 
    def get_context_data(self, *args, **kwarg):
        context = super(MessageDetailView, self).get_context_data(*args, **kwarg)
        datum = get_object_or_404(Message, id=self.kwargs['pk'])
        total_likes = datum.total_likes()
        liked = False
        if datum.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        
        return context


class CreateMessageView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'addMsg.html'
    # fields = ['title', 'body']
    # fields = '__all__'

class EditMessageView(UpdateView):
    model = Message 
    form_class = EditForm
    template_name= 'editMsg.html'

class DeleteMessageView(DeleteView):
    model = Message
    template_name = 'delMsg.html'
    success_url = reverse_lazy('feed')
   
#class AddCommentView(CreateView):
#   model = Comment
    
def LikeView(request, pk):
    msgs = get_object_or_404(Message, id = request.POST.get('msg_id'))
    liked = False
    if msgs.likes.filter(id=request.user.id).exists():
        msgs.likes.remove(request.user)
    else:
        msgs.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('message-detail', args=[str(pk)]))
    

    