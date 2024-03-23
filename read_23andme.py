def read_23andme_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('#'):
                parts = line.strip().split('\t')
                # Assuming the file has four parts: rsid, chromosome, position, genotype
                rsid, chromosome, position, genotype = parts
                print(f"{rsid}: {genotype}")

if __name__ == "__main__":
    filepath = input("Enter the path to your 23andMe raw data file: ")
    read_23andme_file(filepath)
