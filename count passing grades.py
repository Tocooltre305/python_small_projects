def pass_or_fail_checker():
    passed = 0
    while True:
        score = input("Enter your score (q to quit): ").lower()
        if score == "q":
            break       
        score = int(score)
        if score >= 50:
            passed += 1
            print("Pass")
        elif score < 50:
            print("Fail")
    return passed
count = pass_or_fail_checker()
print(f"Scores entered that are passing scores : {count}")