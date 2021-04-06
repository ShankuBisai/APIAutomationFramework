class OrderPayload(object):
    def __init__(self):
        pass

    def createOrderpayload(self,**kwargs):
        data = {
            "payment_method": "bacs",
            "payment_method_title": "Direct Bank Transfer",
            "set_paid": True,
            "billing": {
                "first_name": "John",
                "last_name": "Doe",
                "address_1": "969 Market",
                "address_2": "",
                "city": "San Francisco",
                "state": "CA",
                "postcode": "94103",
                "country": "US",
                "email": "john.doe@example.com",
                "phone": "(555) 555-5555"
            },
            "shipping": {
                "first_name": "John",
                "last_name": "Doe",
                "address_1": "969 Market",
                "address_2": "",
                "city": "San Francisco",
                "state": "CA",
                "postcode": "94103",
                "country": "US"
            },
            "line_items": [
                {
                    "product_id": kwargs["productId"],
                    "quantity": 2
                },
            ],
            "shipping_lines": [
                {
                    "method_id": "flat_rate",
                    "method_title": "Flat Rate",
                    "total": "10.00"
                }
            ]
        }
        return data