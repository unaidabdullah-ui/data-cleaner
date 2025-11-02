import pandas as pd
import argparse

def clean_data(input_file, output_file):
    df = pd.read_csv(input_file)
    original_rows = len(df)
    cleaned_df = df.dropna()
    cleaned_rows = len(cleaned_df)

    cleaned_df.to_csv(output_file, index=False)
    print(f"✅ Cleaned data saved to {output_file}")
    print(f"🧾 Rows before: {original_rows}, after: {cleaned_rows}, removed: {original_rows - cleaned_rows}")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Data Cleaner Tool")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument("--output", required=True, help="Path to save cleaned CSV")
    args = parser.parse_args()

    clean_data(args.input, args.output)

