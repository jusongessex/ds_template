import pyodbc
import pandas as pd
def sql_conn(Database, Query, Server="essexbi"):
    '''
    Usage: Read data from a sql server as a pandas dataframe by establishing a trusted pyodbc connection
    Parameters: - str Database: name of the database for the table specified in the query
                - str Query: The full SQL query for the data encased in triple double-quotations (ex: """ SELECT * 
                                                                                                        FROM table """)
                - str Server: name of the server for the database specified; by default essexbi
    Return:     - pd.Dataframe queryDf: the queried data 
    '''

    
    sqlCxn = pyodbc.connect(
        driver='SQL Server',
        host=Server,
        database=Database,
        Trusted_Connection="yes",
    )
    
    with sqlCxn:
        queryDf = pd.read_sql(Query, sqlCxn)
    print(queryDf.shape)
    print(queryDf.columns)
    return queryDf