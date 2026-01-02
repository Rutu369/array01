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

    # main/master branch output
    print("=== main/master branch output ===")
    print(f"Count of scores: {len(scores)}")
    print(f"Sum: {total}")
    print(f"Average: {avg}")

    # local branch output (your added part)
    print("\n=== local branch output (max & min) ===")
    print(f"Maximum: {max(scores)}")
    print(f"Minimum: {min(scores)}")

if __name__ == "__main__":
    main()
