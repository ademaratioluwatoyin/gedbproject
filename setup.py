import sys
from streamlit import cli as stcli
from settings import *


if __name__ == '__main__':
    try : 
        sub_comm = sys.argv[1:][0]

        if (sub_comm == "create-db") : 
            # Create Tables
            dbms.create_db_tables()
        elif (sub_comm == "run-client"):
            sys.argv = ["streamlit", "run", "main.py"]
            sys.exit(stcli.main())
        elif (sub_comm == "run-admin"):
            sys.argv = ["streamlit", "run", "admin.py"]
            sys.exit(stcli.main())
        else : 
            print("create-db    Create new database")
            print("runserver    Run main streamlit app")
    except : 
        print("run 'python setupy.py help'")

    