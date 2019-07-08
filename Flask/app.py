from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import xlrd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/result',methods=['POST','GET'])
def result():
    reg_no = request.form['reg_no']
    loc = (r"6thSem_BR_2016-20.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    x = -1
    for i in range(1,sheet.nrows-1):
        if int(reg_no) == int(sheet.cell_value(i, 1)):
            x = i
            break
    if x == -1:
        return render_template('login.html')
    else:
        index = sheet.row_values(0)
        answer = sheet.row_values(x)
        return render_template("result.html",answer=answer,index=index)

if __name__ == "__main__":
    app.run(debug=True)
