from zope.interface import implements

from Products.Five.browser import BrowserView

from pcommerce.core.interfaces import IShipmentView, IOrder, IShoppingCart

from pcommerce.shipment.parcel.data import ParcelShipmentData

class ParcelBase(BrowserView):
    implements(IShipmentView)
    
    errors = {}
    
    def __init__(self, shipment, request):
        self.shipment = shipment
        self.context = shipment.context
        self.request = request
        self.cart = IShoppingCart(self.context)
        self.order = IOrder(self.context)
        self.data = self.order.shipmentdata.get('pcommerce.shipment.parcel', ParcelShipmentData())
    
    def __call__(self):
        return self.template()
    
    def validate(self):
        return True
    
    def renders(self):
        return True
        
    def process(self):
        return
    
    @property
    def address(self):
        if self.data.as_customer:
            return self.order.address
        return self.data.address
    
    @property
    def address_as_customer(self):
        if self.request.get('parcel_hidden', False):
            return self.request.get('parcel_address_as_customer', False)
        return self.data.as_customer
