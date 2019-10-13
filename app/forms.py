from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField

class LoginForm(FlaskForm):
  username = StringField('Nombre de usuario')
  password = PasswordField('Password')
  submit = SubmitField('Enviar')

class TodoForm(FlaskForm):
  description = StringField('Descripción')
  submit = SubmitField('Crear')

class DeleteTodoForm(FlaskForm):
  submit = SubmitField('Borrar')

class UpdateTodoForm(FlaskForm):
  submit = SubmitField('Actualizar')