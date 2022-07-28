import os

db_host = os.environ.get('DB_HOST', default='host.docker.internal')
db_name = os.environ.get('DB_NAME', default='notes')
db_user = os.environ.get('DB_USER', default='notes')
db_pass = os.environ.get('DB_PASS', default='')
db_port = os.environ.get('DB_PORT', default='5432')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
