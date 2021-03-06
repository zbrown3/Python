if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average_marks = sum(student_marks[query_name]) / 3
    format_marks = "{:.2f}".format(average_marks)
    print(format_marks)