
#Serp API Key
API_KEY = "7f7342e8d4bfe676ef4d77880ef14d70e2d7cad3c9059ec57ab8e62baf1c5123"

# import companies 
from dummy_db import flw

COMPANIES = [flw.Flutterwave]

PAYMENTS = [comp for comp in COMPANIES if comp.sub_industry == "Payment"]

SUB_INDUSTRIES = {
    'Payment' : PAYMENTS,
}
