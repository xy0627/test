from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)


@app.route("/")
@app.route("/hello")
# def hello():
#     return "Hello world! This is a web application by Flask."
def hello():
    #return render_template("index.html")
    return """
    <!DOCTYPE html>
<html>
    <body>
        <h2>输入两个数求和</h2>
        <form method='post'  action='/add'>
         <table>
          <p>使用表单计算两个数的和</p>
          <tr><td>被加数</td><td><input type='text' name='n1'  /></td></tr>
          <tr><td>加数</td><td><input type='text' name='n2'  /></td></tr>
         </table>
         <button name="sum" type="submit" value="sum">求和</button>
        </form>
    </body>
</html>

    """


@app.route("/add", methods=['GET', 'POST'])
def add():
    n1 = int(request.form['n1'])
    n2 = int(request.form['n2'])
    n3 = n1 + n2
    return render_template("add.html", n1=n1, n2=n2, n3=n3)
#     return """
#     <!DOCTYPE html>
# <html>
#     <body>
#         <h2>输入两个数求和</h2>
#         <form method='get'  action='/hello'>
#          <table>
#           <p>使用表单计算两个数的和</p>
#           <tr><td>被加数</td><td><input type='text' name='n1' value = """+str(n1)+""" /></td></tr>
#          <tr><td>加数</td><td><input type='text' name='n2' value = """+str(n2)+""" /></td></tr>
#          <tr><td>和</td><td><input type='text' name='n3'  value= """+str(n3)+""" /></td></tr>
#          </table>
#          <button name="return" type="submit" value="return">home</button>
#         </form>
#     </body>
# </html>
#     """

if __name__ == "__main__":
    app.run()
