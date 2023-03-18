from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from ..models.users import User
from werkzeug.security import generate_password_hash, check_password_hash
from http import HTTPStatus
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from werkzeug.exceptions import Conflict, BadRequest

auth_namespace = Namespace('auth', description='a namespace for authentication')

signup_model = auth_namespace.model(
    'Signup',{ 
    'id': fields.Integer(),
    'name': fields.String(required=True, description='A name'),
    'email': fields.String(required=True, description='An email'),
    'password': fields.String(required=True, description='A password'),
    'role' : fields.String(required= True, description = "User's role")
    
    
    }
)

user_model = auth_namespace.model(
    'User', {
    'id': fields.Integer(),
    'name': fields.String(required=True, description='A name'),
    'email': fields.String(required=True, description='An email'),
    'password_hash': fields.String(required=True, description='A password'),
    'role' : fields.String(required= True, description = "User's role")
    }
)

login_model = auth_namespace.model(
    'Login', {
    'email' : fields.String(required = True, description = 'An email'),
    'password' : fields.String(required = True, description='A password')
    }
)

@auth_namespace.route('/signup')
class SignUp(Resource):
    @auth_namespace.expect(signup_model)
    @auth_namespace.marshal_with(user_model)
    def post(self):
        """Create a new user"""
    
        data = request.get_json()

        try:
            new_user = User(
                name=data.get('name'),
                email = data.get('email'),
                password_hash = generate_password_hash(data.get('password'))
            )

            new_user.save()

            

            return new_user, HTTPStatus.CREATED
    
        except Exception as e:
            raise Conflict(f'User with email {data.get("email")} already exists')

@auth_namespace.route('/login')
class Login(Resource):
    # @jwt_required()
    @auth_namespace.expect(login_model)
    def post(self):
     
        """Generate a JWT"""
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if user is not None and check_password_hash(user.password_hash, password):
            access_token = create_access_token(identity=user.name)
            refresh_token = create_refresh_token(identity=user.name)

            response = {
                'access_token': access_token,
                'refresh_token': refresh_token
            }

            return response, HTTPStatus.OK
        
        
        raise BadRequest('Invalid name or password')
        

@auth_namespace.route('/refresh')
class Refresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        name = get_jwt_identity()

        access_token = create_access_token(identity=name)
        

        return{"access_token": access_token}, HTTPStatus.OK
    


