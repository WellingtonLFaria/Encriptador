# Encriptador
Encriptador de mensagens feito com Python

## Como usar o Encriptador
[Arquivo de como usar o Encriptador](./src/teste.py)
```python
# Importando biblioteca
from encriptador import Encriptador

# Instanciando o Encriptador o parâmetro a ser informado é a seed de encriptação
encriptador = Encriptador(2)

# Mensagem a ser encriptada
msg = "Hello World"

# Encriptando mensagem
msg_encriptada = encriptador.encriptar(msg)

# Decriptando a mensagem
msg_decriptada = encriptador.decriptar(msg_encriptada)

print(msg_encriptada, msg_decriptada)
```