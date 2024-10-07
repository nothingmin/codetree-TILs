# 학생들의 초기 점수 설정
students = {
    "Bessie": 0,
    "Elsie": 0,
    "Daisy": 0,
    "Gertie": 0,
    "Annabelle": 0,
    "Maggie": 0,
    "Henrietta": 0
}

# 입력 받기
N = int(input().strip())  # 점수를 부여한 횟수 N 입력
for _ in range(N):
    name, score = input().split()  # 학생 이름과 점수를 공백으로 구분해 입력
    score = int(score)
    students[name] += score  # 해당 학생의 점수 누적

# 모든 학생들의 점수를 리스트로 추출
scores = list(students.values())

# 중복을 제거하고 오름차순 정렬
unique_scores = sorted(set(scores))

# 두 번째로 낮은 점수 찾기
if len(unique_scores) < 2:
    print("Tie")  # 모든 학생의 점수가 같으면 Tie
else:
    second_lowest_score = unique_scores[1]  # 두 번째로 낮은 점수

    # 두 번째로 낮은 점수를 가진 학생 찾기
    second_lowest_students = [name for name, score in students.items() if score == second_lowest_score]

    # 두 번째로 낮은 점수를 가진 학생이 여러 명인 경우
    if len(second_lowest_students) > 1:
        print("Tie")
    else:
        print(second_lowest_students[0])