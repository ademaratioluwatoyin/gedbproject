
#Serp API Key
API_KEY = "7f7342e8d4bfe676ef4d77880ef14d70e2d7cad3c9059ec57ab8e62baf1c5123"

import json
from db_mapper.model import Company


# databse setup 
from database import db
dbms = db.MyDatabase(db.SQLITE, dbname='db.sqlite')
COMPANIES =dbms.get_table(db.COMPANIES)


# convert query to obkects 
for i, _ in enumerate(COMPANIES) : 
    _comp = Company(_["name"], _["sub_industry"], _["overview"] )
    _comp.infos = json.loads(_["info"])
    COMPANIES[i] = _comp

SUB_INDUSTRIES_LIST = ("Payment", "Savings", "Lending", "Investech")

SUB_INDUSTRIES_COMPANIES = {
    'Payment' : [comp for comp in COMPANIES if comp.sub_industry == "Payment"],
    'Savings' : [comp for comp in COMPANIES if comp.sub_industry == "Savings"],
    'Lending' : [comp for comp in COMPANIES if comp.sub_industry == "Lending"],
    'Investech' : [comp for comp in COMPANIES if comp.sub_industry == "Investech"],
}

