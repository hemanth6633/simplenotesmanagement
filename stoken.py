from itsdangerous import URLSafeTimedSerializer
salt = 'otpverify'
def entoken(data):
    serializer = URLSafeTimedSerializer('dhoni07')
    return serializer.dumps(data,salt=salt)

def dntoken(data):
    serializer = URLSafeTimedSerializer('dhoni07')
    return serializer.loads(data,salt=salt)