# Flight Fare Prediction
### Importing the required libraries
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

## Training data
- Reading the data
- Checking the shape of dataset
- The dataset is too large and null values values are less than 1% so we can drop them
- Checking for the shape after dropping the null values
#### EDA
- Converting the datetime columns from string format into datetime format
- Creating the duration feature
#### Encoding
- Converting categorical features into numerical values called encoding
- Converting Nominal categorical features into numeric values by using **oneHotEncoding** technique
- Converting Ordinal categorical features into numeric values by using **LabelEncoder** technique
- Dropping un neccessary columns
## Testing data
- All the above steps were repeted for testing data also
## Feature Importance
- Finding the feature importance by using Heatmap and ExtratreeRegressor
## Model Building
- Importing the model from sklearn
- Training the model with training data 
- test the model with test data
- creating pickle file for model
## App
- Creating the app using Streamlit
- Deploying the app
