def greet_user():
    """Display a simple greeting. """
    print("Hello!")

greet_user()

#modifying the function greet_user()
def greet_user(username):
    print(f"Hello, {username.title()}! ")

greet_user('Jesse')