# 🚗 Car Price Prediction — Streamlit ML App

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-yellow?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red?style=for-the-badge&logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-ML%20Model-orange?style=for-the-badge&logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-Data-150458?style=for-the-badge&logo=pandas)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A machine learning web app that predicts the resale price of used cars in India. Select your car brand, enter specs, and get an instant price estimate — with a dynamic background that changes per brand.**

[Features](#-features) · [How It Works](#-how-it-works) · [Installation](#-installation) · [Usage](#-usage) · [Dataset](#-dataset) · [Project Structure](#-project-structure)

</div>

---

## ✨ Features

- 🏎️ **30+ car brands** supported — Maruti, Hyundai, BMW, Audi, Tata, Mahindra, and more
- 🖼️ **Dynamic brand backgrounds** — the page background image changes to match the selected car brand
- 🤖 **ML-powered prediction** using a pre-trained model (`Model.pkl`)
- 💰 **Price output in Indian Rupees (₹)** with comma formatting
- 🎨 **Cinematic dark UI** with glowing red neon inputs, hover animations, and a fixed title bar
- 📋 **11 input features** covering all key factors that affect used car resale value

---

## 🧠 How It Works

The app uses a **supervised regression model** trained on a real-world Indian used car dataset:

1. **User selects** car brand, year, mileage, fuel type, transmission, owner type, and more
2. **Inputs are encoded** — categorical values are mapped to integers matching the training data encoding
3. **Model predicts** the resale price using the trained `Model.pkl` (Random Forest / Gradient Boosting)
4. **Result is displayed** as a large glowing price card

```
User fills inputs
        │
        ▼
Build input DataFrame with 11 features
        │
        ▼
Encode categorical columns
(brand → int, fuel → int, owner → int, etc.)
        │
        ▼
model.predict(input_data)
        │
        ▼
Display: ₹ Estimated Car Price
```

---

## 🧾 Input Features

| Feature | Type | Range / Options |
|---|---|---|
| Car Brand | Dropdown | 30+ brands (Maruti, BMW, Audi …) |
| Year of Manufacture | Number | 1994 – 2024 |
| Kilometres Driven | Number | 11 – 200,000 km |
| Fuel Type | Dropdown | Petrol, Diesel, CNG, LPG |
| Seller Type | Dropdown | Individual, Dealer, Trustmark Dealer |
| Transmission | Dropdown | Manual, Automatic |
| Owner Type | Dropdown | First, Second, Third, Fourth+ Owner |
| Mileage | Number | 10 – 40 km/l |
| Engine CC | Number | 700 – 5,000 CC |
| Max Power | Number | 0 – 200 bhp |
| Number of Seats | Number | 5 – 10 |

---

## 📂 Project Structure

```
car-price-prediction/
│
├── app.py                  # Main Streamlit application
│
├── Model.pkl               # Pre-trained ML regression model
├── Cars_datasets.csv       # Used car dataset (brand, fuel, transmission, price, etc.)
│
└── requirements.txt        # Python dependencies
```

---

## ⚙️ Installation

### Prerequisites
- Python 3.9 or higher

### 1. Clone the repository

```bash
git clone https://github.com/your-username/car-price-prediction.git
cd car-price-prediction
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`.

1. Select your **car brand** from the dropdown — the background changes to match
2. Fill in the remaining details (year, km driven, fuel, transmission, etc.)
3. Click **Predict Car Price**
4. The estimated resale value appears instantly in ₹

---

## 🗄️ Dataset

The model is trained on `Cars_datasets.csv`, an Indian used car dataset containing:

| Column | Description |
|---|---|
| `name` | Car brand + model name |
| `year` | Year of manufacture |
| `selling_price` | Target variable — actual resale price (₹) |
| `km_driven` | Total kilometres driven |
| `fuel` | Fuel type (Petrol / Diesel / CNG / LPG) |
| `seller_type` | Individual / Dealer / Trustmark Dealer |
| `transmission` | Manual / Automatic |
| `owner` | Owner history (First / Second / Third / Fourth+) |
| `mileage` | Fuel efficiency (km/l) |
| `engine` | Engine displacement (CC) |
| `max_power` | Maximum power output (bhp) |
| `seats` | Number of seats |

---

## 🛠️ Training the Model (Optional)

If you want to retrain the model from scratch:

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv('Cars_datasets.csv')

# Encode categorical columns
mappings = {
    'owner':        {'First Owner': 1, 'Second Owner': 2, 'Third Owner': 3, 'Fourth & Above Owner': 4, 'Test Drive Car': 5},
    'fuel':         {'Diesel': 1, 'Petrol': 2, 'LPG': 3, 'CNG': 4},
    'seller_type':  {'Individual': 1, 'Dealer': 2, 'Trustmark Dealer': 3},
    'transmission': {'Manual': 1, 'Automatic': 2},
}
for col, mapping in mappings.items():
    df[col] = df[col].replace(mapping)

# Encode brand
df['name'] = df['name'].apply(lambda x: x.split(' ')[0].strip())
brand_mapping = {brand: idx+1 for idx, brand in enumerate(df['name'].unique())}
df['name'] = df['name'].replace(brand_mapping)

features = ['name', 'year', 'km_driven', 'fuel', 'seller_type',
            'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats']

X = df[features]
y = df['selling_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

pickle.dump(model, open('Model.pkl', 'wb'))
print("Model saved!")
```

---

## 📦 Dependencies

```
streamlit
pandas
scikit-learn
```

Install all at once:

```bash
pip install streamlit pandas scikit-learn
```

---

## ⚠️ Notes

- Prices are predicted in **Indian Rupees (₹)** based on the Indian used car market dataset.
- The model accuracy depends on the training data — results are **estimates**, not guaranteed valuations.
- Background images are loaded from external URLs; an active internet connection is required for them to display.
- `.replace(..., inplace=True)` used in the app is deprecated in newer pandas versions — consider updating to `df[col] = df[col].replace(mapping)` for future compatibility.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

<div align="center">

*Built with ❤️ using Streamlit + scikit-learn · Indian Used Car Market Dataset*

</div>
