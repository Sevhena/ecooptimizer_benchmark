# Code Smell Benchmark Report

## 1. Code Smell Overview

The following table presents the number of code smells detected across selected repositories, grouped by domain. Each column represents a specific smell type.

| Domain       | Repository   | Long Element Chain | Long Lambda Expr | Long Message Chain | No Self Use | String Concat Loop | Too Many Arguments | Use a Generator | **Total Smells** |
| ------------ | ------------ | ------------------ | ---------------- | ------------------ | ----------- | ------------------ | ------------------ | --------------- | ---------------- |
| Data Science | scipy        | 13                 | 1                | 20                 | 248         | 3                  | 576                | 7               | **868**          |
|              | numpy        | 0                  | 1                | 7                  | 50          | 5                  | 116                | 0               | **179**          |
|              | nltk         | 20                 | 14               | 3                  | 234         | 3                  | 104                | 0               | **378**          |
| Web          | streamlit    | 1                  | 3                | 4                  | 44          | 0                  | 71                 | 0               | **123**          |
|              | django       | 7                  | 0                | 27                 | 415         | 9                  | 127                | 2               | **587**          |
| ML           | scikit-learn | 4                  | 0                | 8                  | 28          | 5                  | 199                | 1               | **245**          |
| Utility      | dask         | 4                  | 0                | 11                 | 24          | 4                  | 126                | 4               | **173**          |
| Embedded/IOT | paho.mqtt    | 0                  | 0                | 3                  | 3           | 1                  | 9                  | 0               | **16**           |
|              | gpiozero     | 0                  | 1                | 2                  | 15          | 0                  | 24                 | 0               | **42**           |

---

## 2. Selected Instances for Each Smell Type

For benchmarking, we choose **one instance of each smell per domain**. If a domain has no valid instance, we substitute with an additional one from another domain. The following table lists the selected repositories and corresponding file locations per smell type.

> **Note:** The file paths are relative to the respective repositories and the IDs can be referenced in the `artifacts/smells/raw`directory of the replication package.

| Smell Type                 | Domain       | Repository       | File Path / Identifier |
| -------------------------- | ------------ | ---------------- | ---------------------- |
| **Long Lambda Expression** | Data Science | nltk             | `13d438e9`             |
|                            | Data Science | scipy            | `e0748c3e`             |
|                            | Data Science | numpy            | `b89c2eb1`             |
|                            | Web          | streamlit        | `3dff6d86`             |
|                            | Embedded/IOT | gpiozero         | `e04be5d7`             |
| **Long Message Chain**     | Data Science | scipy            | `f7d9627c`             |
|                            | Web          | django           | `dfadbb34`             |
|                            | ML           | scikit-learn     | `5f1cf174`             |
|                            | Utility      | dask             | `8da83e08`             |
|                            | Embedded/IOT | paho.mqtt.python | `89b86924`             |
| **No Self Use**            | Data Science | nltk             | `dc979356`             |
|                            | Web          | django           | `f0dffe2e`             |
|                            | ML           | scikit-learn     | `db63474a`             |
|                            | Utility      | dask             | `81ec5021`             |
|                            | Embedded/IOT | gpiozero         | `fc7e33d2`             |
| **String Concat in Loop**  | Data Science | numpy            | `050c312a`             |
|                            | Web          | django           | `871b0de2`             |
|                            | ML           | scikit-learn     | `de2a415f`             |
|                            | Utility      | dask             | `5254055f`             |
|                            | Embedded/IOT | paho.mqtt.python | `cbf43c4b`             |
| **Too Many Arguments**     | Data Science | scipy            | `83d99ed0`             |
|                            | Web          | streamlit        | `f5d06531`             |
|                            | ML           | scikit-learn     | `809dea56`             |
|                            | Utility      | dask             | `4e24e944`             |
|                            | Embedded/IOT | gpiozero         | `e50ab4c5`             |
| **Use a Generator**        | Data Science | scipy            | `c0a0307d`             |
|                            | Data Science | scipy *(extra)*  | `2bbdf916`             |
|                            | Web          | django           | `cf18c1e1`             |
|                            | ML           | scikit-learn     | `bebfc193`             |
|                            | Utility      | dask             | `0fa92701`             |

---

## 3. Emissions and Resource Benchmark Results

For each smell type, the benchmark measurements below show the **mean and standard deviation** for:

* Carbon emissions (in gCO₂eq)
* CPU usage (in %)
* RAM usage (in MB)

| Smell Type         | Carbon Mean | Carbon Stdev | CPU Mean | CPU Stdev | RAM Mean | RAM Stdev |
| ------------------ | ----------- | ------------ | -------- | --------- | -------- | --------- |
| Long Element Chain | TBD         | TBD          | TBD      | TBD       | TBD      | TBD       |
| Long Lambda Expr   | TBD         | TBD          | TBD      | TBD       | TBD      | TBD       |
| Long Message Chain | TBD         | TBD          | TBD      | TBD       | TBD      | TBD       |
| No Self Use        | TBD         | TBD          | TBD      | TBD       | TBD      | TBD       |
| String Concat Loop | TBD         | TBD          | TBD      | TBD       | TBD      | TBD       |
| Too Many Arguments | TBD         | TBD          | TBD      | TBD       | TBD      | TBD       |
| Use a Generator    | TBD         | TBD          | TBD      | TBD       | TBD      | TBD       |
