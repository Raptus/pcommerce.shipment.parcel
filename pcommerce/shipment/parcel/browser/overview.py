from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from pcommerce.shipment.parcel.browser.base import ParcelBase

class ParcelOverview(ParcelBase):
    template = ViewPageTemplateFile('overview.pt')