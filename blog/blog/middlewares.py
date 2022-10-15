from django.utils import timezone
from users.models import UserActivity


class LastRequestTimeMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request, *args, **kwargs)
        user = request.user
        if user.is_authenticated:
            UserActivity.objects.update_or_create(user=user, defaults={'last_request': timezone.now()})
        return response
