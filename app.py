#!/usr/bin/env python
# coding: utf-8

# In[5]:


from flask import Flask


# In[6]:


app = Flask(__name__)


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[7]:


from flask import render_template, request
import joblib

@app.route("/", methods = ["GET","POST"])

def index():
    if request.method == "POST":
        purchases = request.form.get("purchases")
        suppcard = request.form.get("suppcard")
        
        purchases = float(purchases)
        suppcard = float(suppcard)
        print(purchases, suppcard)
        
        model1 = joblib.load("CCU_DT")
        pred1 = model1.predict([[purchases, suppcard]])
        str1 = "The score of credit card upgrade based on decision tree is" + str(pred1)
        
        model2 = joblib.load("CCU_Reg")
        pred2 = model2.predict([[purchases, suppcard]])
        str2 = "The score of credit card upgrade based on regression is" + str(pred2)
        
        model3 = joblib.load("CCU_NN")
        pred3 = model3.predict([[purchases, suppcard]])
        str3 = "The score of credit card upgrade based on neural network is" + str(pred3)
        
        model4 = joblib.load("CCU_RF")
        pred4 = model4.predict([[purchases, suppcard]])
        str4 = "The score of credit card upgrade based on random forest is" + str(pred4)
        
        model5 = joblib.load("CCU_GB")
        pred5 = model5.predict([[purchases, suppcard]])
        str5 = "The score of credit card upgrade based on gradient boosting is" + str(pred5)
        
        return(render_template("index.html", result1 = str1,result2 = str2,result3 = str3,result4 = str4,result5 = str5))
    
    else:
        return(render_template("index.html", result1 = "2",result2 = "2",result3 = "2",result4 = "2",result5 = "2"))


# In[ ]:





# In[ ]:




