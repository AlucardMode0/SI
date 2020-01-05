import pigpio
pi = pigpio.pi()
G=2
D=3

from flask import Flask,  request, render_template,redirect
app = Flask(__name__)


@app.route('/', methods=['POST'])
def post():
    str = request.form['degree1']

    print(str,str2)
    pi.set_servo_pulsewidth(G,int(100/9*int(str)+500))

    return render_template("index.html",error=str,error1=str2)

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0')
    except KeyboardInterrupt:
        #raise
        pi.set_servo_pulsewidth(G,0)
        pi.set_servo_pulsewidth(D,0)
        pi.stop()
