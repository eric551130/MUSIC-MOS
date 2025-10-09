import csv
import argparse

'''
# CSV file format:
Time, User, Song1, Song2, Song3, ..., Song20
A/A/A, User1, 4, 5, 3, ..., 4
B/B/B, User2, 2, 3, 4, ..., 5

# Each row represents a user's ratings for 20 songs
'''

# Function to calculate the average MOS score of each song from a CSV file
def calculate_average_mos(file_path):
    total_scores = [0] * 20  # Assuming there are 20 songs
    count_scores = [0] * 20

    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for row in reader:
            scores = row[2:22]  # Extract scores for the 20 songs
            for i in range(20):
                total_scores[i] += float(scores[i])
                count_scores[i] += 1

    average_scores = []
    for i in range(20):
        if count_scores[i] > 0:
            average_scores.append(total_scores[i] / count_scores[i])
        else:
            average_scores.append(0)

    # overall_average_mos = sum(average_scores) / len(average_scores)
    # return overall_average_mos
    return average_scores

def MOS_of_models(mos_list):
    # Index mapping based on index.md (0-based indexing)
    CP_index = [2, 5, 10, 15]  # CP/2, CP/4, CP/3, CP/1 at positions 3, 6, 11, 16
    Expert_index = [1, 6, 12, 18]  # Expert/2, Expert/4, Expert/1, Expert/3 at positions 2, 7, 13, 19
    LLaMA_index = [4, 9, 14, 17]  # LLaMA/1, LLaMA/3, LLaMA/2, LLaMA/4 at positions 5, 10, 15, 18
    RL_index = [0, 7, 11, 16]  # RL/4, RL/1, RL/5, RL/2 at positions 1, 8, 12, 17
    RL_Novelty_index = [3, 8, 13, 19]  # RL+Novelty/3, RL+Novelty/1, RL+Novelty/4, RL+Novelty/2 at positions 4, 9, 14, 20
    
    # Calculate average MOS for each model
    CP_mos = sum([mos_list[i] for i in CP_index]) / len(CP_index)
    Expert_mos = sum([mos_list[i] for i in Expert_index]) / len(Expert_index)
    LLaMA_mos = sum([mos_list[i] for i in LLaMA_index]) / len(LLaMA_index)
    RL_mos = sum([mos_list[i] for i in RL_index]) / len(RL_index)
    RL_Novelty_mos = sum([mos_list[i] for i in RL_Novelty_index]) / len(RL_Novelty_index)
    
    return {
        'Expert': Expert_mos,
        'CP': CP_mos,
        'LLaMA': LLaMA_mos,
        'RL': RL_mos,
        'RL+Novelty': RL_Novelty_mos
    }

def main():
    # file_path = "C:/Users/M11102130/Downloads/score1.csv"  # Path to the CSV file
    parser = argparse.ArgumentParser(description="Calculate average MOS from a CSV file.")
    parser.add_argument("--file_path", '-f', type=str, help="Path to the CSV file")
    args = parser.parse_args()
    file_path = args.file_path

    average_mos = calculate_average_mos(file_path)
    print(f"Average MOS for each song: {average_mos}")
    
    model_mos = MOS_of_models(average_mos)
    print(f"\nAverage MOS by model:")
    for model, score in model_mos.items():
        print(f"  {model}: {score:.4f}")

    print(average_mos[7])

if __name__ == "__main__":
    main()