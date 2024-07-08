from django.utils.translation import ugettext_lazy as _

import horizon

class Mygroup(horizon.PanelGroup):
    name = _("My Group")
    slug = "mygroup"
    panels = ('mypanel',)
    
class Mydashboard(horizon.Dashboard):
    name = _("Mydashboard")
    slug = "mydashboard"
    panels = (Mygroup,)  # Add your panels here.
    default_panel = 'mypanel'  # Specify the slug of the dashboard's default panel.


horizon.register(Mydashboard)
