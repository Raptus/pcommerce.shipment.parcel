from zope.interface import implements, Interface
from zope.component import adapts

from pcommerce.core import PCommerceMessageFactory as _
from pcommerce.core.interfaces import IShipmentMethod
from pcommerce.shipment.parcel.interfaces import IParcelShipment

class ParcelShipment(object):
    implements(IShipmentMethod, IParcelShipment)
    adapts(Interface)
    
    title = _('parcel shipment')
    description = _('parcel shipment by post')
    icon = '++resource++pcommerce_shipment_parcel_icon.png'
    logo = '++resource++pcommerce_shipment_parcel_logo.png'
    
    def __init__(self, context):
        self.context = context
    
    def mailInfo(self, order, lang=None, customer=False):
        data = order.shipmentdata['pcommerce.shipment.parcel']
        address = data.as_customer and order.address or data.address
        return _('parcel_mailinfo', default="""parcel shipment address
${address}""", mapping=dict(address=address.mailInfo(self.context.REQUEST, lang, customer)))
