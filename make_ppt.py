from pptx import Presentation
from pptx.util import Inches, Pt
prs = Presentation(); prs.slide_width = Inches(13.33); prs.slide_height = Inches(7.5)
def add(i, title, lines):
    s = prs.slides.add_slide(prs.slide_layouts[1])
    s.shapes.title.text = title
    tf = s.placeholders[1].text_frame; tf.word_wrap = True
    for j, ln in enumerate(lines):
        p = tf.paragraphs[0] if j == 0 else tf.add_paragraph()
        p.text = ln; p.font.size = Pt(20); p.space_after = Pt(10)
add(0, "AirSense — Air Quality Index Predictor", ["An AI/ML project by Vikranth Reddy", "B.Tech CSE (AI & ML), 2nd Year — Woxsen University", "Ridge regression that estimates the Air Quality Index right in your browser"])
add(1, "The Problem", ["Air pollution changes every day, but most people only hear a single AQI number", "That number depends on several pollutants and the weather together", "Checking separate pollutant readings does not tell you the overall air quality", "A simple, explainable estimate turns raw readings into a clear health message"])
add(2, "The Solution — AirSense", ["Enter PM2.5, PM10, NO2, ozone, temperature, humidity and wind speed", "A trained ridge regression model predicts the Air Quality Index", "The result also shows the standard AQI health category, from Good to Hazardous", "Runs fully in the browser — no backend, no waiting"])
add(3, "Tech Stack", ["Python + scikit-learn: data generation and model training", "Ridge regression (alpha = 1.0) on standardised features", "HTML, CSS and vanilla JavaScript for the interactive demo", "GitHub for source control, Vercel for free hosting"])
add(4, "Architecture", ["Synthetic dataset: 600 city-days, 7 features, seed 42", "Standardisation (mean / std) -> Ridge regression -> model.json", "model.json ships with the site; JavaScript applies the same formula", "Prediction is clipped to a realistic 20–500 AQI range, then mapped to a health category"])
add(5, "Live Demo", ["Try it: enter today's pollutant and weather readings and press Estimate", "Example: PM2.5 180, PM10 320, NO2 90, O3 60, 30 C, 45% humidity, 3 km/h wind -> about 238 AQI (Unhealthy)", "Change any input and the estimate updates instantly", "Demo: https://airsense.vercel.app"])
add(6, "Results", ["5-fold cross-validation R-squared: 0.908", "Mean absolute error: 19.82 AQI points (RMSE 24.91)", "Baseline (always guessing the average): MAE 69.99", "The model is about 3.5x better than the baseline guess", "Browser demo matches Python predictions to within 0.01 AQI points"])
add(7, "Future Scope", ["Train on real city data from government open air-quality datasets", "Add a city selector with live sensor readings", "Compare gradient boosting and small neural networks", "Add a 24-hour AQI forecast and a health-tips panel per category"])
add(8, "Thank You", ["AirSense — Air Quality Index Predictor", "Vikranth Reddy, B.Tech CSE (AI & ML), Woxsen University", "Source: github.com/HVRGAMING2705/airsense", "Questions welcome!"])
prs.save("/home/hatch/workspace/goals/daily-ai-ml-project-factory/files/AIML_AirSense_2026-11-01.pptx")
print("slides:", len(prs.slides._sldIdLst))
