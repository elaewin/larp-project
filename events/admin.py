import datetime
from django.contrib import admin
from django.core.urlresolvers import reverse
from events.models import Event, Tag, Participant


class TagInline(admin.TabularInline):
    model = Tag.events.through


class ParticipantInline(admin.TabularInline):
    model = Participant.players.through


def make_published(modeladmin, request, queryset):
    now = datetime.datetime.now()
    queryset.update(published_date=now)
make_published.short_description = "Set publication date for selected posts."


class EventAdmin(admin.ModelAdmin):
    inlines = [
        TagInline,
        # ParticipantInline,
    ]
    list_display = ('title', 'creator_for_admin', 'date', 'created_date', 'modified_date')
    readonly_fields = ('created_date', 'modified_date')
    actions = [make_published, ]

    def creator_for_admin(self, obj):
        creator = obj.creator
        url = reverse('admin:auth_user_change', args=(creator.pk,))
        name = creator.get_full_name() or creator.username
        link = '<a href="{}">{}</a>'.format(url, name)
        return link
    creator_for_admin.short_description = 'creator'
    creator_for_admin.allow_tags = True


class TagAdmin(admin.ModelAdmin):
    fields = ('name', 'description')


class ParticipantAdmin(admin.ModelAdmin):
    fields = ('game', 'players')


admin.site.register(Event, EventAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Participant, ParticipantAdmin)

# Register your models here.
