import random
import math

# input student/team assignments as dictionary and extract separate teams/students lists
teams_students = {'team1': [f'student{i}' for i in range(1, 5)],
                  'team2': [f'student{i}' for i in range(6, 10)],
                  'team3': [f'student{i}' for i in range(11, 15)],
                  'team4': [f'student{i}' for i in range(16, 20)],
                  'team5': [f'student{i}' for i in range(21, 25)],
                  'team6': [f'student{i}' for i in range(25, 30)]}

teams = list(teams_students.keys())
students = sum(teams_students.values(), [])

teams_per_student = 2 # number of teams to be marked by each student
max_students = math.ceil((len(students) - (len(students) / len(teams))) / len(teams) * teams_per_student) # define maximum students to be assigned per group

assignment = {}

for i in range(len(students)):
    mask = [key for key, val in teams_students.items() if students[i] in val]
    
    try:
        assignment[students[i]] = random.sample([a for a in teams if a not in mask], teams_per_student) # assign random unique teams per student, masking own team from list
    except ValueError as e:
        raise Exception('Teams list minus mask resulted in too few groups. Rerun until it works!') from e

    teams_count = dict.fromkeys(teams, 0) # count number of students assigned per team
    for i in sum(assignment.values(), []):
        if i in teams_count:
            teams_count[i] += 1
        else:
            teams_count[i] = 1

    if len(teams) > teams_per_student: # remove teams that have enough students assigned
        for i in teams[:]:
            if teams_count.get(i) >= max_students:
                teams.remove(i)
    
    else:
        continue

# Print nicely formatted output
print("Students assigned per team: ")
print(teams_count)
print("{:<30} {:<20} {:<20}".format('Student','Team 1', 'Team 2'))
print("{:<30} {:<20} {:<20}".format('-------','-------', '-------'))
for k,v in assignment.items():
    t1, t2 = v
    print("{:<30} {:<20} {:<20}".format(k, t1, t2))
