from django.contrib.auth.hashers import get_hasher


def get_user_password_hash_specs(user):
    """Returns the algorithm, iterations and salt used to hash a user's
       password"""

    algo, iterations, salt, hash = user.password.split('$')

    return {'algo': algo,
            'iterations': int(iterations),
            'salt': salt}


def get_required_password_hash_specs():
    """Returns the algorithm and iterations to be used for new password
       hashes"""

    default_hasher = get_hasher()

    return {'algo': default_hasher.algorithm,
            'iterations': default_hasher.iterations}
