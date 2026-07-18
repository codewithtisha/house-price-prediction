# House Price Prediction

A machine learning web application that predicts house prices based on property features using a Linear Regression model. Built with Flask and deployed on Render.

## Live Demo

https://house-price-prediction-jxks.onrender.com/

## Features

- Real-time house price prediction
- Responsive and modern user interface
- Machine learning model integration
- Input validation
- Instant prediction results

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- NumPy
- Pandas
- Scikit-learn
- Pickle

## Machine Learning Model

- Algorithm: Linear Regression
- Evaluation Metric: R² Score
- Model trained using Scikit-learn

## Dataset

**House Prices India Dataset**

Source: https://www.kaggle.com/datasets/sukhmandeepsinghbrar/house-prices-india

## Project Structure

```
house-price-prediction/
│
├── app.py
├── house_price_model.pkl
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
```

## Run Locally

```bash
git clone https://github.com/codewithtisha/house-price-prediction.git
cd house-price-prediction
pip install -r requirements.txt
python app.py
```

Then open:

```
http://127.0.0.1:5000
```


