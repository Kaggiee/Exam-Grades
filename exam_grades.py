def main():
    """
    This function will ask the user to input 3 exam scores using input. Then, it will display
    a formatted table of the exam scores with a calculated average and corresponding letter
    grade for each.
    """
    score_1 = float(input('Enter Exam 1 score: '))
    score_2 = float(input('Enter Exam 2 score: '))
    score_3 = float(input('Enter Exam 3 score: '))
    average = calc_average(score_1, score_2, score_3)

    print('\nScore\t\tNumeric Grade\tLetter Grade')
    print('----------------------------------------------------')
    print(f'Exam 1:  {score_1:12,.1f}\t\t{determine_grade(score_1):12}')
    print(f'Exam 2:  {score_2:12,.1f}\t\t{determine_grade(score_2):12}')
    print(f'Exam 3:  {score_3:12,.1f}\t\t{determine_grade(score_3):12}')
    print(f'Average: {average:12,.1f}\t\t{determine_grade(average):12}')

def calc_average(letter_1, letter_2, letter_3):
    """
    This function will accept three test scores as arguments and return the average of the
    scores.
    """
    average = letter_1 + letter_2 + letter_3
    return average/3

def determine_grade(grade):
    """
    This function will accept a test score as an argument and return a letter grade for the
    score based on a predetermined scale.
    """
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

# Call the main function.  If this isn't in the file, the code won't run.
if __name__ == '__main__':
    main()
