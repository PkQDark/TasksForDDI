from django.contrib import admin
from blog.models import Comment


class CommentAdmin(admin.ModelAdmin):
    # pass
    list_display = (
        'id',
        'path',
        'post_id',
        'author_id',
        'content',
        'pub_date',
    )


admin.site.register(Comment, CommentAdmin)
