import csv
import random
import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("input_file")
    parser.add_argument("output_file")
    parser.add_argument("n", type=int, nargs="?", default=100)


    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file
    num_lines = args.n

    # Read lines
    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)  # skip header
        rows = list(reader)

    if num_lines > len(rows):
        raise ValueError(
            f"Requested {num_lines} lines but only {len(rows)} available in {input_file}"
        )
    
    sample = random.sample(rows, num_lines)

    with open(output_file, "w", encoding="utf-8", newline="") as out:
        writer = csv.writer(out)
        writer.writerow(["character", "text"])
        writer.writerows(sample)

if __name__ == "__main__":
    main()