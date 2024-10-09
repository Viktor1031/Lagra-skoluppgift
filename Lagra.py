class user:
    def __init__(self, username, password, startItems):
        self.username = username
        self.password = password
        self.inventory = startItems
print("Welcome to Lagra")
allUsers = []
allUsers.append(user("Viktor", "python", []))
allUsers.append(user("Måns", "1234", []))
allUsers.append(user("Blazemaster420", "420", ["blunt", "lighter", "doritos"]))

def checkInput(username, password):
    for user in allUsers:
        if (user.username == username) and (user.password == password):
              return user
    return None

def logInScreen():
    loggingIn = True
    while loggingIn:
        logInSelectionScreen = True
        while logInSelectionScreen:
            print("1) Log in")
            print("q) Quit")
            user_input = input()
            if user_input == "q":
                exit()
            elif user_input == "1":
                logInSelectionScreen = False
        username_input = input()
        password_input = input()
        userLoggingIn = checkInput(username_input, password_input)
        if userLoggingIn != None:
            print("Logged in")
            loggingIn = False
            print("These are your items:")
            showInventory(userLoggingIn)
            return userLoggingIn
        else:
            print("Try different username or password")

def showInventory(user):
    i = 1
    for e in user.inventory:
        print(str(i) + ") " + e)
        i += 1
    print()

def mainScreen(userLoggedIn):
    while True:
        print("Select an action")
        print("a) Add items")
        print("b) List items")
        print("c) Log out")
        user_input = input()
        if user_input == "a":
            print("What do you want to add?")
            user_input = input()
            userLoggedIn.inventory.append(user_input)
            print("You have added " + user_input)
        elif user_input == "b":
            showInventory(userLoggedIn)
        elif user_input == "c":
            print("You have logged out\n")
            userLoggedIn = logInScreen()
        else:
            print("type a, b or c")

userLoggedIn = logInScreen()
mainScreen(userLoggedIn)
