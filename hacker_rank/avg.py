if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(student_marks[query_name])
    avg=student_marks[name][0]+student_marks[name][1]+student_marks[name][2]
    avg=avg/3
    print('{:.2f}'.format(avg))