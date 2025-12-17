# Intelligent Forecasting System for Power Infrastructure

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://power-infra-demand-forecasting.vercel.app/)


![Project Hero](frontend/src/assets/hero_nature_grid.png)

## About the Project
The **Intelligent Forecasting System** is an advanced AI-powered web application designed to optimize supply chain management for Power Transmission and Substation infrastructure projects. By leveraging machine learning, it accurately predicts material requirements (like cables, towers, and transformers) based on project parameters such as region, terrain, and voltage level.

The user interface features a **"Natural & Humanized" design**, moving away from cold technical aesthetics to a warm, organic, and accessible look, emphasizing the harmony between technology and nature.

## Key Features
- **Predictive Analytics**: Uses a Random Forest Regressor to forecast precise material quantities (`Conductors`, `Steel Towers`, `Concrete`, `Insulators`, `Transformers`, `Circuit Breakers`).
- **Smart Clustering**: automatically categorizes projects (e.g., 'New Installation', 'Maintenance') using K-Means clustering to tailor insights.
- **Natural UI/UX**: A responsive, card-based interface with a warm color palette (`Stone`, `Sage Green`) and hyper-realistic visual assets.
- **Real-time Interaction**: Instant forecast generation via a Flask API backend.

## Technology Stack
- **Frontend**: React.js, Vite, CSS3 (Custom Natural Theme).
- **Backend**: Python 3, Flask.
- **Machine Learning**: Scikit-learn (Random Forest, K-Means), Pandas, NumPy.

---

## How to Run

### Prerequisites
- **Python** (3.8 or higher)
- **Node.js** (18 or higher) & **npm**

### 1. Backend Setup (Flask API & ML Model)

Open a terminal in the project root (`e:\mlpro`) and navigate to the backend:

1.  **Navigate to Backend**:
    ```bash
    cd backend
    ```

2.  **Install Python Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Initialize Data & Models** (Run these in order if setting up for the first time):
    *   Generate synthetic dataset:
        ```bash
        python generate_dataset.py
        ```
    *   Perform clustering analysis:
        ```bash
        python clustering_analysis.py
        ```
    *   Train the forecasting model:
        ```bash
        python forecasting_model.py
        ```

4.  **Start the Server**:
    ```bash
    python app.py
    ```
    The backend will run at `http://127.0.0.1:5000`.

### 2. Frontend Setup (React Application)

Open a **new** terminal window (keep the backend running) and navigate to the frontend:

1.  **Navigate to Frontend**:
    ```bash
    cd frontend
    ```

2.  **Install Dependencies** (First time only):
    ```bash
    npm install
    ```

3.  **Start the Development Server**:
    ```bash
    npm run dev
    ```

### 3. Using the Application

1.  Open your browser and visit the URL shown in the frontend terminal (usually `http://localhost:5173`).
2.  Click **"Launch Forecasting Module"** on the landing page.
3.  Fill in the project details (Region, Terrain, Voltage, etc.).
4.  Click **"Generate Forecast"** to view the predicted material requirements with realistic visualizations.
