from flask import Flask, render_template, request
from contextlib import suppress
import requests
import string



app = Flask(__name__)



@app.route('/')
def view():
   
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def calc():

    try:

        from_form = request.form['from']
        to_form = request.form['to']
        amt_form = request.form['amt']


        url = f"https://api.exchangerate.host/convert?from={from_form}&to={to_form}&amount={amt_form}"
        response = requests.get(url)
        data = response.json()

    

        

        

        
        amount = data['query']['amount'] 

        
    



        rate = data['info']['rate']

        
    
        test = amount * rate

       

       
        
        return render_template('valid.html', val=test)
    except:
        valid_cur_url = 'https://api.exchangerate.host/symbols'
        res2 = requests.get(valid_cur_url)
        data2 = res2.json()

        symb = data2['symbols']
        
        
        alph_low = string.ascii_lowercase

        

       

        lower = amt_form.lower()
        for lett in lower:
            if lett in alph_low:
                
                return "invalid amount"

        if to_form not in symb and from_form not in symb:
            
            
            return render_template('bad_all.html', fr=from_form, to=to_form)
     
        if to_form not in symb and from_form in symb:
            return render_template('bad_to.html', to=to_form)
        
       
        
        
             

    
            