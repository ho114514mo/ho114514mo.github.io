from flask import Flask, render_template,request,redirect,jsonify
app=Flask(__name__,template_folder='./templates/',static_folder='',static_url_path='')
@app.route("/main.html")
def rrrrr():
    return render_template("main.html")
@app.route("/")
def rrrr():
    
    return render_template("main.html")
@app.route("/个人主页.html")
def rrr():
    return render_template("个人主页.html")
@app.route("/登陆.html")
def rr():
    password=str(request.args.get('password'))
    name=str(request.args.get('name'))
    if name=='None' and password=='None':   
        return render_template("登陆.html")
    else:
        f=open('./data/user.json','r')
        user=eval(f.read())
        f.close()
        
        if(name in user):
            if(user[name]==password):
                return "1"
            return "2"
        if len(password)<6:
            return "4"
        user[name]=password
        user=str(user)
        while("'"in user):
            k=user.find("'")
            user=user[:k]+'"'+user[k+1:]
        f=open("./data/user.json",'w')
        f.write(str(user))
        f.close()
        return "3"
        #return str(f'name:{name}\npassword:{password}')
    
@app.route("/text/关于编写html的感想/__init__.html")
def r():
    return render_template("text/关于编写html的感想/__init__.html")
app.run(port='8000',host='127.0.0.1',debug=True)