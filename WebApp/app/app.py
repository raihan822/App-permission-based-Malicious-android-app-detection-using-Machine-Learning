from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Feature names for the radio buttons
feature_names = [
    "BROADCAST_BADGE", "WRITE_SETTINGS", "READ_GSERVICES",
    "GET_TASKS", "INSTALL_SHORTCUT", "READ_PHONE_STATE", 
    "ACCESS_WIFI_STATE", "RECEIVE", "SEND_SMS", 
    "RESTART_PACKAGES","ACCESS_COARSE_LOCATION", "SYSTEM_ALERT_WINDOW", 
    "READ_CONTACTS", "BILLING", "RECEIVE_BOOT_COMPLETED"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        inputs = [int(request.form[col]) for col in feature_names]
        inputs = np.array(inputs).reshape(1, -1)
        prediction = model.predict(inputs)[0]
        result = "Malicious App" if prediction == 1 else "Benign App"

    return render_template('index.html', result=result, feature_names=feature_names)

if __name__ == '__main__':
    app.run(debug=True)
