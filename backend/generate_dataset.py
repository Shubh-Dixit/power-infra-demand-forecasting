import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_data(num_samples=5000):
    np.random.seed(42)
    random.seed(42)

    # --- Feature Generation ---
    
    # Date (over last 3 years)
    start_date = datetime(2021, 1, 1)
    dates = [start_date + timedelta(days=random.randint(0, 1095)) for _ in range(num_samples)]
    dates.sort()

    regions = ['North', 'South', 'East', 'West', 'Central']
    terrains = ['Urban', 'Rural', 'Mountainous', 'Coastal']
    infra_types = ['Substation', 'Transmission_Line']
    project_cats = ['New_Installation', 'Maintenance', 'Emergency_Repair', 'System_Upgrade']
    voltages = [33, 66, 132, 220, 400]
    weather = ['Clear', 'Rainy', 'Storm', 'Heatwave', 'Snow']

    data = {
        'Date': dates,
        'Region': np.random.choice(regions, num_samples),
        'Terrain': np.random.choice(terrains, num_samples),
        'Infrastructure_Type': np.random.choice(infra_types, num_samples, p=[0.4, 0.6]),
        'Project_Category': np.random.choice(project_cats, num_samples, p=[0.2, 0.5, 0.1, 0.2]),
        'Voltage_Level_kV': np.random.choice(voltages, num_samples),
        'Weather_Condition': np.random.choice(weather, num_samples),
    }
    
    df = pd.DataFrame(data)

    # Logic-based assignments
    # Route length depends on infra type (Substation usually has 0 or low track length, Transmission has high)
    df['Route_Length_km'] = df.apply(lambda row: np.random.uniform(5, 100) if row['Infrastructure_Type'] == 'Transmission_Line' else np.random.uniform(0.1, 2), axis=1)

    # --- Target (Material) Generation with Correlation ---
    
    def calculate_materials(row):
        # Base multipliers based on voltage (higher voltage = heavier/more expensive equipment)
        voltage_factor = row['Voltage_Level_kV'] / 33.0 
        
        # Transmission Line Logic
        if row['Infrastructure_Type'] == 'Transmission_Line':
            # 3 phases, plus some sag/waste. ~3.1km of conductor per km of route
            conductor = row['Route_Length_km'] * 1000 * 3.1 * (1 + (voltage_factor * 0.1)) 
            towers = row['Route_Length_km'] * 3 # Approx 3 towers per km
            insulators = towers * 3 * (1 + int(voltage_factor)) # Discs per string depends on voltage
            transformers = 0 # Lines don't usually implement main power transformers directly
            breakers = 0 
            concrete = towers * 15 * voltage_factor # Foundation per tower
            
            # Adjust for project type
            if row['Project_Category'] == 'Maintenance':
                conductor *= 0.05 # Only replacing sections
                towers *= 0.01 # Rare to replace whole towers
                insulators *= 0.2 # Replace damaged ones
                concrete *= 0.05
            elif row['Project_Category'] == 'Emergency_Repair':
                conductor *= 0.1
                towers = np.random.randint(0, 3) # Maybe 1 or 2 collapsed towers
                insulators *= 0.1
                concrete *= 0.1

        # Substation Logic
        else:
            conductor = np.random.uniform(500, 5000) # Busbars and connections
            towers = np.random.randint(5, 20) # Gantries
            insulators = np.random.uniform(100, 1000)
            transformers = np.random.randint(1, 4) if row['Project_Category'] in ['New_Installation', 'System_Upgrade'] else 0
            breakers = np.random.randint(2, 10) if row['Project_Category'] != 'Maintenance' else np.random.choice([0, 1])
            concrete = np.random.uniform(100, 1000) # Foundations for equipment
            
            if row['Project_Category'] == 'Maintenance':
               conductor *= 0.1
               concrete *= 0.1
               
        # Random noise/variability
        conductor = int(max(0, conductor * np.random.uniform(0.9, 1.1)))
        towers = int(max(0, towers * np.random.uniform(0.9, 1.1)))
        insulators = int(max(0, insulators * np.random.uniform(0.8, 1.2)))
        concrete = round(max(0, concrete * np.random.uniform(0.8, 1.2)), 2)
        
        return pd.Series([conductor, towers, insulators, transformers, breakers, concrete])

    df[['ACSR_Conductor_m', 'Towers_Steel_Count', 'Insulators_Count', 'Power_Transformers_Count', 'Circuit_Breakers_Count', 'Concrete_m3']] = df.apply(calculate_materials, axis=1)

    # Save to CSV
    df.to_csv('material_demand_data.csv', index=False)
    print("Dataset generated: material_demand_data.csv with", num_samples, "rows.")

if __name__ == "__main__":
    generate_data()
