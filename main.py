import random
import time
import imageio.v2 as imageio  # Import imageio for image processing
import matplotlib.pyplot as plt
from scipy.ndimage import median_filter
import os
import pandas as pd

def randomized_quickselect(arr, k):
    """Find the k-th smallest element in an unordered list using randomized selection."""
    left, right = 0, len(arr) - 1
    while left <= right:
        pivot_index = random.randint(left, right)
        pivot_index = partition(arr, left, right, pivot_index)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            left = pivot_index + 1
        else:
            right = pivot_index - 1

def partition(arr, left, right, pivot_index):
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]  # Move pivot to the end
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    arr[store_index], arr[right] = arr[right], arr[store_index]  # Move pivot to its final place
    return store_index

def experiment(N, n):
    """Perform the experiment for given N and n, and return the average time taken."""
    times = []
    for _ in range(5):
        random_numbers = random.sample(range(1, N + 1), n)
        i = random.randint(1, n)
        start_time = time.time()
        ith_smallest = randomized_quickselect(random_numbers, i-1)
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / len(times)

def apply_median_filter(image_path, filter_size):
    """Apply median filter to the image and return the filtered image."""
    image = imageio.imread(image_path)  # Read PGM image
    filtered_image = median_filter(image, size=(filter_size, filter_size))
    return filtered_image

def save_filtered_image(original_path, filtered_image):
    """Save the filtered image with a name similar to the original file."""
    base_name, ext = os.path.splitext(original_path)
    new_name = f"{base_name}_filtered{ext}"
    imageio.imwrite(new_name, filtered_image)

def process_images(image_paths, filter_size):
    """Process multiple images by applying median filter and saving them."""
    for image_path in image_paths:
        filtered_image = apply_median_filter(image_path, filter_size)
        if filtered_image is not None:
            save_filtered_image(image_path, filtered_image)

def main():
    # Part I: Order Statistic Algorithm
    population_sizes = [5000, 8000, 10000]
    sample_sizes = [100, 300, 500, 1000, 2000, 4000]
    results = []

    for N in population_sizes:
        for n in sample_sizes:
            avg_time = experiment(N, n)
            results.append((N, n, avg_time))

    # Convert results to DataFrame
    df = pd.DataFrame(results, columns=['Population Size (N)', 'Sample Size (n)', 'Average Time (seconds)'])

    print("Results from Part I: Order Statistic Algorithm")
    print(df.to_string(index=False))

    # Plotting the results
    fig, ax = plt.subplots(figsize=(10, 6))
    for N in population_sizes:
        subset = df[df['Population Size (N)'] == N]
        ax.plot(subset['Sample Size (n)'], subset['Average Time (seconds)'], marker='o', label=f'N={N}')

    ax.set_title('Running Time of the Algorithm for Various Combinations of n and N')
    ax.set_xlabel('Sample Size (n)')
    ax.set_ylabel('Average Time (seconds)')
    ax.legend()
    plt.grid(True)

    # Save plot as an image file
    plt.savefig('running_time_plot.png')

    # Part II: Median Filtering of Multiple Images
    image_paths = [
        'image1.pgm', 'image2.pgm', 'image3.pgm', 'image4.pgm', 'image5.pgm',
        'image6.pgm', 'image7.pgm', 'image8.pgm', 'image9.pgm', 'image10.pgm',
        'image11.pgm', 'image12.pgm', 'image13.pgm', 'image14.pgm', 'image15.pgm',
        'image16.pgm', 'image17.pgm', 'image18.pgm', 'image19.pgm', 'image20.pgm'
    ]  # List of PGM image file paths

    filter_size = 3

    process_images(image_paths, filter_size)

if __name__ == "__main__":
    main()
