# Deploying to Azure for Free

This guide outlines how to deploy your **Material Demand Forecasting** project to Azure using their free tier services. We will use **Azure App Service (Free Tier)** for the Python backend and **Azure Static Web Apps (Free Tier)** for the React frontend.

## Prerequisites

1.  **Azure Account**: [Create a free account](https://azure.microsoft.com/free/).
2.  **GitHub Account**: Your code must be pushed to a GitHub repository.
3.  **Azure CLI** (Optional, but useful).

---

## Step 1: Prepare Your Code (Already Done)

I have already made the necessary changes to your code:
1.  **Backend**: Added `gunicorn` to `backend/requirements.txt` (required for production server).
2.  **Frontend**: Updated `frontend/src/Forecast.jsx` to read the API URL from an environment variable (`VITE_API_URL`).

**Action Required**: Push these changes to your GitHub repository.
```bash
git add .
git commit -m "Prepare for Azure deployment"
git push origin main
```

---

## Step 2: Deploy Backend (Azure App Service)

1.  **Log in to Azure Portal** (portal.azure.com).
2.  **Create a resource** -> Search for **"Web App"** -> Create.
3.  **Basics Tab**:
    *   **Subscription**: Select your subscription.
    *   **Resource Group**: Create a new one (e.g., `mlpro-rg`).
    *   **Name**: Unique name (e.g., `mlpro-backend-api`).
    *   **Publish**: Code.
    *   **Runtime stack**: Python 3.9 (or 3.10/3.11).
    *   **Operating System**: Linux.
    *   **Region**: Select one close to you.
    *   **Pricing Plan**: Select **Free F1** (View all plans -> Dev/Test -> F1).
4.  **Deployment Tab**:
    *   **Continuous deployment**: Enable.
    *   **GitHub Account**: Connect your account.
    *   **Organization/Repository/Branch**: Select your repo and branch.
5.  **Review + create** -> **Create**.
6.  **Configuration (CRITICAL)**:
    *   Go to the resource once created.
    *   In the sidebar, go to **Settings** -> **Configuration**.
    *   Go to **General settings** tab.
    *   **Startup Command**: Enter: `gunicorn --bind=0.0.0.0 --timeout 600 app:app`
        *   *Note: We set a high timeout because loading the large model file might take a few seconds.*
    *   Click **Save**.
7.  **Get Backend URL**:
    *   Go to the **Overview** page. Copy the **Default domain** (e.g., `https://mlpro-backend-api.azurewebsites.net`).

---

## Step 3: Deploy Frontend (Azure Static Web Apps)

1.  In Azure Portal, search for **"Static Web Apps"** -> Create.
2.  **Basics Tab**:
    *   **Subscription**: Same as above.
    *   **Resource Group**: Select the one you created (e.g., `mlpro-rg`).
    *   **Name**: Unique name (e.g., `mlpro-frontend`).
    *   **Plan type**: **Free**.
    *   **Source**: GitHub.
    *   **GitHub details**: Select your repo and branch.
    *   **Build Presets**: Select **React** (or Custom).
    *   **App location**: `/frontend`
    *   **Api location**: (Leave empty).
    *   **Output location**: `dist`
3.  **Review + create** -> **Create**.
4.  **Configure Environment Variable**:
    *   Once created, go to the resource.
    *   In the sidebar, go to **Settings** -> **Environment variables**.
    *   Add a new variable:
        *   **Name**: `VITE_API_URL`
        *   **Value**: Your Backend URL from Step 2 (e.g., `https://mlpro-backend-api.azurewebsites.net`)
        *   *Important: Do not add a trailing slash.*
    *   Click **Apply**.
5.  **Redeploy**:
    *   Changing environment variables might require a redeploy. You can trigger this by making a small commit to your repo, or usually, Azure SWA picks it up automatically or offers a "Browse" button that works. If it doesn't work immediately, go to your GitHub Actions tab in your repo and re-run the latest workflow.

---

## Step 4: Verification

1.  Open your Frontend URL (found in Static Web App Overview).
2.  Enter some values and click "Generate Forecast".
3.  If it works, you're done!

### Troubleshooting
*   **500 Error on Backend**: Check **Log stream** in the App Service sidebar to see if python crashed (e.g., missing library).
*   **Cors Error**: In the Backend App Service, go to **CORS** in the sidebar and add your Frontend URL to the allowed origins. Check "Enable Access-Control-Allow-Credentials" if needed.
