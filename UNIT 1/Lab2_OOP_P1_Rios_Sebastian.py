class User:
    def __init__(self, name, email, age, password):
        self.name = name
        self.email = email
        self.age = age
        self.__password = password

    def change_pass(self, new_password):
        self.__password = new_password
        print("Password changed successfully.")

    def create_post(self, title, content):
        # El usuario crea y guarda el post directamente
        new_post = Post(title, content, self.name)
        return new_post

    def create_comment(self, content):
        new_comment = Comment(content, self.name)
        print(f"Comment created successfully by {self.name}: '{content}'")
        return new_comment

    def send_message(self, content, receiver):
        new_message = Message(content, self.name, receiver)
        print(f"Message sent to {receiver}: '{content}'")
        return new_message


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        print(f"Post '{self.title}' created successfully by {self.author}.")

    def edit_post(self, new_content):
        old_content = self.content
        self.content = new_content
        print(f"Post edited. Old: '{old_content}' -> New: '{self.content}'")


class Comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author

    def edit_comment(self, new_content):
        old_content = self.content
        self.content = new_content
        print(f"Comment edited. Old: '{old_content}' -> New: '{self.content}'")


class Message:
    def __init__(self, content, sender, receiver):
        self.content = content
        self.sender = sender
        self.receiver = receiver

    def edit_message(self, new_content):
        old_content = self.content
        self.content = new_content
        print(f"Message edited. Old: '{old_content}' -> New: '{self.content}'")


# --- Ejemplo de uso ---
user1 = User("sebas", "sebas@email.com", 12, "sebastian123")

# Crear post
mi_post = user1.create_post("First Post", "Fotos de mis vacaciones")
mi_post.edit_post("Fotos actualizadas de las vacaciones")

# Crear comentario
mi_comentario = user1.create_comment("Practica 1 de POO")

# Enviar mensaje
mi_mensaje = user1.send_message("Hola, ¿cómo estás?", "Juan")
