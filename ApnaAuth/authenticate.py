from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class ApnaAuthentication(authentication.BaseAuthentication):

    # the class need to have ParentClass=BaseAuthentication
    # the name of the method need to be exactly(authenticate)
    def authenticate(self, request):
        username = request.META.get('HTTP_MERA_USERNAME')  # this will get
        # the HEADER=MERA-USERNAME (NOTE the difference between the "underscores" and the "dashes")
        # value you passed to the Http request
        if not username:
            raise exceptions.AuthenticationFailed('PLease Provide a valid MERA_USERNAME HTTP HEADER value')  # Some people return None instead of raising
            # an error (in case they want to just have an optional authentication , instead of a truly strict/mandatory one)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed(f'user withe username={username} does '
                                                  f'NOT exists inside the Django USER Models')

        return (user, None)  # from the returned tuple (user, None) Middleware=contrib.auth saves "user" into request.user attr,
        # and the second item inside the tuple (in this ase None), inside the
        # request.auth attr (typically the raw token string or Instance is saved inside the request.auth attr)
