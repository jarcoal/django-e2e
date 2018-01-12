from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from . import utils

UserModel = get_user_model()


class PasswordSpecsView(View):
    """Returns info on how a user's password was hashed"""

    username_required_msg = 'username required (e.g. "?{}=<username>")'
    username_not_found_msg = 'username "{}" not found'

    def get(self, req, *args, **kwargs):
        # Get the username from the query string argument
        try:
            username = req.GET[UserModel.USERNAME_FIELD]
        except KeyError:
            return JsonResponse({'error': self.username_required_msg.format(
                                 UserModel.USERNAME_FIELD)}, status=400)

        # Get the user for the username
        try:
            user = UserModel.objects.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            return JsonResponse(
                {'error': self.username_not_found_msg.format(username)},
                status=404)

        return JsonResponse({
            # Send the user's current password hashing specs
            'user': utils.get_user_password_hash_specs(user),

            # Send the current algo/iterations expection so that the client
            # can submit that if needed.
            'required': utils.get_required_password_hash_specs(),
        })
