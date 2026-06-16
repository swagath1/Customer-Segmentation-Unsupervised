# 🛍️ Customer Segmentation using Unsupervised Learning

> Segmenting customers based on purchasing behaviour using Machine Learning to help businesses make data-driven marketing decisions.

### 🌐 Live Demo

🚀 https://customer-segmentation-unsupervised-65jcixprsn4s43rqsfacps.streamlit.app/

## 📌 Project Overview

Customer segmentation is the process of dividing customers into groups with similar characteristics and behaviour.

In this project, I used **Unsupervised Learning** techniques to identify distinct customer groups based on:

- Purchase Price
- Time Spent on Platform
- Session Length
- Interaction Count
- User Actions
- Product Category
- Brand Preference
- Device Type
- Region
- Traffic Source

The discovered segments can help businesses:

✅ Identify loyal customers  
✅ Target high-value customers  
✅ Improve customer retention  
✅ Design personalized marketing campaigns  

---

## 🛠️ Technologies Used

| Category | Tools |
|----------|------|
| Language | Python |
| Data Manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-Learn |
| Clustering | K-Means, Hierarchical Clustering |
| Dimensionality Reduction | PCA |
| Deployment | Streamlit |
| Version Control | Git & GitHub |

---

## 📂 Project Workflow

```text
Raw Data
   ↓
Data Cleaning
   ↓
One Hot Encoding
   ↓
Feature Scaling
   ↓
PCA
   ↓
K-Means Clustering
   ↓
Cluster Analysis
   ↓
Business Insights
   ↓
Streamlit Deployment
```

---

## 📊 Algorithms Used

### 🔹 K-Means Clustering

- Used Elbow Method to determine optimal number of clusters.
- Final model trained with **5 clusters**.
- Assigned each customer to the nearest cluster centroid.

---

### 🔹 Hierarchical Clustering

- Used Agglomerative Clustering.
- Visualized customer groups using Dendrogram.
- Compared with K-Means clustering.

---

### 🔹 PCA (Principal Component Analysis)

Used PCA for:

- Dimensionality Reduction
- Noise Reduction
- Visualization of customer clusters in 2D space

---

## 📈 Features Used

### Numerical Features

- Price
- Time Spent (sec)
- Session Length
- Interaction Count
- Day
- Hour
- Minute

### Categorical Features

- User Action
- Category
- Brand
- Channel
- Device Type
- Region
- Traffic Source

---

## 📷 Visualizations

The project includes:

✅ Elbow Curve

✅ Dendrogram

✅ PCA Explained Variance

✅ Customer Cluster Visualization

---

## 🤖 Saved Models

The following files are saved using Pickle:

```text
kmeans.pkl
scaler.pkl
pca.pkl
train_columns1.pkl
```

---

## 🌐 Streamlit App

The Streamlit app allows users to:

- Enter customer details
- Predict the customer segment
- Get business recommendations based on the predicted cluster

---

## 💡 Business Insights

The identified clusters can represent:

| Cluster | Possible Customer Type |
|--------|------------------------|
| 0 | Casual Visitors |
| 1 | Loyal Customers |
| 2 | High Value Customers |
| 3 | Core Customers |
| 4 | Price Sensitive Customers |

---

## 🚀 Future Improvements

- Deploy on Streamlit Cloud
- Add interactive dashboards
- Compare DBSCAN clustering
- Integrate Power BI dashboard
- Add customer retention analysis

---

## 👨‍💻 Author

**Swagath**

Machine Learning | Data Science | Data Analytics

---

⭐ If you like this project, consider giving it a star!
