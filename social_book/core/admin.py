from django.contrib import admin
from .models import Profile,Post ,PImages,postliker,Follow_user

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(postliker)
admin.site.register(PImages)
admin.site.register(Follow_user)
# Register your models here.
