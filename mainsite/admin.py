from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    # 顯示所有文章時，以'title','slug','pub_date'顯示
    list_display = ('title','slug','pub_date')


admin.site.register(Post)