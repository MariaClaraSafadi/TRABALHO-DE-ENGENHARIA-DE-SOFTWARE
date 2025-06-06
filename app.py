from flask import Flask, render_template_string, request, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = 'chave-secreta-para-validacao'

class FormCadastro(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(message="Nome é obrigatório")])
    email = StringField('Email', validators=[
        DataRequired(message="Email é obrigatório"),
        Email(message="Email inválido")
    ])
    senha = PasswordField('Senha', validators=[
        DataRequired(message="Senha é obrigatória"),
        Length(min=6, message="A senha deve ter pelo menos 6 caracteres")
    ])
    enviar = SubmitField('Cadastrar')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FormCadastro()
    if form.validate_on_submit():
        flash(f'Usuário {form.nome.data} cadastrado com sucesso!', 'success')
        return redirect('/')
    return render_template_string(TEMPLATE, form=form)


TEMPLATE = '''
<!doctype html>
<title>Cadastro</title>
<h1>Cadastro de Usuário</h1>
<form method="POST">
  {{ form.hidden_tag() }}
  <p>
    {{ form.nome.label }}<br>
    {{ form.nome(size=32) }}<br>
    {% for erro in form.nome.errors %}
      <span style="color:red;">{{ erro }}</span>
    {% endfor %}
  </p>
  <p>
    {{ form.email.label }}<br>
    {{ form.email(size=32) }}<br>
    {% for erro in form.email.errors %}
      <span style="color:red;">{{ erro }}</span>
    {% endfor %}
  </p>
  <p>
    {{ form.senha.label }}<br>
    {{ form.senha(size=32) }}<br>
    {% for erro in form.senha.errors %}
      <span style="color:red;">{{ erro }}</span>
    {% endfor %}
  </p>
  <p>{{ form.enviar() }}</p>
</form>

{% with mensagens = get_flashed_messages(with_categories=true) %}
  {% if mensagens %}
    <ul>
    {% for categoria, mensagem in mensagens %}
      <li><strong>{{ mensagem }}</strong></li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
'''

if __name__ == '__main__':
    app.run(debug=True)
