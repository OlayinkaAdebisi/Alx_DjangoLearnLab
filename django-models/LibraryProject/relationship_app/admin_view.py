from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponseForbidden

def is_admin(user):
    if user.profile.role == 'Admin':
        return user.profile.role == 'Admin'
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
