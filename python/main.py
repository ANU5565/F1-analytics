from drivers import get_all_drivers
from teams import get_team_standings

print("Drivers:")
for d in get_all_drivers():
    print(d)

print("\nTeam Standings:")
for t in get_team_standings():
    print(t)
