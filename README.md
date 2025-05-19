# 🏋️ Predict Calorie Expenditure  
**Kaggle Playground Series - Season 5, Episode 5**

This repository contains my solution for the Kaggle competition **"Playground Series - S5E5"**.  
The goal is to predict how many calories were burned during a workout session.

---

## 📝 Objective

Predict the number of **Calories** burned for each row in the test set.

### 🔢 Submission Format

The submission must be a CSV file with two columns: `id` and `Calories`. Example:

id,Calories
750000,93.2
750001,27.42
750002,103.8
...


---

## 📊 Evaluation Metric

The competition uses **Root Mean Squared Logarithmic Error (RMSLE)** as the evaluation metric:

\[
\text{RMSLE} = \sqrt{ \frac{1}{n} \sum_{i=1}^{n} \left( \log(1 + \hat{y}_i) - \log(1 + y_i) \right)^2 }
\]

Where:  
- \( \hat{y}_i \) is the predicted value  
- \( y_i \) is the true value  
- \( n \) is the number of samples

This metric penalizes under-predictions more than over-predictions for small values, and is less sensitive to large absolute errors when the target values are large.

---

## 📅 Timeline

- **Competition start**: May 1, 2025
- **Project Kickoff  | Initial exploration started**: May 19, 2025
- **Final submission deadline**: May 31, 2025 (11:59 PM UTC)

---

## ℹ️ Notes

- The dataset is **synthetically generated** but inspired by real-world data.  
- The competition is part of the **Kaggle Tabular Playground Series**, intended for learning and ex
