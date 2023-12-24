from sqlalchemy import create_engine, text, MetaData, table

db_connection_string = 'mysql+pymysql://admin:SNRKumari.1919@database-1.crl8y9bwsxyd.us-east-1.rds.amazonaws.com:3306/mysql'
engine = create_engine(
    db_connection_string,
    connect_args={"ssl": {
        "ssl_ca": "us-east-1-bundle.pem"
    }})
