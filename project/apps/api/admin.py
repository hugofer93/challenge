from django.contrib import admin

from .models import LastRequestReposGithubApi


@admin.register(LastRequestReposGithubApi)
class LastRequestReposGithubApiAdmin(admin.ModelAdmin):
    list_display = ('user', 'lastRequest', 'created')
    list_display_links = ('user',)
    search_fields = ('user__username', 'user__email')
    list_filter = ('lastRequest', 'created', 'available')
