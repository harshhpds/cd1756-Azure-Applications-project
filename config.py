import os
import urllib

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Flask secret key
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # Azure Blob Storage
    BLOB_ACCOUNT = os.environ.get("BLOB_ACCOUNT")
    BLOB_STORAGE_KEY = os.environ.get("BLOB_STORAGE_KEY")
    BLOB_CONTAINER = os.environ.get("BLOB_CONTAINER")
    BLOB_CONNECTION_STRING = os.environ.get("BLOB_CONNECTION_STRING")

    # Azure SQL Database
    SQL_SERVER = os.environ.get("SQL_SERVER")
    SQL_DATABASE = os.environ.get("SQL_DATABASE")
    SQL_USER_NAME = os.environ.get("SQL_USER_NAME")
    SQL_PASSWORD = os.environ.get("SQL_PASSWORD")

    # ODBC connection string
    params = urllib.parse.quote_plus(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={SQL_SERVER},1433;"
        f"DATABASE={SQL_DATABASE};"
        f"UID={SQL_USER_NAME};"
        f"PWD={SQL_PASSWORD};"
        f"TrustServerCertificate=yes;"
    )

    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc:///?odbc_connect={params}"
        if SQL_SERVER else None
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft Authentication (OAuth2)
    CLIENT_ID = os.environ.get("APPLICATION_CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET_VALUE")
    AUTHORITY = "https://login.microsoftonline.com/common"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]

    # Flask session type
    SESSION_TYPE = "filesystem"
import os
import urllib

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Flask secret key
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # Azure Blob Storage
    BLOB_ACCOUNT = os.environ.get("BLOB_ACCOUNT")
    BLOB_STORAGE_KEY = os.environ.get("BLOB_STORAGE_KEY")
    BLOB_CONTAINER = os.environ.get("BLOB_CONTAINER")
    BLOB_CONNECTION_STRING = os.environ.get("BLOB_CONNECTION_STRING")

    # Azure SQL Database
    SQL_SERVER = os.environ.get("SQL_SERVER")
    SQL_DATABASE = os.environ.get("SQL_DATABASE")
    SQL_USER_NAME = os.environ.get("SQL_USER_NAME")
    SQL_PASSWORD = os.environ.get("SQL_PASSWORD")

    # ODBC connection string
    params = urllib.parse.quote_plus(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={SQL_SERVER},1433;"
        f"DATABASE={SQL_DATABASE};"
        f"UID={SQL_USER_NAME};"
        f"PWD={SQL_PASSWORD};"
        f"TrustServerCertificate=yes;"
    )

    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc:///?odbc_connect={params}"
        if SQL_SERVER else None
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft Authentication (OAuth2)
    CLIENT_ID = os.environ.get("APPLICATION_CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET_VALUE")
    AUTHORITY = "https://login.microsoftonline.com/common"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]

    # Flask session type
    SESSION_TYPE = "filesystem"
