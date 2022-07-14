from flask import Flask, render_template, url_for
import funçõesDHT as dht
app = Flask(__name__)

dht.inicializar(4)

@app.route('/')
def home():
    umidade, temperatura = dht.lerDHT()
    return render_template('index.html', umid=umidade, temp=temperatura)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

