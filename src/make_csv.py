import csv

input_path = "../data/raw/transcripts.txt"
output_path = "b99_clean_lines.csv"

name_map = {
    "CHARLES" : "Charles",
    "BOYLE" : "Charles",
    "ROSA" : "Rosa",
    "TERRY" : "Terry"
}

with open(input_path, "r", encoding = "utf-8") as f, open(output_path, "w", encoding = "utf-8", newline = "") as out:
    writer = csv.writer(out)
    writer.writerow(["character", "text"])

    for line in f:
        line = line.strip()
        if not line:
            continue

        #removing the "[coughs]", "[laughs]"...
        if "[" in line or "]" in line:
            continue

        upper = line.upper()

        for variant, canonical in name_map.items():
            prefix = variant + ":"
            if upper.startswith(prefix):
                text = line.split(":", 1)[1].strip()
                writer.writerow([canonical, text])
                break
