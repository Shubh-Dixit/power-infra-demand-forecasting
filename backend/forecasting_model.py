import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

def run_forecasting():
    print("Loading Clustered Data...")
    df = pd.read_csv('material_demand_data_clustered.csv')
    
    # Inputs
    feature_cols = ['Region', 'Terrain', 'Infrastructure_Type', 'Project_Category', 'Voltage_Level_kV', 'Weather_Condition', 'Route_Length_km']
    # Targets
    target_cols = ['ACSR_Conductor_m', 'Towers_Steel_Count', 'Insulators_Count', 'Power_Transformers_Count', 'Circuit_Breakers_Count', 'Concrete_m3']
    
    X = df[feature_cols]
    y = df[target_cols]
    
    # Preprocessing Pipeline
    categorical_features = ['Region', 'Terrain', 'Infrastructure_Type', 'Project_Category', 'Weather_Condition']
    numerical_features = ['Voltage_Level_kV', 'Route_Length_km']
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', 'passthrough', numerical_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ])
    
    # Model: Multi-Output Random Forest
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', MultiOutputRegressor(RandomForestRegressor(n_estimators=100, random_state=42)))
    ])
    
    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training Intelligent Forecasting Model (Random Forest)...")
    model.fit(X_train, y_train)
    
    # Evaluate
    print("Evaluating Model...")
    y_pred = model.predict(X_test)
    
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    
    print(f"\nModel Performance:")
    print(f"Overall RMSE: {rmse: .2f}")
    print(f"Overall R2 Score: {r2: .2f}")
    
    # Importance of Cluster awareness (Unsupervised Learning contribution)
    # We can perform a check: How well does it predict per Cluster?
    
    print("\nSample Predictions vs Actuals:")
    sample_res = pd.DataFrame(y_pred[:5], columns=target_cols)
    sample_act = y_test.iloc[:5].reset_index(drop=True)
    
    print("Actuals (First 5 test samples):")
    print(sample_act)
    print("\nPredictions (First 5 test samples):")
    print(sample_res.round(2))
    
    # Save Model
    joblib.dump(model, 'demand_forecasting_model.pkl')
    print("\nModel saved to 'demand_forecasting_model.pkl'")

if __name__ == "__main__":
    run_forecasting()
