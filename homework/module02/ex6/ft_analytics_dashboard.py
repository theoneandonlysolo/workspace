print("=== Game Analytics Dashboard ===\n")

players = [
    {
        "name": "alice",
        "score": 2300,
        "active": True,
        "region": "north",
        "achievements": ["first_kill", "level_10", "treasure_hunter", "speed_demon", "collector"]
    },
    {
        "name": "bob",
        "score": 1800,
        "active": True,
        "region": "east",
        "achievements": ["first_kill", "level_10", "boss_slayer"]
    },
    {
        "name": "charlie",
        "score": 2150,
        "active": True,
        "region": "central",
        "achievements": ["level_10", "treasure_hunter", "boss_slayer", "speed_demon", "explorer", "strategist", "survivor"]
    },
    {
        "name": "diana",
        "score": 1600,
        "active": False,
        "region": "north",
        "achievements": ["first_kill", "collector", "merchant"]
    }
]

print("=== List Comprehension Examples ===")
high_scorers = [player["name"] for player in players if player["score"] > 2000]
score_doubles = [player["score"] * 2 for player in players]
active_players = [player["name"] for player in players if player["active"]]

print(f"High scorers (>2000): {high_scorers}")
print(f"Scores doubled: {score_doubles}")
print(f"Active players: {active_players}\n")

print("=== Dict Comprehension Examples ===")
player_scores = {player["name"]: player["score"] for player in players}
score_categories = {
    player["name"]: (
        "high" if player["score"] > 2000
        else "medium" if player["score"] >= 1700
        else "low"
    )
    for player in players
}
achievement_counts = {player["name"]: len(player["achievements"]) for player in players}

print(f"Player scores: {player_scores}")
print(f"Score categories: {score_categories}")
print(f"Achievement counts: {achievement_counts}\n")

print("=== Set Comprehension Examples ===")
unique_players = {player["name"] for player in players}
unique_achievements = {
    achievement
    for player in players
    for achievement in player["achievements"]
}
active_regions = {player["region"] for player in players if player["active"]}

print(f"Unique players: {unique_players}")
print(f"Unique achievements: {unique_achievements}")
print(f"Active regions: {active_regions}\n")

print("=== Combined Analysis ===")
total_players = len(players)
total_unique_achievements = len(unique_achievements)
average_score = sum(player["score"] for player in players) / len(players)
top_player = max(players, key=lambda player: player["score"])

print(f"Total players: {total_players}")
print(f"Total unique achievements: {total_unique_achievements}")
print(f"Average score: {average_score}")
print(
    f"Top performer: {top_player['name']} "
    f"({top_player['score']} points, {len(top_player['achievements'])} achievements)"
)