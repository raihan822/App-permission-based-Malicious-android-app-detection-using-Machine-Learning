# 📱 Android App Permission-Based Malware Detection using Machine Learning

With the rapid proliferation of smartphones and Android’s dominant market share, the threat of malicious applications exploiting user data has significantly increased. This project presents a machine learning-based approach to **detect malicious Android apps based on their permissions**, offering a lightweight and efficient solution for real-world use.

## 🧠 Project Highlights

* **Focus:** Detecting malicious Android applications based on requested permissions.
* **Approach:** Feature selection techniques to reduce dimensionality and optimize model performance.
* **Algorithms Used:** XGBoost, Random Forest, and other traditional ML classifiers.
* **Interface:** User-friendly web app built with **Flask** for interactive malware detection.

---

## 🧾 Features

✅ Reduced feature set from **86 to 15** using:

* Variance Threshold
* Pearson Correlation
* Mutual Information Gain

✅ Achieved high accuracy while maintaining **low resource consumption**.

✅ Built a **Flask-based web interface** for practical usability.

✅ Suitable for both academic research and real-world deployment.

---

## 🗂️ Project Structure

```
├── WebApp/                     # Flask web app directory
│   ├── requirements.txt             # Python dependencies
│   ├── app/
│       ├── templates/               # HTML files
│       ├── static/                  # CSS, JS files
│       ├── model.pkl                # Trained ML model files
│       └── app.py                   # Flask main app
├── Dataset/                    # Dataset and processed features
├── (r)CSE445_Project.ipynb     # ML training and evaluation scripts
├── model.pkl                   # Trained ML model files
├── for manual Testing.xlsx     # Separate test set for manual input and test case
└── README.md                   # This file
```

---

## 🚀 How to Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/raihan822/App-permission-based-Malicious-android-app-detection-using-Machine-Learning.git
   cd App-permission-based-Malicious-android-app-detection-using-Machine-Learning
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application**

   ```bash
   cd app
   python app.py
   ```

5. **Open in browser**

   * Go to `http://127.0.0.1:5000` to use the interface.

---

## 📊 Machine Learning Techniques

* **Feature Selection:**
  Efficient reduction using:

  * Variance Threshold
  * Pearson Correlation
  * Mutual Information

* **Classification Models:**

  * Random Forest
  * XGBoost
  * Logistic Regression
  * Support Vector Machine (SVM)

* **Evaluation Metrics:**

  * Accuracy
  * Precision
  * Recall
  * F1-Score
  * Confusion Matrix

---

## 📁 Dataset

* Collected Android app permissions and corresponding malware/benign labels.
* Preprocessed and used for both feature engineering and model training.

> *Note: Dataset files are available in the `/Dataset` folder.*

---

## 📸 Screenshots

> *(will be added soon)*

---

## 📌 Future Work

* Integrate with Android mobile app for real-time detection.
* Use more dynamic analysis features (e.g., API calls, network behavior).
* Explore deep learning models for further performance gains.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change or improve.

---

## 📝 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 🙋‍♂️ Author

**Raihan Sarker**
🔗 [LinkedIn](https://www.linkedin.com/in/raihan82/) | 📫 Email: [raihansarker820@gmail.com](mailto:raihansarker820@gmail.com)
