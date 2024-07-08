from django.utils.translation import ugettext_lazy as _
from horizon import tables


class MyFilterAction(tables.FilterAction):
    name = "myfilter"


class InstancesTable(tables.DataTable):
    name = tables.Column('name', \
                         verbose_name=_("Name"))
    status = tables.Column('status', \
                           verbose_name=_("Status"))
    availability_zone = tables.Column('OS-EXT-AZ:availability_zone', \
                           verbose_name=_("Availability Zone"))
    instance_name = tables.Column('OS-EXT-SRV-ATTR:instance_name', \
                         verbose_name=_("Instance Name"))
    image_name = tables.Column('image_name', \
                               verbose_name=_("Image Name"))

    class Meta:
        name = "instances"
        verbose_name = _("Instances")
        table_actions = (MyFilterAction,)