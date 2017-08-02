from django.contrib import admin

from .models import Quest, Completion, Goal, Challenge

admin.site.register(Quest)
admin.site.register(Completion)
admin.site.register(Goal)
admin.site.register(Challenge)
