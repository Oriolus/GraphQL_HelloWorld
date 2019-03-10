import urllib
from config_loader import load
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


db_config = load()['database']


params = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};' +
                                 'SERVER={0};'.format(db_config['server']) +
                                 'DATABASE={0};'.format(db_config['database']) +
                                 'UID={0};'.format(db_config['uid']) +
                                 'PWD={0}'.format(db_config['password'])
                                 )
conn_string = 'mssql+pyodbc:///?odbc_connect={}'.format(params)

engine = create_engine(conn_string)
db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))


Base = declarative_base()
Base.query = db_session.query_property()
