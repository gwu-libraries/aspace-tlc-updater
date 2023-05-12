class User:
    def __init__(self, user_dict):
        self.session = user_dict['session']
        self.email = user_dict['user']['email']
        self.permissions = user_dict['user']['permissions']