# AirSense — Air Quality Index Predictor

A 2nd-year B.Tech AI/ML project by Vikranth Reddy (Woxsen University).

## What it does
Predicts the Air Quality Index (AQI) from PM2.5, PM10, nitrogen dioxide, ozone, temperature, humidity and wind speed, and explains the result with the standard AQI health category.

## Model
- Ridge regression (alpha = 1.0) on standardised features
- Trained on 600 synthetic city-days (seed 42)
- 5-fold cross-validation: R² = 0.908, MAE = 19.82, RMSE = 24.91
- Baseline (predict the mean): MAE = 69.99 — the model is ~3.5x better

## Files
- `train.py` — generates data, trains the model, writes `model.json`
- `model.json` — learned means, standard deviations, coefficients, intercept
- `index.html` — interactive demo; the browser runs the exact same weights as Python

## Live demo
https://airsense.vercel.app
