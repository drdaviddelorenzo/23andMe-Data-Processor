def query_snp_rsID(filename, rsID_query):
    """
    Searches the given 23andMe raw data file for the specified SNP rsID and prints the genotype.
    """
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('#'):
                parts = line.strip().split('\t')
                rsid, chromosome, position, genotype = parts
                if rsid == rsID_query:
                    print(f"Genotype for {rsid}: {genotype}")
                    return
    print("SNP rsID not found.")

def read_23andme_file(filename):
    """
    Reads the 23andMe raw data file and prints all SNP rsIDs and their genotypes.
    """
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('#'):
                parts = line.strip().split('\t')
                rsid, chromosome, position, genotype = parts
                print(f"{rsid}: {genotype}")

if __name__ == "__main__":
    filepath = input("Enter the path to your 23andMe raw data file: ")
    # Ask the user if they want to query a specific SNP rsID
    query = input("Do you want to query a specific SNP rsID? (yes/no): ").lower()
    if query == 'yes':
        rsID_query = input("Enter the SNP rsID to query: ")
        query_snp_rsID(filepath, rsID_query)
    else:
        read_23andme_file(filepath)
