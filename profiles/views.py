from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm, UserForm
from .models import Profile


# Create your views here.

@login_required()
def edit_profile(request):

    # This line is a part of the connection to Cloudinary API
    context = dict(backend_form=ProfileForm())

    if request.method == 'POST':
        user_form = UserForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        context['posted'] = profile_form.instance

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profiles:detail', pk=request.user.profile.pk)

    else:

        # This creates a profile for users that don't have a profile.
        # They didn't have a profile because they registered before the profile feature was added.
        # A profile is created for a user during the process of signup.

        Profile.objects.get_or_create(user=request.user)
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'profiles/update_form.html', {'user_form': user_form, 'profile_form': profile_form})


class ProfileDetail(LoginRequiredMixin, generic.DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
    context_object_name = 'profile'
