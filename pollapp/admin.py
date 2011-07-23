from pollapp.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    # the ordering and accessibility of object fields
    # fields = ['pub_date', 'question']

    # must not be used together with fields!
    fieldsets = [
        (None,  {'fields': ['question']}),
        ('Date Information', {'fields': ['pub_date'],
                              'classes': ['collapse']})
    ]

    inlines = [ChoiceInline,]


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
