from django.contrib import admin
from litreview.models import Ticket, Review, UserFollows

# Register your models here.
# listings/admin.py


admin.site.register(Ticket)
admin.site.register(Review)
admin.site.register(UserFollows)
