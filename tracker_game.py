while True:
    user_input = input("Enter your game score (or type 'stop' to quit): ")
    cleaned_input = user_input.strip().lower()

    if cleaned_input == "stop":
        print("Game session ended!")
        break

    try:
        score = int(cleaned_input)
    except ValueError:
        print("Invalid input. Please enter a number or 'stop'.")
        continue

    if score > 100:
        print("Wow! That's a new high score!")
    else:
        print("Good try, keep playing!")