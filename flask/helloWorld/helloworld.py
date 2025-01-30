from flask import Flask  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #define the default route   
def home():  
    return "hello world!!";  
  
if __name__ =='__main__':  
    app.run(debug = True)  
#try hitting http://localhost:5000    