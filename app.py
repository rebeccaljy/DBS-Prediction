#!/usr/bin/env python
# coding: utf-8

# # Import packages and files

# In[25]:


from flask import Flask, render_template, request
import joblib


# # Checking functions in packages/files

# In[3]:


dir(Flask)


# In[4]:


__name__


# # App backend

# In[26]:


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        print(rate)
        model = joblib.load("DBS_Prediction")
        pred = model.predict([[rate]])
        return(render_template("index.html", result=pred))
    else:
        return(render_template("index.html", result="waiting"))


# In[ ]:


# making sure that you're the one writing the app
if __name__ == "__main__":
    app.run()


# In[ ]:




