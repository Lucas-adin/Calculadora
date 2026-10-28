from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calcular', methods=['POST'])
def calcular():

    dados = int(request.form['dados'])
    transparencia = int(request.form['transparencia'])
    vies = int(request.form['vies'])
    seguranca = int(request.form['seguranca'])
    supervisao = int(request.form['supervisao'])

    total = dados + transparencia + vies + seguranca + supervisao

    if total <= 6:
        nivel = 'BAIXO 🟢'
        recomendacao = 'O sistema apresenta baixo risco ético.'

    elif total <= 13:
        nivel = 'MÉDIO 🟡'
        recomendacao = 'Existem pontos que precisam ser revisados.'

    else:
        nivel = 'ALTO 🔴'
        recomendacao = 'O sistema possui riscos éticos elevados.'

    return render_template(
        'index.html',
        resultado=total,
        nivel=nivel,
        recomendacao=recomendacao
    )


if __name__ == '__main__':
    app.run(debug=True)

    from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calcular', methods=['POST'])
def calcular():

    dados = int(request.form['dados'])
    transparencia = int(request.form['transparencia'])
    vies = int(request.form['vies'])
    seguranca = int(request.form['seguranca'])
    supervisao = int(request.form['supervisao'])

    total = dados + transparencia + vies + seguranca + supervisao

    if total <= 6:
        nivel = 'BAIXO 🟢'
        recomendacao = 'O sistema apresenta baixo risco ético.'

    elif total <= 13:
        nivel = 'MÉDIO 🟡'
        recomendacao = 'Existem pontos que precisam ser revisados.'

    else:
        nivel = 'ALTO 🔴'
        recomendacao = 'O sistema possui riscos éticos elevados.'

    return render_template(
        'index.html',
        resultado=total,
        nivel=nivel,
        recomendacao=recomendacao
    )


if __name__ == '__main__':
    app.run(debug=True)
