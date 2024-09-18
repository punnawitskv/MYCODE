def parse_input(input_str):
    teams = input_str.split('/')
    data = []
    for team in teams:
        name, wins, loss, draws, scored, conceded = team.split(',')
        wins, loss, draws, scored, conceded = int(wins), int(loss), int(draws), int(scored), int(conceded)
        points = wins * 3 + draws
        goal_difference = scored - conceded
        data.append((name, points, goal_difference))
    return data

def custom_sort(data):
    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):
            if (data[j][1] < data[j + 1][1]) or (data[j][1] == data[j + 1][1] and data[j][2] < data[j + 1][2]):
                data[j], data[j + 1] = data[j + 1], data[j]

def generate_results(data):
    results = []
    for name, points, goal_difference in data:
        results.append([name, {'points': points}, {'gd': goal_difference}])
    return results

def process_football_data(input_str):
    data = parse_input(input_str)
    custom_sort(data)
    return generate_results(data)

input_str = input('Enter Input : ')
output = process_football_data(input_str)
print("== results ==")
for line in output:
    print(line)
