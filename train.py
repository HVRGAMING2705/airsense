import json, numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_predict, KFold
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

rng = np.random.default_rng(42)
n = 600
pm25 = rng.uniform(10, 300, n)       # ug/m3
pm10 = pm25 * rng.uniform(1.2, 2.0, n) + rng.uniform(0, 60, n)
no2 = rng.uniform(10, 120, n)        # ppb
o3 = rng.uniform(10, 100, n)         # ppb
temp = rng.uniform(5, 42, n)         # C
humidity = rng.uniform(20, 95, n)    # %
wind = rng.uniform(0, 30, n)         # km/h
# Generative AQI: particulates dominate, gases add, wind clears the air
y = (20 + 0.60 * pm25 + 0.20 * pm10 + 0.35 * no2 + 0.15 * o3
     - 0.8 * (wind - 10) + 0.15 * (humidity - 50) + rng.normal(0, 25, n))
y = np.clip(y, 20, 500)
X = np.column_stack([pm25, pm10, no2, o3, temp, humidity, wind])
names = ["pm25_ug_m3", "pm10_ug_m3", "no2_ppb", "o3_ppb", "temp_c", "humidity_pct", "wind_kmh"]
mu, sd = X.mean(0), X.std(0)
Xs = (X - mu) / sd
model = Ridge(alpha=1.0).fit(Xs, y)
kf = KFold(5, shuffle=True, random_state=42)
pred_cv = cross_val_predict(Ridge(alpha=1.0), Xs, y, cv=kf)
r2 = float(r2_score(y, pred_cv)); mae = float(mean_absolute_error(y, pred_cv))
rmse = float(np.sqrt(mean_squared_error(y, pred_cv)))
base_mae = float(mean_absolute_error(y, np.full(n, y.mean())))
print(f"CV R2={r2:.3f} MAE={mae:.2f} RMSE={rmse:.2f} baseline_MAE={base_mae:.2f} mean_AQI={y.mean():.1f}")
print("coef", model.coef_, "intercept", model.intercept_)
mj = {"features": names, "means": mu.tolist(), "stds": sd.tolist(),
      "coef": model.coef_.tolist(), "intercept": float(model.intercept_),
      "metrics": {"cv_r2": r2, "cv_mae": mae, "cv_rmse": rmse, "baseline_mae": base_mae, "mean_aqi": float(y.mean()), "n": n}}
with open("model.json", "w") as f: json.dump(mj, f, indent=1)

def predict(v):
    z = (np.array(v) - mu) / sd
    return float(model.intercept_ + z @ model.coef_)
samples = [[35, 70, 30, 40, 28, 55, 12], [180, 320, 90, 60, 30, 45, 3],
           [12, 25, 15, 30, 22, 60, 20], [250, 450, 110, 80, 33, 35, 2],
           [90, 170, 55, 50, 26, 50, 8]]
for s in samples: print(s, round(predict(s), 2))
