from django.shortcuts import render,reverse
from .forms import RegisterForm
from django.views.generic.edit import CreateView,DeleteView
from django.contrib.auth.decorators import login_required
from .models import Token
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm

    def get_success_url(self):
        # url = self.request.META.get('HTTP_REFERER')
        # if url:
        #     return url
        # return '/'
        return reverse('login')

def home(request):
    return render(request,'registration/home.html')

@login_required
def features(request):
    return render(request,'registration/features.html')

class DeleteKey(DeleteView):
    model = Token
    success_url = reverse_lazy('features')

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(DeleteKey, self).get_object()
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj


class AddKey(CreateView):
    model=Token
    fields = ['name']
    success_url = reverse_lazy('features')
    template_name = 'registration/features.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super().form_valid(form)
        except:
            return self.form_invalid(form)
    def form_invalid(self, form):
        messages.add_message(self.request,messages.INFO,"This app name is already in used. Please choose another name.")
        return super().form_invalid(form)