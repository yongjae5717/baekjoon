import sys

input = sys.stdin.readline

n = int(input())
student_list = list([0] * n for _ in range(n))
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
students = list()
for _ in range(n ** 2):
    # index 0: 학생의 번호, 나머지: 좋아하는 학생의 번호
    student = list(map(int, input().split()))
    students.append(student)
    temp = list()
    for i in range(n):
        for j in range(n):
            if student_list[i][j] == 0:
                like = 0
                n_like = 0
                for k in range(len(d)):
                    dx = i + d[k][0]
                    dy = j + d[k][1]
                    if (0 <= dx < n) and (0 <= dy < n):
                        if student_list[dx][dy] in student[1:]:
                            like += 1
                        if student_list[dx][dy] == 0:
                            n_like += 1
                temp.append([like, n_like, i, j])
    temp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    x, y = temp[0][2], temp[0][3]
    student_list[x][y] = student[0]

# for i in student_list:
#     print(i)

result_point = 0
students.sort()
for i in range(n):
    for j in range(n):
        count = 0
        for k in range(len(d)):
            dx = i + d[k][0]
            dy = j + d[k][1]
            if 0 <= dx < n and 0 <= dy < n:
                if student_list[dx][dy] in students[student_list[i][j] - 1]:
                    count += 1
        if count != 0:
            result_point += 10 ** (count -1)

print(result_point)