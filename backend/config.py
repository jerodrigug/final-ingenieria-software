import os

# Configuración para conexión con base de datos en MongoDB Atlas.

DB_URI = 'mongodb+srv://seat:seat@cluster0-5zw53.azure.mongodb.net/test?retryWrites=true&w=majority' # Funciona
JWT_SECRET = 'super_secret'

# Configuración para almacenamiento de documentos en AWS S3.

S3_BUCKET = ''
S3_KEY = ''
S3_SECRET = ''

#S3_BUCKET                 = os.environ.get("S3_BUCKET_NAME")
#S3_KEY                    = os.environ.get("S3_ACCESS_KEY")
#S3_SECRET                 = os.environ.get("S3_SECRET_ACCESS_KEY")

S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

SECRET_KEY                = os.urandom(32)
DEBUG                     = True
PORT                      = 5000