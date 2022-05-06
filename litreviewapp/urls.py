from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from litreview import views
import authentication.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('ticket/create', views.ticket_upload, name='ticket_create'),
    path('review/create', views.review_upload, name='review_create'),
    path('review/<int:test_ticket_id>/create', views.review_upload_2, name='review_create_2'),
    path('ticket/<int:ticket_id>/update', views.ticket_update, name='ticket_update'),
    path('review/<int:review_id>/update', views.review_update, name='review_update'),
    path('ticket/<int:ticket_id>/delete', views.ticket_delete, name='ticket_delete'),
    path('review/<int:review_id>/delete', views.review_delete, name='review_delete'),
    path('follows/<int:followed_user_id>/confirm', views.follows, name='follow_confirmed'),
    path('follows', views.follows_searched, name='follows'),
    path('follows/<int:follow_id>/delete', views.follow_delete, name='follow_delete'),
    path('feed', views.feed, name='feed'),
    path('posts', views.posts, name='posts'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
