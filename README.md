**Solar Insights Analysis: Weather and Solar Radiation Data Exploration**

---

### **Overview**
This project involves analyzing meteorological and solar radiation data to uncover patterns, relationships, and anomalies. The analysis is focused on key weather metrics like solar radiation components (GHI, DNI, DHI), temperature (Tamb), wind conditions (WS, WSgust, WD), and relative humidity (RH). 

#### **Goals:**
1. Examine relationships between weather variables.
2. Detect anomalies and outliers using statistical measures (e.g., Z-scores).
3. Explore complex multivariate relationships using advanced visualizations (e.g., bubble charts, wind roses).
4. Investigate patterns in solar irradiance and wind data.

---

### **Installation**
#### **Prerequisites:**
- Python 3.10+
- Required libraries:
  ```
  pandas
  numpy
  matplotlib
  seaborn
  scipy
  windrose
  ```
- Install dependencies:
  ```
  pip install -r requirements.txt
  ```

---

### **Usage**
1. Place the dataset in the `data/` folder.
2. Open the `eda.ipynb` notebook.
3. Run cells sequentially to:
   - Conduct exploratory data analysis.
   - Generate visualizations like scatter plots, histograms, and wind roses.
   - Detect and handle outliers using Z-scores.
   - Analyze correlations and complex relationships.

---

### **Key Features**
- **Outlier Detection:** Z-score-based method to identify anomalous data points.
- **Bubble Charts:** Visualize multivariate relationships between solar and meteorological parameters.
- **Wind Roses:** Show the distribution of wind speed and direction.
- **Correlation Heatmaps:** Explore relationships between key weather variables.

---

### **Output**
- Cleaned data and reports exported to `data/processed/`.

---

### **Contributing**
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```
   git checkout -b feature-name
   ```
3. Commit your changes and push to the branch:
   ```
   git commit -m "Add feature-name"
   git push origin feature-name
   ```
4. Submit a pull request.

---

### **Contact**
For questions or collaboration, contact:  
**Sara Fedlu**  
**sfedlu28@gmail.com**
