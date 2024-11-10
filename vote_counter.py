import csv

def count_votes(file_path):
    results = {}
    
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # Skip the header

        for row in reader:
            city = row[0]
            candidate = row[1]
            try:
            	votes = int(row[2])
            except:
                votes = 0
            
            if candidate in results:
                results[candidate] += votes
            else:
                results[candidate] = votes

    for candidate, total_votes in results.items():
        print(f"{candidate}: {total_votes} votes")

# Example usage
count_votes('votes.csv')
