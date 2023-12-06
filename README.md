# Salary_Prediction_Selenium



Description
This project utilizes Selenium for web scraping on Glassdoor to extract job-related data such as job title, salary information, and location. The scraped data is then used to train an XGBoost Regressor model that predicts salary based on job title, location, and the seniority of the role. The trained model is deployed on Streamlit, providing a user-friendly interface for salary predictions.



Run the web scraping script:

python datacollection/selenium_scraping.py
This script uses Selenium to scrape job-related data from Glassdoor.

Train the XGBoost Regressor model:
train_model.py
This script processes the scraped data and trains the predictive model.

Deploy the model on Streamlit:

streamlit run inference_app.py
Open the provided URL to access the Streamlit app and make salary predictions.

Project Structure
scrape_glassdoor.py: Python script for web scraping using Selenium on Glassdoor.
train_model.py: Script to preprocess scraped data and train the XGBoost Regressor model.
app.py: Streamlit application for deploying and interacting with the trained model.
requirements.txt: List of Python dependencies.

Dependencies
Selenium
XGBoost
Streamlit
