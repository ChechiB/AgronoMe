from app.api.helperApi.hlUrl import urlUsuario
from flask import request,make_response,jsonify
from flask_restplus import Resource
from app.uses_cases.moduloSeguridad.gestionarUsuarios import postUser,getAllUsers, getUsuario, updateUsuario, activateUser, requestRecoverPass, restorePass, accountUser
from app.uses_cases.moduloSeguridad.checkUrl import checkUrl
from app.api.shared.tokenHandler import token_required
from app.api.helperApi.hlResponse import notCheck
users = urlUsuario

@users.route('')
class UsersHandler(Resource):
    @token_required
    def post(data,currentUser):           
        return postUser(data)
    
    @token_required
    def get(data,currentUser):                 
        return getAllUsers()
        

@users.route('/<string:cod>')
class UsersHandler(Resource):
    @token_required
    def get(data,currentUser,cod):
        return getUsuario(cod)  
        
    @token_required
    def put(data,currentUser,cod):            
        return updateUsuario(data, cod)
     

@users.route('/account/activate')
class UsersActivate(Resource):
    @token_required
    def get(data,currentUser):
        return activateUser(currentUser)


@users.route('/account/recover')
class UsersRecover(Resource):
    def post(self):
        data = self.api.payload
        return requestRecoverPass(data)

  
@users.route('/account/restore')
class UsersRestore(Resource):
    @token_required
    def post(data,currentUser):
        return restorePass(data,currentUser)


@users.route('/account/user')
class UsersAccount(Resource):
    @token_required
    def post(data,currentUser):
        return accountUser(data)