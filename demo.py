from woocommerce import API
import pprint

wcapi = API(
    url="http://localhost:10004",
    consumer_key="ck_4a21aba40202255b495b850168ccdfb6304612c8",
    consumer_secret="cs_9a86b012601db4affdf8047e1424a0e318e1d824",
    version="wc/v3"
)

# r = wcapi.get("products")
# pprint.pprint(r.json())

def addCustomerPayload(**kwargs):
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

wcapi = API(
    url="http://localhost:10004",
    consumer_key="ck_4a21aba40202255b495b850168ccdfb6304612c8",
    consumer_secret="cs_9a86b012601db4affdf8047e1424a0e318e1d824",
    version="wc/v3"
)

r = wcapi.post("customers",addCustomerPayload(email= "abc@gmail.com"))
print(r.json())




