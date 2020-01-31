from django.contrib import admin
from darjano.models import Salon,Branch

class SalonAdmin(admin.ModelAdmin):
    list_display = ('id','name','address','branch')
    list_display_links = ('name',)
    list_filter = ()
    list_editable = ('address','branch')
    search_fields = ()
    def Update_selected_Salons(self,request,queryset):
        queryset.update(address='Ahmednagar')
    actions = [Update_selected_Salons]
    
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    


admin.site.register(Salon,SalonAdmin)
admin.site.register(Branch)