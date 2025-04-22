import matplotlib.pyplot as plt
import numpy as np

def plot_data(file_path):
    data = {}

    # Read and parse the file
    with open(file_path, 'r') as file:
        for line in file:
            split_factor, sorted_size, shuffled_size, blocks_written, blocks_count = map(float, line.split())
            key = (int(sorted_size), int(shuffled_size))
            if key not in data:
                data[key] = {'split_factors': [], 'blocks_written': [], 'blocks_count': []}
            data[key]['split_factors'].append(split_factor)
            data[key]['blocks_written'].append(blocks_written)
            data[key]['blocks_count'].append(blocks_count)

    # Plot Blocks Written
    plt.figure(figsize=(10, 5))
    for key, values in data.items():
        plt.plot(values['split_factors'], values['blocks_written'], marker='o', label=str(key))
    plt.xlabel('Split Factor')
    plt.ylabel('Blocos Escritos')
    plt.title('Blocos Escritos vs Split Factor')
    plt.legend(title='(Tamanho Ordenado, Tamanho Aleatório)')
    plt.grid()
    plt.show()

    # Plot Blocks Count
    plt.figure(figsize=(10, 5))
    for key, values in data.items():
        plt.plot(values['split_factors'], values['blocks_count'], marker='o', label=str(key))
    plt.xlabel('Split Factor')
    plt.ylabel('Quantidade de Blocos')
    plt.title('Quantidade de Blocos vs Split Factor')
    plt.legend(title='(Tamanho Ordenado, Tamanho Aleatório)')
    plt.grid()
    plt.show()

# Example usage
plot_data('data.txt')  # Replace 'data.txt' with the actual file path
