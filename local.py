from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   import time
   from datetime import datetime as dat

   # change hosts path according to your OS
   hosts_path = "C:\Windows\System32\Drivers\etc\hosts"
   # localhost's IP
   localIP = "127.0.0.1"
   website_list = [name]

   while True:
       if dat(dat.now().year, dat.now().month, dat.now().day, 1) < dat.now() < dat(dat.now().year, dat.now().month,
                                                                              dat.now().day, 11):
           print("Process Executed...")
           with open(hosts_path, 'r+') as file:
               content = file.read()
               for website in website_list:
                   if website in content:
                       pass
                   else:
                       file.write(localIP + " " + website + "\n")
       else:
           with open(hosts_path, 'r+') as file:
               content = file.readlines()
               file.seek(0)
               for line in content:
                   if not any(website in line for website in website_list):
                       file.write(line)
                       # removing hostnmes from host file
                       file.truncate()
           print("Process not executing...")
       time.sleep(5)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)