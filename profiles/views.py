from django.shortcuts import render
from .models import Profile
import logging
from django.http import Http404


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum
# lacus d
def index(request):
    """Displays profiles list

    Args:
        request (HttpRequest): HTTP ovbject request

    Returns:
        HttpResponse: HTTP response containing profiles view
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque quis, pellentesque
# dui. Nullam facilisis pharetra vulputate. Sed tincidunt, dolor id facilisis fringilla, eros leo
# tristique lacus, it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus
# et netus et males
def profile(request, username):
    """Displays a profile details

    Args:
        request (HttpRequest): HTTP ovbject request
        username (str): profile username

    Returns:
        HttpResponse: HTTP response containing profile view
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist as ex:
        logging.exception(f'Profile introuvable : {ex}', exc_info=False)
        raise Http404()
    else:
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
