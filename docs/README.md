# Jolly Dollars Fraud Dashboard

A comprehensive, interactive dashboard for analyzing fraud detection patterns and model performance.

## 📊 Dashboard Features

### Key Metrics
- **Total Applications**: 46,258 applications analyzed
- **Fraud Rate**: 6.06% confirmed fraud cases
- **Pass Rate**: 47.02% applications approved
- **Manual Review Rate**: 38.89% requiring manual review

### Interactive Charts

1. **Fraud Status Distribution**: Pie chart showing the distribution of all fraud statuses
2. **Model Performance**: Stacked bar chart comparing fraud model results with actual outcomes
3. **Monthly Trends**: Line chart showing fraud trends over time
4. **Behavior Check Scores**: Distribution of behavioral analysis scores
5. **Device Check Scores**: Distribution of device fingerprinting scores
6. **Daily Volume Trends**: Combined chart showing application volume and fraud detection rates

## 🚀 Setup Instructions

### For GitHub Pages

1. **Enable GitHub Pages**:
   - Go to your repository settings
   - Navigate to "Pages" section
   - Select source: "Deploy from a branch"
   - Choose branch: `main` (or your default branch)
   - Select folder: `/Data_Analysis/Github_Pages`

2. **Access the Dashboard**:
   - Your dashboard will be available at: `https://[username].github.io/[repository-name]/`
   - Replace `[username]` with your GitHub username
   - Replace `[repository-name]` with your repository name

### Local Development

1. **Serve locally**:
   ```bash
   # Navigate to the Github_Pages directory
   cd Data_Analysis/Github_Pages
   
   # Start a simple HTTP server (Python 3)
   python -m http.server 8000
   
   # Or using Node.js (if you have it installed)
   npx serve .
   ```

2. **Access locally**:
   - Open your browser to `http://localhost:8000`

## 📁 Files Structure

```
Github_Pages/
├── index.html          # Main dashboard HTML file
├── dashboard_data.json  # Processed fraud analysis data
└── README.md           # This file
```

## 🎨 Dashboard Components

### Summary Statistics Cards
- Real-time metrics with hover effects
- Color-coded for quick visual assessment
- Responsive design for mobile devices

### Interactive Charts
- Built with Chart.js for smooth animations
- Responsive and mobile-friendly
- Hover tooltips for detailed information
- Multiple chart types: doughnut, bar, line, and combination charts

### Data Processing
- Automated data aggregation from CSV source
- Date-based trending analysis
- Cross-referencing between fraud models and actual outcomes

## 🔧 Customization

### Colors
The dashboard uses a carefully selected color palette:
- **Primary**: Blue gradient (#667eea to #764ba2)
- **Success**: Green (#27ae60) for approved applications
- **Danger**: Red (#e74c3c) for fraud cases
- **Warning**: Orange (#f39c12) for manual reviews
- **Info**: Blue (#3498db) for informational data

### Adding New Charts
To add a new chart:

1. Add a new chart container in the HTML
2. Process the required data in the Python script
3. Create a new chart function in JavaScript
4. Call the function in the `loadDashboard()` method

## 📱 Mobile Responsiveness

The dashboard is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones
- Various screen orientations

## 🛠️ Technical Details

### Dependencies
- **Chart.js**: For creating interactive charts
- **Date-fns**: For date manipulation and formatting
- **Modern CSS Grid**: For responsive layout

### Browser Support
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

### Performance
- Lazy loading of chart data
- Optimized for datasets up to 50K records
- Efficient data sampling for large time series

## 📈 Data Insights

The dashboard reveals several key insights:

1. **Model Accuracy**: The fraud detection model shows good performance with clear patterns
2. **Seasonal Trends**: Fraud attempts may show temporal patterns
3. **Score Distributions**: Behavior and device scores provide valuable risk indicators
4. **Review Efficiency**: High manual review rate suggests opportunities for model tuning

## 🔒 Security & Privacy

- No sensitive data is exposed in the dashboard
- All personal identifiers are hashed in the source data
- Static deployment ensures no server-side vulnerabilities

## 📞 Support

For questions or issues with the dashboard:
1. Check the browser console for JavaScript errors
2. Verify the `dashboard_data.json` file is accessible
3. Ensure your browser supports modern JavaScript features

---

**Last Updated**: August 2, 2025  
**Data Period**: January 1, 2025 - March 31, 2025  
**Total Records**: 46,258 applications
