# Import necessary libraries
from typing import List, Tuple

# Define a global dictionary to store running stats
# The key will be the Discord username, and the value will be a list of tuples (time, distance, upload date)
running_stats = {}

# Function to update running stats
def update_running_stats(username: str, time: str, distance: float, date: str) -> str:
    if username not in running_stats:
        running_stats[username] = (time, distance, date)
    else:
        if distance > running_stats[username][1]:  # Compare distances
            running_stats[username] = (time, distance, date)
            return f"New best distance updated for {username}."
        else:
            # If the current run's distance is not a new best, do not update
            return f"No update. Your best distance is still {running_stats[username][1]} miles."
    return f"Running stats updated for {username}."

# Function to get the leaderboard
def get_leaderboard() -> str:
    leaderboard = sorted(running_stats.items(), key=lambda x: x[1][1], reverse=True)
    leaderboard_str = "🏆 Leaderboard 🏆:\n"
    medals = ["🥇", "🥈", "🥉", "🏅"]
    for idx, (user, run) in enumerate(leaderboard, 1):
        time = run[0]
        distance = run[1]
        # Add medals to the top 3
        medal = medals[idx - 1] if idx <= 3 else medals[3]
        # Displaying both time and distance
        leaderboard_str += f"{medal} {user} - Best Time: {time}, Distance: {distance} miles\n"
    return leaderboard_str

# Modify the get_response function to handle running stat updates and leaderboard requests
def get_response(user_input: str, username: str) -> str:
    lowered = user_input.lower()
    parts = lowered.split()

    if parts[0] == '/update' and len(parts) == 4:
        _, time, distance, date = parts
        return update_running_stats(username, time, float(distance), date)
    elif parts[0] == '/leaderboard':
        return get_leaderboard()
    elif 'hello' in lowered:
        return '해위~'
    else:
        return '뭐라카노'