#!/usr/bin/env python3
"""
Jolly Dollars Fraud Dashboard Deployment Script

This script prepares the dashboard for GitHub Pages deployment by:
1. Generating the latest dashboard data
2. Validating all files are present
3. Creating a deployment-ready package
"""

import os
import json
import shutil
import subprocess
from pathlib import Path

def generate_dashboard_data():
    """Generate the latest dashboard data from the CSV file."""
    print("🔄 Generating dashboard data...")
    
    script = """
import pandas as pd
import json
from datetime import datetime
import numpy as np

# Load the data
df = pd.read_csv('Lead Fraud Analyst _Case_Assessment_Data.csv')

# Clean and prepare data
df['APPLICATION_SUBMITTED_DATE'] = pd.to_datetime(df['APPLICATION_SUBMITTED_DATE'], errors='coerce')
df['date'] = df['APPLICATION_SUBMITTED_DATE'].dt.date
df['month'] = df['APPLICATION_SUBMITTED_DATE'].dt.to_period('M')

# Daily trends
daily_trends = df.groupby('date')['FRAUD_STATUS'].value_counts().unstack(fill_value=0)
daily_trends_json = []
for date, row in daily_trends.iterrows():
    daily_trends_json.append({
        'date': str(date),
        'Pass': int(row.get('Pass', 0)),
        'Fail': int(row.get('Fail', 0)),
        'Confirmed_Fraud': int(row.get('Confirmed Fraud', 0)),
        'Manual_Review': int(row.get('Manual Review', 0)),
        'Manual_Review_No_Case': int(row.get('Manual Review No Case', 0)),
        'False_Positive': int(row.get('False Positive', 0))
    })

# Model performance
model_performance = df.groupby(['FRAUD_MODEL_RESULT', 'FRAUD_STATUS']).size().unstack(fill_value=0)
model_perf_json = []
for model, row in model_performance.iterrows():
    model_perf_json.append({
        'model_result': model,
        'Pass': int(row.get('Pass', 0)),
        'Fail': int(row.get('Fail', 0)),
        'Confirmed_Fraud': int(row.get('Confirmed Fraud', 0)),
        'Manual_Review': int(row.get('Manual Review', 0)),
        'Manual_Review_No_Case': int(row.get('Manual Review No Case', 0)),
        'False_Positive': int(row.get('False Positive', 0))
    })

# Behavior and device scores
behavior_scores = df[df['BEHAVIOR_CHECK_SCORE'].notna()]['BEHAVIOR_CHECK_SCORE'].value_counts().sort_index()
behavior_json = [{'score': float(score), 'count': int(count)} for score, count in behavior_scores.items()]

device_scores = df[df['DEVICE_CHECK_SCORE'].notna()]['DEVICE_CHECK_SCORE'].value_counts().sort_index()
device_json = [{'score': float(score), 'count': int(count)} for score, count in device_scores.items()]

# Monthly trends
monthly_trends = df.groupby('month')['FRAUD_STATUS'].value_counts().unstack(fill_value=0)
monthly_json = []
for month, row in monthly_trends.iterrows():
    monthly_json.append({
        'month': str(month),
        'Pass': int(row.get('Pass', 0)),
        'Fail': int(row.get('Fail', 0)),
        'Confirmed_Fraud': int(row.get('Confirmed Fraud', 0)),
        'Manual_Review': int(row.get('Manual Review', 0)),
        'Manual_Review_No_Case': int(row.get('Manual Review No Case', 0)),
        'False_Positive': int(row.get('False Positive', 0))
    })

# Summary statistics
summary = {
    'total_applications': len(df),
    'fraud_rate': round((df['FRAUD_STATUS'] == 'Confirmed Fraud').sum() / len(df) * 100, 2),
    'pass_rate': round((df['FRAUD_STATUS'] == 'Pass').sum() / len(df) * 100, 2),
    'manual_review_rate': round(((df['FRAUD_STATUS'] == 'Manual Review') | (df['FRAUD_STATUS'] == 'Manual Review No Case')).sum() / len(df) * 100, 2),
    'false_positive_rate': round((df['FRAUD_STATUS'] == 'False Positive').sum() / len(df) * 100, 2)
}

# Fraud reasons analysis
fraud_reasons = []
for reasons in df['FRAUD_MODEL_REASONS'].dropna():
    if isinstance(reasons, str) and reasons.startswith('['):
        try:
            parsed_reasons = eval(reasons)
            fraud_reasons.extend(parsed_reasons)
        except:
            pass

from collections import Counter
reason_counts = Counter(fraud_reasons)
top_reasons = [{'reason': k, 'count': v} for k, v in reason_counts.most_common(10)]

# Export dashboard data
dashboard_data = {
    'summary': summary,
    'daily_trends': daily_trends_json,
    'monthly_trends': monthly_json,
    'model_performance': model_perf_json,
    'behavior_scores': behavior_json,
    'device_scores': device_json,
    'fraud_reasons': top_reasons
}

# Save to file
with open('../Data_Analysis/Github_Pages/dashboard_data.json', 'w') as f:
    json.dump(dashboard_data, f, indent=2)

print("✅ Dashboard data generated successfully!")
"""
    
    # Change to assignment files directory and run the script
    os.chdir("Assignment_Files")
    exec(script)
    os.chdir("..")

