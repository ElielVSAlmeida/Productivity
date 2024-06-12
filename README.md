# Welcome to Productivity Analysis!

This project aims to show a sample of my abilities with machine learning and neural networks (AI) using **SKLearn** and **TensorFlow**, **OS** and **Dotenv** were used for operation optimization. The goal is to:
- Create a **Algorithmic Machine Learning Model** that is based on easily accessible business features.
- Build an in-depth **Data Analysis** with Interactive Graphs using **Tableau** to further the investigation of what drives productivity.
- Format a **Data Base** where data can be stored, organized, related, secured and distributed using **SQL** and frameworks as **SQLAlchemy** and **MySLQConnector**.

The data was cleaned and formatted with **Pandas**, also **Matplotlib** and **Seaborn** were used for visualization. **Flask** along with a bit of HTML was used to build the website, for deployment **GUnicorn** and **Render** was chosen. To interact with the dashboard and use the ML Algorithm to make a prediction use this website [LINK](https://productivity-study.onrender.com).

# Data Sources

![alt text](https://github.com/ElielVSAlmeida/Productivity/blob/main/vizualization/about_data.png)

# Analysis

The features describe poorly the target, meaning that yielding a high accuracy on the prediction would be almost impossible, and also leading easily to overfitted models.

![alt text](https://github.com/ElielVSAlmeida/Productivity/blob/main/vizualization/analysis.png)

# Obstacles

So I setted ranges for the model, transforming the target, therefore the model has only to predict the level (low, medium, high and very high) of the productivity, then with that prediction it will find the productivity percentages.

![alt text](https://github.com/ElielVSAlmeida/Productivity/blob/main/vizualization/values.png)

# Conclusion

Despite the obstacles, the model performed better than the benchmark, and it is pretty reliable to its intended use. See [Benchmark](https://github.com/dynasty-29/Productivity-Prediction-Project/blob/main/productivity_prediction_final.ipynb).

![alt text](https://github.com/ElielVSAlmeida/Productivity/blob/main/vizualization/conclusion.png)
