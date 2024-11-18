"""Main module."""
import pandas as pd
import os
import sys

def combine_tsv_make_csv(tsv_folder_path, output_csv_file):
    # Check if the input folder exists
    if not os.path.exists(tsv_folder_path):
        print(f"Error: The folder '{tsv_folder_path}' does not exist.")
        sys.exit(1)  # Exit if folder doesn't exist
    
    # Get all .tsv files in the directory
    tsv_files = [f for f in os.listdir(tsv_folder_path) if f.endswith('target_psms.tsv')]
    print(f"Found the following .tsv files: {tsv_files}")

    if not tsv_files:
        print(f"Error: No files ending in target_psms.tsv found in '{tsv_folder_path}'.")
        sys.exit(1)  # Exit if no relevant files are found

    combined_df = pd.DataFrame()

    # Loop through each .tsv file and combine them
    for tsv_file in tsv_files:
        tsv_file_path = os.path.join(tsv_folder_path, tsv_file)
        
        # Check if the .tsv file exists
        if not os.path.isfile(tsv_file_path):
            print(f"Error: The file '{tsv_file_path}' does not exist.")
            sys.exit(1)  # Exit if file doesn't exist

        try:
            # Read the TSV file into a DataFrame
            df = pd.read_csv(tsv_file_path, sep='\t')
            combined_df = pd.concat([combined_df, df], ignore_index=True)
            print(f"After adding {tsv_file}, combined_df shape is: {combined_df.shape}")
        except Exception as e:
            print(f"Error occurred while reading the file '{tsv_file_path}': {e}")
            sys.exit(1)  # Exit on read failure

    # Print the final shape of the combined DataFrame
    print(f"Final combined_df shape: {combined_df.shape}")
    print(f"Successfully combined {len(tsv_files)} .tsv files into combined_df.")
    
    # Try writing the final combined dataframe to CSV
    try:
        combined_df.to_csv(output_csv_file, index=False)
        print(f"Temporary dataframe has been written to {output_csv_file}")
    except Exception as e:
        print(f"Error occurred while writing the CSV file '{output_csv_file}': {e}")
        sys.exit(1)  # Exit on write failure

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python combine_tsv_make_csv.py <tsv_folder_path> <output_csv_file>")
        sys.exit(1)
    
    tsv_folder_path = sys.argv[1]
    output_csv_file = sys.argv[2]
    
    combine_tsv_make_csv(tsv_folder_path, output_csv_file)