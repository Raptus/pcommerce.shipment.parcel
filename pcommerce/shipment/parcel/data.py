from pcommerce.core.data import ShipmentData

def ParcelShipmentData(as_customer=True, address=None):
    data = ShipmentData('pcommerce.shipment.parcel')
    data.as_customer = as_customer
    data.address = address
    return data
