from django.contrib import admin
from account.models import Profile, Health, Document, DocumentCategory

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_username', 'user_first_name', 'user_type', 'user_is_superuser')
    search_fields = ('user__username', 'user__first_name', 'user__email')
    list_filter = ('user_type', 'user__is_superuser', 'user__is_staff')

    fieldsets = (
        (None, {'fields': ('user', 'phone', 'avatar', 'bio', 'birthday', 'user_type')}),
    )

    def user_username(self, obj):
        return obj.user.email
    user_username.short_description = 'Username'

    def user_first_name(self, obj):
        return obj.user.first_name
    user_first_name.short_description = 'First Name'

    def user_is_superuser(self, obj):
        return obj.user.is_superuser
    user_is_superuser.short_description = 'Superuser'
    user_is_superuser.boolean = True

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Document)
admin.site.register(DocumentCategory)
admin.site.register(Health)

