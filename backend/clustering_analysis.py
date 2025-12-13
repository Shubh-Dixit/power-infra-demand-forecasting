import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

def run_clustering():
    # 1. Load Data
    print("Loading data...")
    df = pd.read_csv('material_demand_data.csv')
    
    # 2. Select Features for Clustering
    # We want to cluster based on the input features to find 'types' of projects/conditions
    # OR we can cluster based on Demand to find 'Demand Profiles'.
    # Let's cluster based on Material Demand to identify "High", "Medium", "Low" resource scenarios.
    
    demand_features = ['ACSR_Conductor_m', 'Towers_Steel_Count', 'Insulators_Count', 'Power_Transformers_Count', 'Circuit_Breakers_Count', 'Concrete_m3']
    X = df[demand_features]
    
    # 3. Preprocessing
    print("Preprocessing...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 4. K-Means Clustering
    # We'll try 3 clusters for simplicity (e.g., Low, Medium, High intensity projects)
    print("Running K-Means...")
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(X_scaled)
    
    df['Cluster'] = clusters
    
    # Analyze Clusters
    cluster_summary = df.groupby('Cluster')[demand_features].mean()
    print("\nCluster Centers (Average Material Demand):")
    print(cluster_summary)

    # Automated Labeling based on 'Power_Transformers_Count' and 'ACSR_Conductor_m'
    # Cluster with Transformers > 1 is likely "Substation"
    # Cluster with Max Conductor is "Major_Transmission"
    # Remaining is "Minor_Transmission/Maintenance"
    
    label_map = {}
    for cluster_id in cluster_summary.index:
        row = cluster_summary.loc[cluster_id]
        if row['Power_Transformers_Count'] > 0.5:
            label_map[cluster_id] = 'Substation_Project'
        elif row['ACSR_Conductor_m'] == cluster_summary['ACSR_Conductor_m'].max():
            label_map[cluster_id] = 'Major_Transmission_Line'
        else:
            label_map[cluster_id] = 'Minor_Transmission_Maintenance'
            
    df['Cluster_Label'] = df['Cluster'].map(label_map)
    print("\nCluster Labels assigned:", label_map)

    # Save Labeled Data
    df.to_csv('material_demand_data_clustered.csv', index=False)
    print("Saved labeled data to 'material_demand_data_clustered.csv'")
    
    # Save descriptive stats
    with open('cluster_description.txt', 'w') as f:
        f.write("Unsupervised Learning: K-Means Clustering on Material Demand\n")
        f.write("============================================================\n\n")
        f.write("Cluster Mean Values:\n")
        f.write(cluster_summary.to_string())
        f.write("\n\nInterpretation & Labels:\n")
        for k, v in label_map.items():
            f.write(f"Cluster {k}: {v}\n")

    # 5. Visualization (PCA)
    print("Generating PCA Plot...")
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(X_scaled)
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=principal_components[:, 0], y=principal_components[:, 1], hue=df['Cluster_Label'], palette='viridis', alpha=0.7)
    plt.title('Material Demand Clusters (PCA Reduced)')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend(title='Project Type')
    plt.savefig('cluster_plot.png')
    print("Plot saved to cluster_plot.png")

if __name__ == "__main__":
    run_clustering()
