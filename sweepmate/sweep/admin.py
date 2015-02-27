from django.contrib import admin
from sweep.models import Backer, Event, Player, Sweep

class BackerAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('firstname',)}

class EventAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('eventname',)}

class PlayerAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('playername',)}

class SweepAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('sweepname',)}
		

# Register your models here.
admin.site.register(Backer, BackerAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Sweep, SweepAdmin)