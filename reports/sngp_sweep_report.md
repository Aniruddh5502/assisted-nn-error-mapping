# Comprehensive Sweep Analysis Report

## 1. Dataset Overview & Statistics
This section provides a statistical summary of the collected sweep data.

|       |   lipschitz |   mean_rmse |   mean_spearman |   mean_ratio |   val_mean_rmse |   val_mean_spearman |   val_mean_ratio |
|:------|------------:|------------:|----------------:|-------------:|----------------:|--------------------:|-----------------:|
| count |     6       |  6          |       6         |     6        |      6          |           6         |         6        |
| mean  |     2.58333 |  0.0139531  |       0.217295  |     1.21066  |      0.0105245  |           0.195961  |         0.919566 |
| std   |     1.74404 |  0.00751654 |       0.0426608 |     0.858189 |      0.00548818 |           0.0460428 |         0.617172 |
| min   |     0.5     |  0.00847462 |       0.143212  |     0.653616 |      0.0063751  |           0.127639  |         0.510362 |
| 25%   |     1.25    |  0.0103842  |       0.201351  |     0.676378 |      0.00790376 |           0.169558  |         0.587598 |
| 50%   |     2.5     |  0.0108619  |       0.232806  |     0.834879 |      0.00861731 |           0.207451  |         0.643744 |
| 75%   |     3.75    |  0.0136189  |       0.240685  |     1.30185  |      0.0100069  |           0.216265  |         0.927755 |
| max   |     5       |  0.0287575  |       0.26077   |     2.85951  |      0.0214015  |           0.257094  |         2.12824  |

## 2. Detailed Sweep Results
The following table presents the exact metrics recorded for each Lipschitz constant value.

|   lipschitz |   mean_rmse |   mean_spearman |   mean_ratio |   val_mean_rmse |   val_mean_spearman |   val_mean_ratio |
|------------:|------------:|----------------:|-------------:|----------------:|--------------------:|-----------------:|
|      0.5000 |      0.0288 |          0.2410 |       2.8595 |          0.0214 |              0.2178 |           2.1282 |
|      1.0000 |      0.0145 |          0.2396 |       1.4187 |          0.0103 |              0.2116 |           1.0059 |
|      2.0000 |      0.0108 |          0.2608 |       0.9514 |          0.0078 |              0.2571 |           0.6934 |
|      3.0000 |      0.0085 |          0.1931 |       0.6624 |          0.0064 |              0.2033 |           0.5104 |
|      4.0000 |      0.0102 |          0.2260 |       0.7184 |          0.0081 |              0.1583 |           0.5854 |
|      5.0000 |      0.0109 |          0.1432 |       0.6536 |          0.0091 |              0.1276 |           0.5941 |

## 3. Metric Definitions
To interpret the results above, note the following mappings:
- **Lipschitz ($L$)**: The spectral normalization constraint applied to the model backbone.
- **RMSE**: Root Mean Squared Error (lower is better).
- **Spearman $\rho$**: Monotonic correlation between absolute error and predicted variance (higher is better).
- **Ratio**: The relationship between RMSE and standard deviation (closer to 1.0 indicates better calibration).

## 4. Data Integrity Audit
- **Total Rows Processed**: 6
- **Null Values Detected**: 0
- **Data Loss during analysis**: 0.0%
