print("Name- Shantnu")
print("Enrollment No.: 0103AL231190")
import random
import datetime

# Sample Quiz Data
quiz_data = {
    "DSA": [
        ("What is the time complexity of binary search?", ["O(n)", "O(log n)", "O(n log n)", "O(1)"], "O(log n)"),
        ("Which data structure uses FIFO?", ["Stack", "Queue", "Tree", "Graph"], "Queue"),
        ("Which traversal gives sorted output in BST?", ["Inorder", "Preorder", "Postorder", "Levelorder"], "Inorder"),
        ("Which data structure is used in recursion?", ["Queue", "Stack", "Heap", "Linked List"], "Stack"),
        ("Which algorithm is used to find shortest path?", ["DFS", "BFS", "Dijkstra", "Kruskal"], "Dijkstra")
    ],
    "DBMS": [
        ("Which key uniquely identifies a record?", ["Primary Key", "Foreign Key", "Candidate Key", "Composite Key"], "Primary Key"),
        ("Which command is used to remove a table?", ["DELETE", "DROP", "REMOVE", "CLEAR"], "DROP"),
        ("Which language is used to query data?", ["DDL", "DML", "DQL", "DCL"], "DQL"),
        ("Normalization helps in?", ["Data Redundancy", "Data Duplication", "Data Retrieval", "Data Storage"], "Data Redundancy"),
        ("Which is not a DDL command?", ["CREATE", "ALTER", "SELECT", "DROP"], "SELECT")
    ],
    "PYTHON": [
        ("Which keyword defines a function?", ["def", "func", "lambda", "function"], "def"),
        ("Which data type is immutable?", ["List", "Set", "Dictionary", "Tuple"], "Tuple"),
        ("Which operator is used for power?", ["^", "**", "//", "%"], "**"),
        ("Which method adds an element to a list?", ["append()", "add()", "insert()", "extend()"], "append()"),
        ("What is the output of print(type([]))?", ["list", "tuple", "dict", "set"], "list")
    ]
}

# User Data

users = {}
logged_in_user = None

# Functions

def register():
    print("\n=== Registration ===")
    username = input("Enter username: ")
    if username in users:
        print("User already exists!")
        return
    password = input("Enter password: ")
    contact = input("Enter contact number: ")
    name = input("Enter your full name: ")
    users[username] = {"password": password, "contact": contact, "name": name, "scores": []}
    print("Registration successful!")

def login():
    global logged_in_user
    print("\n=== Login ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]["password"] == password:
        logged_in_user = username
        print(f"Welcome, {users[username]['name']}!")
    else:
        print("Invalid username or password.")

def logout():
    global logged_in_user
    logged_in_user = None
    print("Logged out successfully.")

def attempt_quiz():
    if not logged_in_user:
        print("Please login first.")
        return
    print("\nSelect Category:")
    for i, cat in enumerate(quiz_data.keys(), start=1):
        print(f"{i}. {cat}")
    choice = int(input("Enter choice: "))
    category = list(quiz_data.keys())[choice - 1]
    questions = random.sample(quiz_data[category], min(5, len(quiz_data[category])))
    
    score = 0
    for i, (q, options, ans) in enumerate(questions, start=1):
        print(f"\nQ{i}. {q}")
        for j, opt in enumerate(options, start=1):
            print(f"{j}. {opt}")
        user_ans = input("Enter option number: ")
        if options[int(user_ans) - 1] == ans:
            score += 1
    total = len(questions)
    print(f"\n✅ You scored {score}/{total}")
    
    users[logged_in_user]["scores"].append({
        "category": category,
        "marks": score,
        "total": total,
        "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

def view_score():
    if not logged_in_user:
        print("Please login first.")
        return
    print("\n=== Your Scores ===")
    for s in users[logged_in_user]["scores"]:
        print(f"{s['category']:10} | {s['marks']}/{s['total']} | {s['datetime']}")

def update_profile():
    if not logged_in_user:
        print("Please login first.")
        return
    print("\n=== Update Profile ===")
    new_name = input("Enter new name: ")
    new_contact = input("Enter new contact number: ")
    users[logged_in_user]["name"] = new_name
    users[logged_in_user]["contact"] = new_contact
    print("Profile updated successfully!")

def view_profile():
    if not logged_in_user:
        print("Please login first.")
        return
    print("\n=== Profile ===")
    u = users[logged_in_user]
    print(f"Name: {u['name']}")
    print(f"Contact: {u['contact']}")
    print(f"Username: {logged_in_user}")

# Main Menu

while True:
    print("\n====== QUIZ SYSTEM ======")
    print("1. Registration")
    print("2. Login")
    print("3. Quiz Menu")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        if not logged_in_user:
            print("Please login first.")
        else:
            while True:
                print("\n--- Quiz Menu ---")
                print("3.1 Attempt Quiz")
                print("3.2 View Score")
                print("3.3 Update Profile")
                print("3.4 View Profile")
                print("3.5 Logout")
                print("3.6 Back to Main Menu")
                sub = input("Enter choice: ")

                if sub == '3.1':
                    attempt_quiz()
                elif sub == '3.2':
                    view_score()
                elif sub == '3.3':
                    update_profile()
                elif sub == '3.4':
                    view_profile()
                elif sub == '3.5':
                    logout()
                    break
                elif sub == '3.6':
                    break
                else:
                    print("Invalid choice.")
    elif choice == '4':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice.")
