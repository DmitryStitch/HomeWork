import time
import multiprocessing

def read_info(name):

    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line.strip())
            line = file.readline()
    return all_data

if __name__ == '__main__':
    filenames = [f'file_{number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Линейный вызов: {elapsed_time}")

    # Многопроцессный вызов
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Многопроцессный вызов: {elapsed_time}")