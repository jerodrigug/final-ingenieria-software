# Configuración para consumo de API GovCapeta.

API_BASE_URL = 'http://govcarpetaapp.mybluemix.net'

# Configuración para conexión con base de datos en MongoDB Atlas.

DB_URI = 'mongodb+srv://seat:seat@cluster0-5zw53.azure.mongodb.net/test?retryWrites=true&w=majority' # Funciona

# Configuración para almacenamiento de documentos en AWS S3.

S3_BUCKET_NAME = 'software-final'
S3_LOCATION	= 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET_NAME)

S3_ACCESS_KEY_ID = ''
S3_SECRET_ACCESS_KEY = ''
S3_SESSION_TOKEN = ''
