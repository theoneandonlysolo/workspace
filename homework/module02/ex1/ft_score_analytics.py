import sys

print("=== Player Score Analytics ===")

if len(sys.argv) == 1:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
else:
    scores = []
    i = 1

    while i < len(sys.argv):
        try:
            score = int(sys.argv[i])
            scores.append(score)
        except:
            pass
        i += 1

    if len(scores) == 0:
        print("No valid scores provided.")
    else:
        total = sum(scores)
        count = len(scores)
        average = total / count
        highest = max(scores)
        lowest = min(scores)
        score_range = highest - lowest

        print(f"Scores processed: {scores}")
        print(f"Total players: {count}")
        print(f"Total score: {total}")
        print(f"Average score: {average}")
        print(f"High score: {highest}")
        print(f"Low score: {lowest}")
        print(f"Score range: {score_range}")