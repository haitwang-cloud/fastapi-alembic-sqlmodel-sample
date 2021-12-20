from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

MYSQL_USER = config.get('DATABASE', 'MYSQL_USER')
MYSQL_PWD = config.get('DATABASE', 'MYSQL_PWD')
MYSQL_HOST = config.get('DATABASE', 'MYSQL_HOST')
MYSQL_PORT = config.get('DATABASE', 'MYSQL_PORT')
MYSQL_DATABASE_NAME = config.get('DATABASE', 'MYSQL_DATABASE_NAME')

SQLALCHEMY_DATABASE_URL = "mysql://{}:{}@{}:{}/{}?charset=utf8".format(
    MYSQL_USER,
    MYSQL_PWD,
    MYSQL_HOST,
    MYSQL_PORT,
    MYSQL_DATABASE_NAME
)

TORTOISE_ORM = {
    "connections": {"default": SQLALCHEMY_DATABASE_URL},
    "apps": {
        "models": {
            "models": ["aerich.models", "app.models.models"],
            "default_connection": "default",
        },
    },
}