def validate_files():
    """Validate that all required files are present."""
    print("🔍 Validating files...")
    
    required_files = [
        "Data_Analysis/Github_Pages/index.html",
        "Data_Analysis/Github_Pages/dashboard_data.json",
        "Data_Analysis/Github_Pages/README.md",
        "Data_Analysis/Github_Pages/_config.yml"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ Missing files:")
        for file in missing_files:
            print(f"  - {file}")
        return False
    
    print("✅ All required files are present")
    return True

def create_deployment_package():
    """Create a deployment-ready package."""
    print("📦 Creating deployment package...")
    
    # Create docs directory for alternative GitHub Pages setup
    docs_dir = "docs"
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
    
    os.makedirs(docs_dir)
    
    # Copy files to docs directory
    source_dir = "Data_Analysis/Github_Pages"
    for file in os.listdir(source_dir):
        if file.endswith(('.html', '.json', '.md', '.yml')):
            shutil.copy2(os.path.join(source_dir, file), docs_dir)
    
    print(f"✅ Deployment package created in '{docs_dir}' directory")

def display_setup_instructions():
    """Display GitHub Pages setup instructions."""
    print("\n" + "="*60)
    print("🚀 GITHUB PAGES SETUP INSTRUCTIONS")
    print("="*60)
    print()
    print("1. Push your code to GitHub:")
    print("   git add .")
    print("   git commit -m 'Add fraud analysis dashboard'")
    print("   git push origin main")
    print()
    print("2. Enable GitHub Pages:")
    print("   - Go to repository Settings")
    print("   - Navigate to 'Pages' section")
    print("   - Source: 'Deploy from a branch'")
    print("   - Branch: 'main'")
    print("   - Folder: '/Data_Analysis/Github_Pages' or '/docs'")
    print()
    print("3. Access your dashboard:")
    print("   https://[username].github.io/[repository-name]/")
    print()
    print("4. Alternative: Use the 'docs' folder")
    print("   - Select '/docs' as the source folder in GitHub Pages settings")
    print("   - This provides a cleaner URL structure")
    print()
    print("📊 Dashboard Features:")
    print("   - Interactive fraud status distribution")
    print("   - Model performance analysis")
    print("   - Temporal trends and patterns")
    print("   - Risk score correlations")
    print("   - Mobile-responsive design")
    print()
    print("✨ Your dashboard is ready for deployment!")

def main():
    """Main deployment function."""
    print("🪙 Jolly Dollars Fraud Dashboard Deployment")
    print("="*50)
    print()
    
    try:
        # Generate latest data
        generate_dashboard_data()
        
        # Validate files
        if not validate_files():
            print("❌ Deployment failed due to missing files")
            return
        
        # Create deployment package
        create_deployment_package()
        
        # Display instructions
        display_setup_instructions()
        
    except Exception as e:
        print(f"❌ Deployment failed: {str(e)}")
        return

if __name__ == "__main__":
    main()
