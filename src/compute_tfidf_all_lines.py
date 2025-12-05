import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
import os

def main():
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, '..', 'data', 'processed', 'all_lines_labelled.csv')
    output_file = os.path.join(script_dir, '..', 'data', 'tf-idf', 'top10_tfidf_all_lines.csv')
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Load data
    print(f"Loading data from {input_file}...")
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: File not found at {input_file}")
        return
    
    # Check columns
    if 'text' not in df.columns or 'final_label' not in df.columns:
        print("Error: Input CSV must contain 'text' and 'final_label' columns.")
        return

    # Group by label and combine text
    # We treat all text for a given label as one document
    grouped = df.groupby('final_label')['text'].apply(lambda x: ' '.join(x.astype(str))).reset_index()
    
    labels = grouped['final_label'].tolist()
    corpus = grouped['text'].tolist()
    
    # Compute TF-IDF
    # using 'english' stop words to remove common words
    stop_words = list(ENGLISH_STOP_WORDS) + ['like', 'just', 'don', 'know', 'pedal']
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    tfidf_matrix = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names_out()
    
    results = []
    
    print("\nTop 10 TF-IDF words per label:")
    print("-" * 30)

    # Iterate over each label (document)
    for i, label in enumerate(labels):
        # Get the row for this label
        row = tfidf_matrix[i]
        # Convert to dense array to iterate
        # (row is 1 x n_features sparse matrix)
        dense_row = row.toarray().flatten()
        
        # Get indices of top 10 scores
        # argsort sorts in ascending order, so we take the last 10 and reverse
        top_indices = dense_row.argsort()[-10:][::-1]
        
        top_words = []
        for idx in top_indices:
            word = feature_names[idx]
            score = dense_row[idx]
            top_words.append((word, score))
            
        # Print to console
        print(f"Label: {label}")
        words_str = ", ".join([f"{w} ({s:.4f})" for w, s in top_words])
        print(f"  {words_str}\n")
        
        # Store for CSV
        for rank, (word, score) in enumerate(top_words, 1):
            results.append({
                'label': label,
                'rank': rank,
                'word': word,
                'tfidf_score': score
            })

    # Save to CSV
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()
