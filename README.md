![alt text](https://github.com/ElielVSAlmeida/Productivity/blob/main/vizualization/backgroundedit.jpg)

![GitHub Created At](https://img.shields.io/github/created-at/ElielVSAlmeida/Productivity)
![Static Badge](https://img.shields.io/badge/Python-3776AB?style=plastic&logo=python&logoColor=%23FFD343)
![Static Badge](https://img.shields.io/badge/SciKit-1c7AE8?style=plastic&logo=scikitlearn&logoColor=%23F7931E)
![Static Badge](https://img.shields.io/badge/Flask-FFFFFF?style=plastic&logo=flask&logoColor=%23000000)
![Static Badge](https://img.shields.io/badge/DotEnv-000000?style=plastic&logo=dotenv)
![Static Badge](https://img.shields.io/badge/Tableau-blue?style=plastic&logo=tableau&logoColor=FFFFFF)
![Static Badge](https://img.shields.io/badge/MySQL-4479A1?style=plastic&logo=mysql&logoColor=FFFFFF)
![Static Badge](https://img.shields.io/badge/Pandas-150458?style=plastic&logo=pandas&logoColor=FFFFFF)


# Welcome to Productivity Analysis!

This dataset includes important attributes of the garment manufacturing process and the productivity of the employees which had been collected manually and also been validated by the industry experts. 

Defining the metrics is essential, what productivity means here is: To tell you how *efficiently* and *effectively* your workforce is delivering results over a set period. Therefore having *Total Output* divided by *Total Input* we can find *Productivity*, since it is a garment manufacturing company we can assume that is quantity per hour divided by the total cost per hour.

This project aims to show a sample of my abilities with machine learning and neural networks (AI) using **SKLearn** and **TensorFlow**, **OS** and **Dotenv** were used for operation optimization. The goal is to:
- Create a **Algorithmic Machine Learning Model** that is based on easily accessible business features.
- Build an in-depth **Data Analysis** with Interactive Graphs using **Tableau** to further the investigation of what drives productivity.
- Format a **Data Base** where data can be stored, organized, related, secured and distributed using **SQL** and frameworks as **SQLAlchemy** and **MySLQConnector**.

The data was cleaned and formatted with **Pandas**, also **Matplotlib** and **Seaborn** were used for visualization. **Flask** along with a bit of HTML was used to build the website, for deployment **GUnicorn** and **Render** was chosen. To interact with the dashboard and use the ML Algorithm to make a prediction use this [website link](https://productivity-study.onrender.com).

# Data Sources

This data was a obtained in the [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/dataset/597/productivity+prediction+of+garment+employees), and there is a article published in [International Journal of Business Intelligence and Data Mining](https://dl.acm.org/doi/abs/10.1504/ijbidm.2021.118183) on the mining process.

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
