from sqlalchemy import create_engine, text
import os
USER= os.environ['USER']
PASSWORD= os.environ['PASSWORD']
HOST=os.environ['HOST']
PORT=os.environ['PORT']
DATABASE=os.environ['DATABASE']
# Replace the placeholders in the connection string with actual values
connection_string = "mysql+pymysql://%s:%s@%s:%s/%s" % (USER, PASSWORD, HOST, PORT, DATABASE)

engine = create_engine(connection_string, connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}})

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM accounts"))
#     for row in result:
#         print(row)

