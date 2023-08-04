from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# import datetime
# import jwt
# from config.config import Config
# from flask import jsonify
#


# JWT_EXPIRY_SECOND = 30
#
#
# def generate_token(uid):
#     payload = {
#         'id': uid,
#         'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=JWT_EXPIRY_SECOND)
#     }
#     return jwt.encode(payload=payload, key=Config().SECRET_KEY, algorithm='HS256')
#
#
# def verify_tokens(token: str):
#     try:
#         payload = jwt.decode(token, Config().SECRET_KEY, algorithms=['HS256'])
#         return payload
#     except jwt.ExpiredSignatureError:
#         return jsonify({'message': 'Token has expired'})
#     except jwt.InvalidTokenError:
#         return jsonify({'message': 'Invalid token'})
