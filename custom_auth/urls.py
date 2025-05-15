from allauth.account.views import ConfirmEmailView
from django.urls import path, include, re_path

urlpatterns = [
	# API аутентификации
	path('', include('dj_rest_auth.urls')),
	re_path(
		r"^registration/account-confirm-email/(?P<key>[-:\w]+)/$",
		ConfirmEmailView.as_view(),
		name="account_confirm_email",
	),
	path('registration/', include('dj_rest_auth.registration.urls')),
	path('social/', include('allauth.socialaccount.urls')),

]
