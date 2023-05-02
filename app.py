from flask import Flask, redirect, render_template, flash, request, url_for
import json
import requests
import os

from api.api import atualizar_clube, excluir_clube, get_clube_by_id, get_clubes, gravar_clube


app = Flask(__name__,
            template_folder="views",
            static_folder="src")
app.config['UPLOAD_FOLDER'] = 'src/img'
app.config["SECRET_KEY"] = 'secret'


@app.route('/')
def index():
    return render_template("index.html", request=request)


@app.route('/clubes')
def clubes():
    endpoint = '/clubes'
    clubes = get_clubes(endpoint)

    # flash('Uma mensagem flash')

    return render_template("index.html", clubes=clubes, request=request)


@app.route('/sobre')
def sobre():
    return render_template("index.html", request=request)
    # return render_template("sobre.html")


@app.route('/atualizar')
def atualizar():
    clube_id = request.args.get('clube_id')
    name = request.args.get('name')
    city = request.args.get('city')
    state = request.args.get('state')
    logo = request.args.get('logo')

    return render_template("index.html", clube_id=clube_id, name=name, city=city, state=state, logo=logo)


@app.route('/gravar', methods=['GET', 'POST'])
def post_data():
    clube_id = request.form.get('clube_id')
    name = request.form['name']
    city = request.form['city']
    state = request.form['state']

    logo = request.files['logo']
    filename = logo.filename
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    logo.save(filepath)
    logo_path = filename

    action = request.form.get('action')

    if not name or not city or not state or not logo_path:
        flash(message='Todos os campos devem ser preenchidos', category='danger')
        return redirect(url_for('atualizar'))

    data = {
        'name': name,
        'city': city,
        'state': state,
        'logo': logo_path
    }

    if action == 'criar':
        endpoint = '/clube-add'
        response = gravar_clube(endpoint, data)
    elif action == 'atualizar':
        endpoint = '/clube/'
        response = atualizar_clube(endpoint, clube_id, data)

    if response.status_code == 200:
        flash(message='Os dados foram salvos com sucesso!', category='success')
        return redirect(url_for('clubes'))
    else:
        return 'Erro ao gravar dados'


@app.route('/excluir/<int:id>', methods=['POST', 'DELETE'])
def excluir(id):
    clube = get_clube_by_id(id)
    response = excluir_clube(id)
    if response.status_code == 200:
        if 'logo' in clube:
            filename = clube['logo']
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            if os.path.isfile(filepath):
                os.remove(filepath)
            else:
                flash('Arquivo da imagem não encontrado', 'warning')
        flash('Clube excluído com sucesso!', 'success')
    else:
        flash('Erro ao excluir clube', 'danger')
    return redirect(url_for('clubes'))


if __name__ == '__main__':
    # mudei o port do front porque o back está usando a 5000
    app.run(port=5001, debug=True)
