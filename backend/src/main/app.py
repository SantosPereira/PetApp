from flask import app, Flask, make_response, request, render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def barra():
    resposta = make_response(
        jsonify(
            {
                'Status': '200'
            }
        )
    )
    resposta.headers['Access-Control-Allow-Origin'] = '*'
    return resposta


@app.route('/cadastrarusuario', methods=['GET','POST'])
def cadastrarUsuario():
    dados = request.form.get('nome')
    return jsonify(dados)


if __name__ == "__main__":
	app.run(host='localhost')