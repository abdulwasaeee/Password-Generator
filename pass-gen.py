from flask import Flask,render_template,jsonify
import random

app= Flask(__name__)

def generate_password():
 #adding lowercase letters
 lc1=chr(random.randint(97,122))
 lc2=chr(random.randint(97,122))
 lc3=chr(random.randint(97,122))

 #adding numbers
 n1=chr(random.randint(48,57))
 n2=chr(random.randint(48,57))
 n3=chr(random.randint(48,57))

 #adding uppercase letters
 uc1=chr(random.randint(65,90))
 uc2=chr(random.randint(65,90))

 #adding symbols
 s1=chr(random.randint(33,47))
 s2=chr(random.randint(33,47))

 list=[lc1,lc2,lc3,n1,n2,n3,uc1,uc2,s1,s2]

 random.shuffle(list)

 password=''.join(list)

 return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password')
def password():
    password=generate_password()
    return jsonify(p=password)

if __name__ == '__main__':
    app.run(debug=True)





