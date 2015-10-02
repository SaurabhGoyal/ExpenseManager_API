from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from apps.account.models import User


class CustomUserCreationForm(UserCreationForm):
    """ A form for creating new custom-users. """

    # class Meta(UserCreationForm.Meta):
    #     """ Extending the Meta class to customize the desired fields in the form. """
    #     model = User
    #     fields = '__all__'

    def clean_email(self):
        return self.cleaned_data['email'].strip().lower()


class CustomUserChangeForm(UserChangeForm):
    """ A form for updating existing users. """

    # class Meta(UserChangeForm.Meta):
    #     """ Extending the Meta class to customize the desired fields in the form. """
    #     model = User
    #     fields = '__all__'

    def clean_email(self):
        return self.cleaned_data['email'].strip().lower()


class AuthUserAdmin(UserAdmin):
    """ Custom UserAdmin for Custom User model """

    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    readonly_fields = ('date_joined', )

    list_display = ('email', 'first_name', 'last_name', 'date_joined', )
    list_filter = ('is_active', )

    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'phone', )}),
        ('Permissions', {'fields': ('is_active', )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'phone', )
        }
        ),
    )

    search_fields = ('email', )
    ordering = ('email', )
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(User, AuthUserAdmin)
