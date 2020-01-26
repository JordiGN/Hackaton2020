class CreateUserService:
    def __init__(self):
        self.model = UserModel()
        
    def create(self, params):
        self.model.create(params["name"], params["email"],params["psswd"])