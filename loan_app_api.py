from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('result.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Extract form data
    gender = request.form.get('gender')
    married = request.form.get('married')
    applicant_income = request.form.get('applicant_income')
    loan_amount = request.form.get('loan_amount')
    credit_history = request.form.get('credit_history')
    
    # preprocess the request.json
    # import model from pickle 
    # [Gender, Married, ApplicantIncome, LoanAmount, Credit_History]
    # pass this feature to model ( model will return 1 = "approve" or 0 = "not approve")
    # "your loan application has been accepted/rejected"


    # Render the result HTML page with the submitted data
    return render_template('result.html',
                           gender=gender,
                           married=married,
                           applicant_income=applicant_income,
                           loan_amount=loan_amount,
                           credit_history=credit_history)



if __name__ == "__main__":
    app.run(debug = True)
