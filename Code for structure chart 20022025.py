# calculate the final grade for a student
# based on 3 assessment scores entered using a 
# then display results

def main():
    scores = []
    scores = collect_scores(scores)
    while len(scores) != 3:
        scores = collect_scores(scores)
    
    
    calculate_average(scores)
    average = calculate_average(scores)
    determine_grade(average)
    display_results()

def collect_scores(scores):
    for i in range(3):
        score - int(input("Enter score: "))
        scores.append(score)
        return scores
    
def calculate_average(scores):
    average = average(scores)
    return average

def determine_grade(average):
    if average >= 90:
        grade = "Band 6"
    elif average >= 80:
        grade = "Band 5"
    elif average >= 70:
        grade = "Band 4"
    else:
        grade = "Fail"
    return grade

def display_results(average,grade):
    print(f"Average: {average}, Grade: {grade}")