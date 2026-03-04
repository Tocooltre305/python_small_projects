def exam_marks_checker():
    pass_mark = 50
    subjects_passed = 0
    subjects_failed = 0
    while True:
        entry = input("Enter subject mark (q to quit): ")
        if entry.lower() == 'q':
            break
        mark = float(entry)
        if mark >= pass_mark:
            print(f"Result: PASS (Mark: {mark})")
            subjects_passed += 1
        else:
            print(f"Result: FAIL (Mark: {mark})")
            subjects_failed += 1
    total_subjects = subjects_passed + subjects_failed
    print("\n--- Final Results ---")
    print(f"Total Subjects tracked: {total_subjects}")
    print(f"Passed: {subjects_passed}")
    print(f"Failed: {subjects_failed}")
    if total_subjects > 0:
        if subjects_passed == total_subjects:
            print("Perfect record! You passed every subject.")
        elif subjects_passed > 0:
            print(f"You passed {subjects_passed} out of {total_subjects} subjects.")
        else:
            print("No subjects were passed this time.")
    else:
        print("No data entered.")
exam_marks_checker()