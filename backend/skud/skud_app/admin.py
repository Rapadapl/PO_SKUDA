from django.contrib import admin

# Register your models here.
from .models import Log,Card,User,Level,Reader,SBC
#admin.site.register(Article)
#admin.site.register(Author)
admin.site.register(Log)
admin.site.register(Card)
admin.site.register(User)
admin.site.register(Level)
admin.site.register(Reader)
admin.site.register(SBC)