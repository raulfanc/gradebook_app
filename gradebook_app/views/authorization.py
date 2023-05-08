from django.contrib.auth.decorators import login_required, user_passes_test

from django.utils.decorators import method_decorator


class LecturerRequiredMixin:
    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='lecturer').exists()))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class StudentRequiredMixin:
    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='student').exists()))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)