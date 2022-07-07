
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column, String, Integer, Table
from .models import *

# Global Variables
SQLITE = 'sqlite'


class MyDatabase:

    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}',
        
    }

    # Main DB Connection Ref Obj
    db_engine = None

    def __init__(self, dbtype, username='', password='', dbname=''):
        dbtype = dbtype.lower()

        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)

            self.db_engine = create_engine(engine_url)
            print(self.db_engine)

        else:
            print("DBType is not found in DB_ENGINE")

    def create_db_tables(self):
        
        try:
            metadata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error occurred during Table creation!")
            print(e)

    # Insert, Update, Delete
    def execute_query(self, query=''):
        if query == '':
            return

        print(query)
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)

    def get_table(self, table='', query=''):
        query = query if query != '' else "SELECT * FROM '{}';".format(table)
        print(query)
        data = []
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    obj= {}
                    obj["id"] = row[0]
                    obj["name"] = row[1]
                    obj["sub_industry"] = row[2]
                    obj["overview"] = row[3]
                    obj["info"] = row[4]
                    data.append(obj)  # print(row[0], row[1], row[2])
                result.close()
            
            return data

    def print_all_data(self, table='', query=''):
        query = query if query != '' else "SELECT * FROM '{}';".format(table)
        print(query)

        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:

                for row in result:
                    print(row)  # print(row[0], row[1], row[2])
                result.close()

        print("\n")

    def insert_company(self, name, overview, sub_industry, metrics):
        # Insert Data
        try :
            query = f"INSERT INTO {COMPANIES}( name, subindustry, overview, info) VALUES ( '{name}','{sub_industry}', '{overview}', '{metrics}');"
            self.execute_query(query)
            self.print_all_data(COMPANIES)
            return True
        except : 
            return False

    # Examples

    def sample_query(self):
        # Sample Query
        query = "SELECT name, overview FROM {TBL_USR} WHERE " \
                "sub_industry LIKE 'M%';".format(TBL_USR=COMPANIES)
        self.print_all_data(query=query)


    def sample_delete(self):
        # Delete Data by Id
        query = "DELETE FROM {} WHERE id=3".format(COMPANIES)
        self.execute_query(query)
        self.print_all_data(COMPANIES)
        
    def refresh(self):
        # Delete All Data
        query = "DELETE FROM {}".format(COMPANIES)
        self.execute_query(query)
        self.print_all_data(COMPANIES)

    def sample_insert(self):
        # Insert Data
        query = "INSERT INTO {}( name, subindustry, overview) " \
                "VALUES ( 'Flutterwave','Payments', 'Establised ....');".format(COMPANIES)
        self.execute_query(query)
        self.print_all_data(COMPANIES)

    def sample_update(self):
        # Update Data
        query = "UPDATE {} set name='XXXX' WHERE id={id}"\
            .format(COMPANIES, id=3)
        self.execute_query(query)
        self.print_all_data(COMPANIES)
