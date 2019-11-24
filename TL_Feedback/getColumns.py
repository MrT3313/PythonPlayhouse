
def getColumns(listParam):
    # Set Columns for list comprehension
    # Col Headers
        # 1. "Date => Submitted At (Simple Date)"
        # 2. "Student => Student"
        # 3. "TL Feedback"
        # 4. "TL Rating"

    # Create Col Index Dictionary 
    colIndex = {
        'Date': 5,
        'Student': 2,
        'feedback_for_tl': 6,
        'student_tl_rating': 7,
    }

    # List to Return 
    filteredList = []
    
    # Filter List
    print(type(listParam))
    for i in listParam:
        selectedItems = [
            i[colIndex['Date']], 
            i[colIndex['Student']], 
            i[colIndex['feedback_for_tl']], 
            i[colIndex['student_tl_rating']]]
        # print(selectedItems)

        # Append selection to filtered list
        filteredList.append(selectedItems)
    
    # print(filteredList)
    return(filteredList)
    