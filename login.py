from PySimpleGUI import PySimpleGUI as sg

# layout
sg.theme('Reddit')
layout = [
  [sg.Text('Usuário'),sg.Input(key='usuario'.lower())],
  [sg.Text('Senha'),sg.Input(key='senha',password_char='*')],
  [sg.Checkbox('Salvar o login?')],
  [sg.Button('Entrar')]
]
# Janela
janela = sg.Window('Tela de Login', layout)
# Ler os eventos
while True:
  eventos, valores = janela.read()
  if eventos == sg.WINDOW_CLOSED:
    break
  if eventos == 'Entrar':
    if valores['usuario'] == 'Lima' and valores['senha'] == '12345':
      print('Bem-vindo a Calculadora de IMC')