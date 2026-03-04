def pass_or_fail_checker():
    while True:
        score = input("Enter your score (q to quit): ").lower()
        if score == "q":
            break       
        score = int(score)
        if score >= 50:
            print("Pass")
        elif score < 50:
            print("Fail")

pass_or_fail_checker()