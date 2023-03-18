from flask_login import current_user
from flask import abort, redirect, url_for
from functools import wraps

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        if not current_user.has_role('admin'):
            return abort(403)
        return func(*args, **kwargs)
    return wrapper
