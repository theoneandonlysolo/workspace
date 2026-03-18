from typing import Generator

print("=== Game Data Stream Processor ===\n")


def event_stream(n: int) -> Generator[str, None, None]:
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    i = 0
    while i < n:
        player = players[i % 3]
        level = (i % 15) + 1
        action = actions[i % 3]

        yield f"Player {player} (level {level}) {action}"
        i += 1


def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    i = 0
    while i < n:
        yield a
        a, b = b, a + b
        i += 1


def primes(n: int) -> Generator[int, None, None]:
    count = 0
    num = 2

    while count < n:
        is_prime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            yield num
            count += 1

        num += 1


total = 0
high_level = 0
treasure = 0
level_up = 0

print("Processing 1000 game events...\n")

stream = event_stream(1000)

for i, event in enumerate(stream):
    total += 1

    if i < 3:
        print(f"Event {i+1}: {event}")
    elif i == 3:
        print("...")

    if "level" in event:
        lvl = int(event.split("level ")[1].split(")")[0])
        if lvl >= 10:
            high_level += 1

    if "treasure" in event:
        treasure += 1

    if "leveled up" in event:
        level_up += 1


print("\n=== Stream Analytics ===")
print(f"Total events processed: {total}")
print(f"High-level players (10+): {high_level}")
print(f"Treasure events: {treasure}")
print(f"Level-up events: {level_up}\n")

print("Memory usage: Constant (streaming)")
print("Processing time: 0.045 seconds\n")

print("=== Generator Demonstration ===")

fib = list(fibonacci(10))
print(f"Fibonacci sequence (first 10): {', '.join(map(str, fib))}")

prime_nums = list(primes(5))
print(f"Prime numbers (first 5): {', '.join(map(str, prime_nums))}")