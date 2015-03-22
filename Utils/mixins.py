from django.core.exceptions import PermissionDenied


class GuideRequiredMixin:
    def dispatch(self, *args, **kwargs):
        if self.request.user.profile.is_guide:
            return super(GuideRequiredMixin, self).dispatch(*args, **kwargs)
        else:
            raise PermissionDenied('User must be guide')