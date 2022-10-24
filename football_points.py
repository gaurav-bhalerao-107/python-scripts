def football_points(wins: int, draws: int) -> int:
    return (wins * 3) + (draws * 1)

a, b, c = [int(x) for x in input().split()]

points = football_points(a, b)
print(points)
