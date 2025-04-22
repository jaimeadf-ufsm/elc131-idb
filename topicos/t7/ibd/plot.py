import matplotlib.pyplot as plt
import numpy as np

def read_data(filename):
    frequent_reads = []
    lru_misses = []
    layered_lru_misses = []

    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 3:
                frequent_reads.append(float(parts[0]))
                lru_misses.append(int(parts[1]))
                layered_lru_misses.append(int(parts[2]))

    return np.array(frequent_reads), np.array(lru_misses), np.array(layered_lru_misses)

def plot_data(frequent_reads, lru_misses, layered_lru_misses):
    plt.figure(figsize=(10, 6))
    plt.plot(frequent_reads, lru_misses, label='Cache LRU', marker='o', linestyle='--')
    plt.plot(frequent_reads, layered_lru_misses, label='Cache Layered LRU', marker='s', linestyle='--')

    plt.xlabel('Probabilidade de Leituras Frequentes')
    plt.ylabel('Número de Page Misses')
    plt.title('Número de Page Misses vs Probabilidade de Leituras Frequentes')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    filename = "data.txt"  # Change this to your actual file name
    frequent_reads, lru_misses, layered_lru_misses = read_data(filename)
    plot_data(frequent_reads, lru_misses, layered_lru_misses)
