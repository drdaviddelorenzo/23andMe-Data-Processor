import csv
import os

def query_snp_rsID(filename, rsID_query):
    """
    Searches the given 23andMe raw data file for the specified SNP rsID and prints the genotype.
    """
    found = False
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('#'):
                parts = line.strip().split('\t')
                rsid, chromosome, position, genotype = parts
                if rsid == rsID_query:
                    print(f"Genotype for {rsid}: {genotype}")
                    found = True
                    break
    if not found:
        print("SNP rsID not found.")

def query_snps_from_csv(filename, csv_query_file, output_csv_file):
    """
    Reads SNP rsIDs from a CSV file, queries their genotypes from the 23andMe raw data file,
    and writes the results to another CSV file.
    """
    # Load rsIDs from the CSV query file
    with open(csv_query_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rsid_list = [row[0] for row in reader]

    # Query each rsID in the 23andMe file and store results
    results = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue
            parts = line.strip().split('\t')
            rsid, _, _, genotype = parts
            if rsid in rsid_list:
                results.append((rsid, genotype))

    # Write queried genotypes to the output CSV file
    with open(output_csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['rsID', 'Genotype'])
        writer.writerows(results)

def main():
    filepath = input("Enter the path to your 23andMe raw data file: ")
    query_type = input("Do you want to query a specific SNP rsID or a CSV file of rsIDs? (rsID/csv): ").lower()
    if query_type == 'rsid':
        rsID_query = input("Enter the SNP rsID to query: ")
        query_snp_rsID(filepath, rsID_query)
    elif query_type == 'csv':
        csv_query_file = input("Enter the path to your CSV file with SNP rsIDs: ")
        # Automatically generate the name for the output CSV file
        output_csv_file = os.path.splitext(csv_query_file)[0] + '_genotypes.csv'
        query_snps_from_csv(filepath, csv_query_file, output_csv_file)
        print(f"Output has been written to {output_csv_file}")
    else:
        print("Invalid input. Please enter 'rsID' or 'csv' to proceed.")

if __name__ == "__main__":
    main()