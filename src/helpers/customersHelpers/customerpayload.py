class CustomersPayload():
    def __init__(self):
        pass

    def createCustomerPayload(self,**kwargs):
        data = {
            "email": kwargs['email'],
            "first_name": "John",
            "last_name": "Doe",
            "username": kwargs['email'],
            "billing": {
                "first_name": "John",
                "last_name": "Doe",
                "company": "",
                "address_1": "969 Market",
                "address_2": "",
                "city": "San Francisco",
                "state": "CA",
                "postcode": "94103",
                "country": "US",
                "email": kwargs["email"],
                "phone": "(555) 555-5555"
            },
            "shipping": {
                "first_name": "John",
                "last_name": "Doe",
                "company": "",
                "address_1": "969 Market",
                "address_2": "",
                "city": "San Francisco",
                "state": "CA",
                "postcode": "94103",
                "country": "US"
            }
        }
        return data