import csv

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
    query = input("Do you want to query a specific SNP rsID or a CSV file of rsIDs? (rsID/csv): ").lower()
    if query == 'rsid':
        rsID_query = input("Enter the SNP rsID to query: ")
        query_snp_rsID(filepath, rsID_query)
    elif query == 'csv':
        csv_query_file = input("Enter the path to your CSV file with SNP rsIDs: ")
        output_csv_file = input("Enter the path for the output CSV file with genotypes: ")
        query_snps_from_csv(filepath, csv_query_file, output_csv_file)

if __name__ == "__main__":
    main()