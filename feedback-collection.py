feedbacks =[]

while True:
    print("\n ==== Feedback Collection System ====")
    print("'1. Give Feedback'\n 2. 'View Feedback'\n 3. 'Exit'")
    
    choice =input("Enter your choice:")
    
    if choice =="1":
        name =input("Enter your name:")
        feedback =input("Enter your feedback:")
        rating = int(input("Give rating(1-5)"))
        
        feedbacks.append({
            "name": name,
            "feedback": feedback,
            "rating": rating
        })
        print("Feedback submitted successfully!")
        
    elif choice =="2":
        if not feedbacks:
            print("No feedback available!")
            
        else:
            print("\n ==== All Feedback ====")
            
            for item in feedbacks:
                print("\n Name:",item["name"])
                print("Feedback:",item["feedback"])
                print("Ratingaa:",item["rating"],"/ 5")
                
    elif choice =="3":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")