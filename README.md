# **Median Image Filtering Using Order Statistics**

## **Introduction:**

This project implements median image filtering using order statistics to enhance digital image quality. The method reduces noise while preserving critical image details such as edges and textures. Additionally, the project includes performance analysis of an order statistic algorithm.


## **Features:**
- Noise Reduction:
  - Applies median filtering to effectively reduce visual noise in images.
- Performance Analysis:
  - Includes scripts to measure and analyze the algorithm's performance with different sample sizes and data points.
- Visual Comparisons:
  - Provides before-and-after image comparisons to demonstrate the filtering effects.
 
## **Technologies Used:**
- Python: Core programming language for the project.
- NumPy: For efficient numerical operations.
- Matplotlib: For generating performance graphs.
- SciPy: For image processing tasks, specifically median filtering.
- Pandas: For handling and analyzing performance data.
- Imageio: For reading and writing image files.

## **Getting Started:**

### **Prerequisites:**
- Python 3.8 or higher
- NumPy
- Matplotlib
- SciPy
- Pandas
- Imageio



## **Installation:**

Clone the repository and install the required packages:

```
git clone https://github.com/yourusername/median-image-filtering.git

cd median-image-filtering

pip install numpy matplotlib scipy pandas imageio
```

## **Usage:**
To run the image filtering and performance analysis script:

`python main.py `

## **Performance Analysis:**
The performance of the algorithm is analyzed based on various sample sizes and total data points.
The graph below illustrates the running time for different combinations of n (sample size) and N (total data points):
![running_time_plot](https://github.com/lindseyveneziano/Order-Statistics/assets/123207895/aa657e13-2493-4234-862c-c782dea18601)

## **Author:**
- **Lindsey Veneziano** - [GitHub Profile](https://github.com/lindseyveneziano)
