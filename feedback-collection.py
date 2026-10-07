feedbacks = []

while True:
    print("\n===== FEEDBACK COLLECTION SYSTEM =====")
    print("1. Give Feedback")
    print("2. View Feedback")
    print("3. Delete Feedback")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        feedback = input("Enter your feedback: ")

        rating = int(input("Give rating (1-5): "))

        if rating < 1 or rating > 5:
            print("Rating must be between 1 and 5!")
        else:
            feedbacks.append({
                "name": name,
                "feedback": feedback,
                "rating": rating
            })

            print("Feedback submitted successfully!")

    
    elif choice == "2":
        if not feedbacks:
            print("No feedback available!")
        else:
            print("\n===== ALL FEEDBACK =====")

            for i, item in enumerate(feedbacks, start=1):
                print("\nFeedback", i)
                print("Name:", item["name"])
                print("Feedback:", item["feedback"])
                print("Rating:", item["rating"], "/ 5")


    elif choice == "3":
        if not feedbacks:
            print("No feedback available!")
        else:
            name = input("Enter name to delete feedback: ")

            found = False

            for item in feedbacks:
                if item["name"].lower() == name.lower():
                    feedbacks.remove(item)
                    print("Feedback deleted successfully!")
                    found = True
                    break

            if not found:
                print("Feedback not found!")


    elif choice == "4":
        print("Thank you for using Feedback Collection System!")
        break

    else:
        print("Invalid choice!")
