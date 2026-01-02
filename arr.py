import sys
import os

def parse_scores_from_string(s):
    scores = []
    for part in s.replace(",", " ").split():
        try:
            scores.append(float(part))
        except ValueError:
            pass
    return scores

def read_scores():
    # Priority: CLI args > SCORES env var > scores.txt > interactive prompt
    if len(sys.argv) > 1:
        return parse_scores_from_string(" ".join(sys.argv[1:]))

    env = os.getenv("SCORES")
    if env:
        return parse_scores_from_string(env)

    if os.path.isfile("scores.txt"):
        with open("scores.txt", "r") as f:
            return parse_scores_from_string(f.read())

    raw = input("Enter scores separated by spaces or commas: ")
    return parse_scores_from_string(raw)

def main():
    scores = read_scores()

    if not scores:
        print("No valid scores provided.")
        sys.exit(1)

    total = sum(scores)
    avg = total / len(scores)

    print("=== main/master branch output ===")
    print(f"Count of scores: {len(scores)}")
    print(f"Sum: {total}")
    print(f"Average: {avg}")

if __name__ == "__main__":
    main()
