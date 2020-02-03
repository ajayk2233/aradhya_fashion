from django.contrib import admin
from darjano.models import Salon,Branch
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import User,Group

class AdminSite(admin.AdminSite):
    site_title = 'Aradhya Fashion title'

    # Text to put in each page's <h1>.
    site_header = gettext_lazy('Aradhya Fashion header')

    # Text to put at the top of the admin index page.
    index_title = gettext_lazy('Aradhya Fashion index')

    # URL for the "View site" link at the top of each admin page.
    site_url = '/darjano/show'

class SalonAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug','address','branch')
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
    

admin_site = AdminSite()
admin_site.register(Salon,SalonAdmin)
admin_site.register([User,Group])