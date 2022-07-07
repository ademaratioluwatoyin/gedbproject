

from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column, String, Integer, Table

# Table Names
COMPANIES = 'companies'


metadata = MetaData()

company = Table(COMPANIES, metadata, Column("id", Integer, primary_key=True),
                Column('name', String(32)),
                Column('subindustry', String(32)),
                Column('overview', String()),
                #Column('document', String()),
                Column('info', String()))
