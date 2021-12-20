from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

mysql_username = config.get('DATABASE', 'MYSQL_USER')
mysql_pwd = config.get('DATABASE', 'MYSQL_PWD')
mysql_host = config.get('DATABASE', 'MYSQL_HOST')
mysql_port = config.get('DATABASE', 'MYSQL_PORT')
mysql_database_name = config.get('DATABASE', 'MYSQL_DATABASE_NAME')

DATABASE = "mysql://{}:{}@{}:{}/{}?charset=utf8".format(
    mysql_username,
    mysql_pwd,
    mysql_host,
    mysql_port,
    mysql_database_name
)

engine = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True,
    pool_size=50
)

Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
