# Deployment Guide: Render (Docker) + Vercel

This guide outlines the steps to deploy your full-stack application using **Docker** for the backend on Render and Vercel for the frontend.

## Prerequisites

1.  **GitHub Account**: Ensure your code is pushed to a GitHub repository.
2.  **Render Account**: For deploying the backend container.
3.  **Vercel Account**: For deploying the frontend.

---

## Part 1: Prepare the Codebase

A `Dockerfile` has been added to the `backend/` directory. This tells Render exactly how to build your application and includes a step to generate the machine learning model automatically during the build.

**Action Required:**
Push the new Docker configuration to GitHub:
```bash
git add .
git commit -m "Add Docker configuration for Render"
git push origin main
```

---

## Part 2: Deploy Backend on Render (Using Docker)

1.  Log in to [Render Dashboard](https://dashboard.render.com/).
2.  Click **New +** and select **Web Service**.
3.  Connect your GitHub repository.
4.  Configure the service:
    *   **Name**: `power-demand-backend`
    *   **Region**: Choose the one closest to you.
    *   **Root Directory**: `backend` (Important: tell Render to look in the backend folder).
    *   **Runtime**: **Docker** (Select this option).
    *   **Instance Type**: Free
    *   *Note: Render will automatically find the `Dockerfile` in the `backend` directory and build it.*
5.  Click **Create Web Service**.
6.  Wait for the build to finish. It will install dependencies and run `python forecasting_model.py`.
7.  Once live, copy the URL (e.g., `https://power-demand-backend.onrender.com`).

---

## Part 3: Deploy Frontend on Vercel

1.  Log in to [Vercel Dashboard](https://vercel.com/dashboard).
2.  Click **Add New...** > **Project**.
3.  Import your GitHub repository.
4.  Configure the project:
    *   **Framework Preset**: Vite.
    *   **Root Directory**: `frontend`.
    *   **Environment Variables**:
        *   Key: `VITE_API_URL`
        *   Value: Paste your Render Backend URL (e.g., `https://power-demand-backend.onrender.com`).
        *   *No trailing slash.*
5.  Click **Deploy**.

---

## Part 4: Testing

1.  Open the Vercel URL.
2.  Enter values and click "Generate Forecast".
3.  The frontend will talk to your Dockerized backend on Render.
