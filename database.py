from sqlalchemy import create_engine, text
USER="qvonmg1ppdnsylw8ks0y"
PASSWORD="pscale_pw_A55cImmJAXFpJrIXQjVF0Zf56TxzSoIf2iCoGocF7Tt"
HOST="aws.connect.psdb.cloud"
PORT=3306
DATABASE="cyber_ctf"
# Replace the placeholders in the connection string with actual values
connection_string = "mysql+pymysql://%s:%s@%s:%s/%s" % (USER, PASSWORD, HOST, PORT, DATABASE)

engine = create_engine(connection_string, connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}})

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM accounts"))
    for row in result:
        print(row)

