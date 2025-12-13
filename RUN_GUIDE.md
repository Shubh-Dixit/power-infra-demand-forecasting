# How to Run the Intelligent Forecasting System

This guide provides step-by-step instructions to set up and run the full stack application.

## Prerequisites
- **Python** (3.8 or higher)
- **Node.js** (18 or higher) & **npm**

## 1. Backend Setup (Flask API & ML Model)

Open a terminal or command prompt in the project root directory (`e:\mlpro`).

### A. Navigate to Backend
```bash
cd backend
```

### B. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### C. Generate Data & Train Model (One-time Setup)
If you haven't generated the data or trained the model yet, run these commands:

1. **Generate Dataset**:
   ```bash
   python generate_dataset.py
   ```
   *(Creates `material_demand_data.csv`)*

2. **Run Clustering Analysis**:
   ```bash
   python clustering_analysis.py
   ```
   *(Creates `material_demand_data_clustered.csv`, categorizes the projects, and generates `cluster_plot.png`)*

3. **Train Forecasting Model**:
   ```bash
   python forecasting_model.py
   ```
   *(Trains the Random Forest model and saves it as `demand_forecasting_model.pkl`)*

### D. Start the Backend Server
Now, start the Flask API server which serves the predictions:
```bash
python app.py
```
The backend will run at **http://127.0.0.1:5000**.
**Important**: Keep this terminal open while using the app.

---

## 2. Frontend Setup (React Application)

Open a **new** terminal window (do not close the backend one) and navigate to the frontend directory:

```bash
cd frontend
```

### A. Install Node Dependencies
(Only needed the first time you run the project)
```bash
npm install
```

### B. Start the Frontend Application
```bash
npm run dev
```
The frontend will start (usually at **http://localhost:5173**).
**Important**: Keep this terminal open as well.

---

## 3. Accessing the Application

1. Open your web browser.
2. Go to the URL shown in the frontend terminal (e.g., **http://localhost:5173**).
3. You should see the "Material Demand AI" dashboard.
4. Select inputs (Region, Terrain, etc.) and click "Generate Forecast" to see predictions from the backend.
