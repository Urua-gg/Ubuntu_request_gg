def list_sum():
    numbers = input("Enter integers separated by spaces: ")
    num_list = [int(num) for num in numbers.split()]
    total = sum(num_list)
    print("The sum of all integers is:", total)


def favorite_books():
    books = ("The Mastermind", "My Life as a Pauper", "Storyteller", "The Brave Warrior", "The Success")
    print("\nMy Favorite Books:")
    for book in books:
        print(book)


def person_info():
    person = {}
    person["name"] = input("Enter your name: ")
    person["age"] = int(input("Enter your age: "))
    person["favorite_color"] = input("Enter your favorite color: ")
    print("\nPerson information:", person)


def common_elements():
    set1 = set(map(int, input("Enter integers for the first set (space-separated): ").split()))
    set2 = set(map(int, input("Enter integers for the second set (space-separated): ").split()))
    common_set = set1.intersection(set2)
    print("Common elements:", common_set)


def odd_length_words():
    words = ["apple", "banana", "pear", "kiwi", "mango", "grape"]
    odd_length_words = [word for word in words if len(word) % 2 != 0]
    print("Words with an odd number of characters:", odd_length_words)


# Menu for user to select a task
while True:
    print("\n=== PYTHON TASK MENU ===")
    print("1. Create a list of integers and compute the sum")
    print("2. Display your favorite books")
    print("3. Store and display person information using a dictionary")
    print("4. Find common elements in two sets of integers")
    print("5. Display words with odd number of characters")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == '1':
        list_sum()
    elif choice == '2':
        favorite_books()
    elif choice == '3':
        person_info()
    elif choice == '4':
        common_elements()
    elif choice == '5':
        odd_length_words()
    elif choice == '6':
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
