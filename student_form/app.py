from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def Student():
    return render_template('student.html')

@app.route('/result',methods=['POST'])
def Result():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html',result=result)

if __name__ =='__main__':
    app.run()