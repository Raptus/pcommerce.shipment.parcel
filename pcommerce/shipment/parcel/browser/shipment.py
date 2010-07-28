from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from pcommerce.core.interfaces import IAddressFactory
from pcommerce.shipment.parcel.browser.base import ParcelBase
from pcommerce.shipment.parcel.data import ParcelShipmentData

class ParcelShipment(ParcelBase):
    template = ViewPageTemplateFile('shipment.pt')
    
    def validate(self):
        self.errors = {}
        parcel_as_customer = self.request.form.get('parcel_address_as_customer', False)
        if not parcel_as_customer:
            factory = IAddressFactory(self.request)
            self.errors = factory.validate('parcel_address')
        return len(self.errors) == 0
    
    def process(self):
        self.data = ParcelShipmentData()
        parcel_as_customer = self.request.form.get('parcel_address_as_customer', False)
        if not parcel_as_customer:
            factory = IAddressFactory(self.request)
            self.data.address = factory.create('parcel_address')
        self.data.as_customer = parcel_as_customer
        props = getToolByName(self.context, 'portal_properties').pcommerce_properties
        self.data.pretaxcharge = props.getProperty('parcel_pretaxcharge', 0.0)
        self.data.posttaxcharge = props.getProperty('parcel_posttaxcharge', 0.0)
        return self.data