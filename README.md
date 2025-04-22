# House Price Prediction App

## Project Overview
This project is a machine learning-based web application that predicts house prices using various property features. Built with Streamlit, it provides an interactive interface for users to input property details and receive instant price predictions.

## Features
- **Interactive Input Form**: User-friendly interface with organized feature categories
  - Basic Information (lot area, year built, quality ratings)
  - Exterior Features (house style, roof type, exterior materials)
  - Interior Features (basement, bathrooms, kitchen, heating)
  - Garage & Additional Features (garage details, porches, pool)

- **Real-time Prediction**: Instant price predictions based on user inputs
- **Comprehensive Feature Set**: Over 40 different property features considered
- **Organized Interface**: Features grouped into logical categories for easy input
- **Responsive Design**: Works seamlessly on both desktop and mobile devices

## Technical Details
### Data
- **Dataset**: Ames Housing Dataset
- **Features**: 43 different property characteristics
- **Data Preprocessing**:
  - One-hot encoding for categorical variables
  - Handling of missing values
  - Feature alignment between training and test sets

### Model
- **Algorithm**: Random Forest Regressor
- **Training**: Trained on historical housing data
- **Features Used**: All 43 property characteristics
- **Model Storage**: Serialized using pickle for easy deployment

### Technology Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Libraries**:
  - pandas: Data manipulation
  - numpy: Numerical computations
  - scikit-learn: Machine learning model
  - streamlit: Web interface

## Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/House-Price-Prediction.git
cd House-Price-Prediction
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Run the application locally:
```bash
streamlit run StreamlitPart.py
```

2. Access the application through your web browser at `http://localhost:8501`

3. Fill in the property details in the interactive form

4. Click "Predict House Price" to get the estimated value

## Project Structure
```
House-Price-Prediction/
├── StreamlitPart.py      # Main application file
├── requirements.txt      # Project dependencies
├── README.md            # Project documentation
├── .gitignore           # Git ignore file
├── train.csv            # Training dataset
├── test.csv             # Test dataset
└── random_forest_model.pkl  # Trained model
```

## Data Features
The model considers various property characteristics including:
- Lot size and configuration
- Building quality and condition
- Number of rooms and bathrooms
- Heating and cooling systems
- Garage details
- Porch and deck areas
- Sale conditions

## Model Performance
The Random Forest model was chosen for its ability to:
- Handle both numerical and categorical features
- Capture non-linear relationships
- Provide robust predictions
- Handle missing values effectively

## Deployment
The application is deployed on Streamlit Community Cloud, making it accessible worldwide. The deployment process includes:
1. Code pushed to GitHub repository
2. Automatic deployment through Streamlit Community Cloud
3. Continuous updates with new commits

## Future Improvements
- Add historical price trends
- Include property images
- Provide confidence intervals for predictions
- Add feature importance visualization
- Implement user feedback system

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or suggestions, please open an issue in the GitHub repository. 