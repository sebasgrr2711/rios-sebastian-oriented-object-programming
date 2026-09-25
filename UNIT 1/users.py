class user:
    def __init__(self, id_user, name):
        self.id = id_user
        self.name = name

    def show_user_info(self):
        return f"{self.id} - {self.name}"
