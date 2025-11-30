import os
import glob
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

# Get all annotated CSV files
DATA_FOLDER = os.path.join(WORKING_DIR, "..", "data", "processed", "final_coded_300")
files = sorted(glob.glob(os.path.join(DATA_FOLDER, "*.csv")))

# Load data from all annotated files
dfs = []
for fpath in files:
    df_tmp = pd.read_csv(fpath)

    # detect text column and label column
    text_col = next((c for c in df_tmp.columns if c.lower() == "text"), None)
    label_col = next((c for c in df_tmp.columns if c.lower() == "final_label"), None)

    sub = df_tmp[[text_col, label_col]]
    sub["source_file"] = os.path.basename(fpath)
    dfs.append(sub)

df = pd.concat(dfs, ignore_index=True)
df["text"] = df["text"].astype(str)

# Fit global vectorizer (global IDF across all files)
vectorizer = TfidfVectorizer(stop_words="english", lowercase=True, ngram_range=(1, 1), min_df=1)
X = vectorizer.fit_transform(df["text"])  # shape: (n_docs, n_terms)
features = vectorizer.get_feature_names_out()

# Helper to get top n terms for a label
def top_terms_for_label(label, top_n=10):
    idx = df.index[df["final_label"] == label].tolist()
    if not idx:
        return []
    block = X[idx]  # submatrix
    sums = block.sum(axis=0).A1
    scores = sums / len(idx)  # mean aggregation
    top_idx = scores.argsort()[::-1][:top_n]
    return [(features[i], float(scores[i]), len(idx)) for i in top_idx]

# Compute for every label (use mean aggregation by default to avoid bias from label size)
labels = sorted(df["final_label"].unique())
rows = []
for lab in labels:
    terms = top_terms_for_label(lab, top_n=10)
    print(lab)
    for term, score, doc_count in terms:
        print(f"  {term}\t{score:.4f}\t(doc_count={doc_count})")
        rows.append((lab, term, score, doc_count))
    print()

# Save results
out_path = os.path.join(WORKING_DIR, "..", "data", "tf-idf", "top10_tfidf_per_label.csv")
pd.DataFrame(rows, columns=["label", "term", "tfidf_mean", "doc_count"]).to_csv(out_path, index=False)
print("Saved:", out_path)