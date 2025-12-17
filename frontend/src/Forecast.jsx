import { useState } from 'react'
import './App.css'
import realConductor from './assets/real_conductor.png'
import realTower from './assets/real_steel_tower.png'
import realInsulator from './assets/real_insulator.png'
import realConcrete from './assets/real_concrete.png'
import realTransformer from './assets/real_transformer.png'
import realBreaker from './assets/real_circuit_breaker.png'

function Forecast() {
    const [formData, setFormData] = useState({
        Region: 'North',
        Terrain: 'Urban',
        Infrastructure_Type: 'Transmission_Line',
        Project_Category: 'New_Installation',
        Voltage_Level_kV: '33',
        Weather_Condition: 'Clear',
        Route_Length_km: '10'
    })

    const [result, setResult] = useState(null)
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState(null)

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        })
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        setLoading(true)
        setError(null)
        setResult(null)

        try {
            const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000';
            const response = await fetch(`${API_URL}/predict`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            })

            if (!response.ok) {
                throw new Error('Failed to fetch prediction')
            }

            const data = await response.json()
            setResult(data)
        } catch (err) {
            setError(err.message)
        } finally {
            setLoading(false)
        }
    }

    return (
        <div>
            <header className="header" style={{ marginTop: '2rem' }}>
                <h1 className="title">Demand Forecast</h1>
                <p className="subtitle">Enter project parameters below</p>
            </header>

            <div className="main-content">
                <section className="form-section">
                    <form className="form-card" onSubmit={handleSubmit}>
                        <div className="form-group">
                            <label className="form-label">Region</label>
                            <select name="Region" value={formData.Region} onChange={handleChange} className="form-select">
                                <option value="North">North</option>
                                <option value="South">South</option>
                                <option value="East">East</option>
                                <option value="West">West</option>
                                <option value="Central">Central</option>
                            </select>
                        </div>

                        <div className="form-group">
                            <label className="form-label">Terrain</label>
                            <select name="Terrain" value={formData.Terrain} onChange={handleChange} className="form-select">
                                <option value="Urban">Urban</option>
                                <option value="Rural">Rural</option>
                                <option value="Mountainous">Mountainous</option>
                                <option value="Coastal">Coastal</option>
                            </select>
                        </div>

                        <div className="form-group">
                            <label className="form-label">Infrastructure Type</label>
                            <select name="Infrastructure_Type" value={formData.Infrastructure_Type} onChange={handleChange} className="form-select">
                                <option value="Transmission_Line">Transmission Line</option>
                                <option value="Substation">Substation</option>
                            </select>
                        </div>

                        <div className="form-group">
                            <label className="form-label">Project Category</label>
                            <select name="Project_Category" value={formData.Project_Category} onChange={handleChange} className="form-select">
                                <option value="New_Installation">New Installation</option>
                                <option value="Maintenance">Maintenance</option>
                                <option value="Emergency_Repair">Emergency Repair</option>
                                <option value="System_Upgrade">System Upgrade</option>
                            </select>
                        </div>

                        <div className="form-group">
                            <label className="form-label">Voltage Level (kV)</label>
                            <select name="Voltage_Level_kV" value={formData.Voltage_Level_kV} onChange={handleChange} className="form-select">
                                <option value="33">33 kV</option>
                                <option value="66">66 kV</option>
                                <option value="132">132 kV</option>
                                <option value="220">220 kV</option>
                                <option value="400">400 kV</option>
                            </select>
                        </div>

                        <div className="form-group">
                            <label className="form-label">Weather Condition</label>
                            <select name="Weather_Condition" value={formData.Weather_Condition} onChange={handleChange} className="form-select">
                                <option value="Clear">Clear</option>
                                <option value="Rainy">Rainy</option>
                                <option value="Storm">Storm</option>
                                <option value="Heatwave">Heatwave</option>
                                <option value="Snow">Snow</option>
                            </select>
                        </div>

                        <div className="form-group">
                            <label className="form-label">Route Length (km) / Substation Area</label>
                            <input
                                type="number"
                                name="Route_Length_km"
                                value={formData.Route_Length_km}
                                onChange={handleChange}
                                className="form-input"
                                min="0"
                                step="0.1"
                                required
                            />
                        </div>

                        <button type="submit" className="submit-btn" disabled={loading}>
                            {loading ? 'Analyzing...' : 'Generate Forecast'}
                        </button>
                    </form>
                </section>

                <section className="result-section">
                    {error && (
                        <div className="result-card" style={{ borderColor: '#ef4444' }}>
                            <h3 style={{ color: '#ef4444' }}>Error</h3>
                            <p>{error}</p>
                        </div>
                    )}

                    {result ? (
                        <div className="result-card">
                            <h2>Forecasted Demand</h2>
                            <div className="result-grid">
                                <div className="metric-item">
                                    <img src={realConductor} alt="Conductor" className="metric-icon" />
                                    <span className="metric-value">{result.ACSR_Conductor_m}</span>
                                    <span className="metric-label">Conductor (m)</span>
                                </div>
                                <div className="metric-item">
                                    <img src={realTower} alt="Tower" className="metric-icon" />
                                    <span className="metric-value">{result.Towers_Steel_Count}</span>
                                    <span className="metric-label">Steel Towers</span>
                                </div>
                                <div className="metric-item">
                                    <img src={realInsulator} alt="Insulator" className="metric-icon" />
                                    <span className="metric-value">{result.Insulators_Count}</span>
                                    <span className="metric-label">Insulators</span>
                                </div>
                                <div className="metric-item">
                                    <img src={realConcrete} alt="Concrete" className="metric-icon" />
                                    <span className="metric-value">{result.Concrete_m3}</span>
                                    <span className="metric-label">Concrete (m³)</span>
                                </div>
                                <div className="metric-item">
                                    <img src={realTransformer} alt="Transformer" className="metric-icon" />
                                    <span className="metric-value">{result.Power_Transformers_Count}</span>
                                    <span className="metric-label">Transformers</span>
                                </div>
                                <div className="metric-item">
                                    <img src={realBreaker} alt="Breaker" className="metric-icon" />
                                    <span className="metric-value">{result.Circuit_Breakers_Count}</span>
                                    <span className="metric-label">Circuit Breakers</span>
                                </div>
                            </div>
                        </div>
                    ) : (
                        <div className="empty-state">
                            <p>Enter project details to view material demand forecast.</p>
                        </div>
                    )}
                </section>
            </div>
        </div>
    )
}

export default Forecast
