import random
import math

# input lists of teams and students
teams = [f'team{i}' for i in range(1, 7)]
students = [f'student{i}' for i in range(1, 30)]
teams_per_student = 2 # number of teams to be marked by each student

max_students = math.ceil(len(students) / len(teams) * teams_per_student) # each student is assigned 2 groups. define maximum students per group

assignment = {} # initialize empty assignments dictionary

for i in range(len(students)):
    assignment[students[i]] = random.sample(teams, teams_per_student) # assign random unique teams per student

    teams_count = dict.fromkeys(teams, 0) # count number of students assigned per team
    for i in sum(assignment.values(), []):
        if i in teams_count:
            teams_count[i] += 1
        else:
            teams_count[i] = 1

    if len(teams) > 2: # loop to remove teams that have enough students assigned
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