from flask import Flask, request, jsonify,render_template
import pickle

app = Flask(__name__)
model_pickel = open("classifier.pkl", "rb")
clf = pickle.load(model_pickel)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()

    gender = data.get('Gender')
    married = data.get('Married')
    applicant_income = data.get('ApplicantIncome')
    loan_amount = data.get('LoanAmount')
    credit_history = data.get('Credit_History')

    input_lis = []
    
    if gender == "Male":
        input_lis.append(1)
    else:
        input_lis.append(0)
    
    if married == "Yes":
        input_lis.append(1)
    else:
        input_lis.append(0)
    
    input_lis.append(int(applicant_income))
    input_lis.append(int(loan_amount))
    input_lis.append(int(credit_history))

    result = clf.predict([input_lis])
    print("debug 0 ", result)

    if result == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return jsonify({'message': f'Your loan application has been {pred}'})

if __name__ == '__main__':
    app.run(debug=True)
