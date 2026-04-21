if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.append(score)
    
    unique_scores = sorted(set(scores))
    second_lowest_grade = unique_scores[1]
    result_names = []
    for name, score in students:
        if score == second_lowest_grade:
            result_names.append(name)
    result_names.sort()
    
    for name in result_names:
        print(name)