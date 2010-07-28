from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from pcommerce.shipment.parcel.browser.base import ParcelBase

class ParcelConfirmation(ParcelBase):
    template = ViewPageTemplateFile('confirmation.pt')