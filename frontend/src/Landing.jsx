import React from 'react';
import { useNavigate } from 'react-router-dom';
import './App.css';
import heroImage from './assets/hero_nature_grid.png';

function Landing() {
    const navigate = useNavigate();

    return (
        <div className="landing-container">
            <div className="landing-content">
                <h1 className="title landing-title">Intelligent Forecasting System</h1>
                <p className="subtitle landing-subtitle">
                    Advanced AI-powered supply chain optimization for Power Transmission and Substation Infrastructure.
                </p>

                <div className="hero-image-container">
                    <img src={heroImage} alt="Power Grid in Nature" className="hero-image" />
                </div>

                <div className="landing-features">
                    <div className="feature-card">
                        <h3>Predictive Analytics</h3>
                        <p>Accurate material demand forecasting using machine learning based on historical data.</p>
                    </div>
                    <div className="feature-card">
                        <h3>Smart Clustering</h3>
                        <p>Automatic categorization of project types (Maintenance, New Install, Upgrades) for tailored insights.</p>
                    </div>
                    <div className="feature-card">
                        <h3>Grid Optimization</h3>
                        <p>Reduce downtime and overstocking by precise resource allocation.</p>
                    </div>
                </div>

                <button className="submit-btn landing-btn" onClick={() => navigate('/forecast')}>
                    Launch Forecasting Module
                </button>
            </div>
        </div>
    );
}

export default Landing;
