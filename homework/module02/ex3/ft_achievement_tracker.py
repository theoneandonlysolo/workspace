print("=== Achievement Tracker System ===\n")

alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
bob = {"first_kill", "level_10", "boss_slayer", "collector"}
charlie = {"level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"}

print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}\n")

print("=== Achievement Analytics ===")

all_achievements = alice.union(bob).union(charlie)
print(f"All unique achievements: {all_achievements}")
print(f"Total unique achievements: {len(all_achievements)}\n")

common = alice.intersection(bob).intersection(charlie)
print(f"Common to all players: {common}\n")

rare = all_achievements.difference(
    alice.intersection(bob).union(alice.intersection(charlie)).union(bob.intersection(charlie))
)
print(f"Rare achievements (1 player): {rare}\n")

print("Alice vs Bob common:", alice.intersection(bob))
print("Alice unique:", alice.difference(bob))
print("Bob unique:", bob.difference(alice))