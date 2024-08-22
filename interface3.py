import tkinter as tk # Importa a biblioteca Tkinter para a criação da interface gráfica
import math # Importa a biblioteca math para realizar operações matemáticas
from PIL import Image, ImageTk # Importa as classes Image e ImageTk da biblioteca PIL para manipulação de imagens 
import os # Importa a biblioteca os para operações com o sistema de arquivos
import sys # Importa a biblioteca sys para manipulação de variáveis e funções do sistema 

def resource_path(relative_path):
    """
    Obtém o caminho absoluto para o recurso, funciona tanto em ambiente de desenvolvimento quanto após o empacotamento com PyInstaller.
    
    """
    try:
        # PyInstaller cria um diretório temporário e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception :
        # Se não estiver executando pelo PyInstaller, utiliza o caminho absoluto do diretório atual
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path) # Retorna o caminho completo do arquivo

def calcular ():
    """
    Realiza o calculo dos valores trionométricos (seno,cosseno e tangente) do angulo fornecido e atualiza as labels com os resultados.
    """
    try:
        angulo = float(entrada_angulo.get()) # Obtem o valor do angulo inserido pelo usuario
        radiano = math.radians(angulo) # Converte o angulo de graus para radianos

        # Calcula os valores trigonométricas
        seno = math.sin(radiano)
        cosseno = math.cos(radiano)
        tangente = math.tan(radiano)
        #Atualiza as labels com os resultados formatados com 3 casa decimais 
        resultado_seno.config(text=f"{seno:.3f}")
        resultado_cosseno.config(text=f"{cosseno:.3f}")
        resultado_seno.config(text=f"{tangente:.3f}")
    except ValueError: 
        #Em caso de erro (por exemplo, entrada inválida), exibe "Erro" nas labels 
        resultado_seno.config(text="Erro")
        resultado_cosseno.config(text="Erro")
        resultado_tangente.config(text="Erro")
def limpar():
    """
    Valida a entrada do usuário permitindo apenas numeros e garantindo que o valor esteja entre 0 e 90.
    """
    if texto.isdigit() or texto == "": # Permite apenas números ou campo vazio
        if texto == "": # Se o campo estiver vazio, permite a entrada
            return True 
        valor = int(texto) # Converte o texto para inteiro
        return 0 <= valor <= 90 # Retorna True se o valor estiver entre 0 e 90, caso contrário false
    return False # Se o texto não for um número, retorna False

# Configuração de janela principal
janela = tk.Tk() # Cria a janela principal
janela.title("Claculadora Trigonométrica") # Define o titulo da janela
janela.geometry("400x500") # Define o tamanho da janela
janela.configure(bg="#f0f0f0") # Define a cor de fundo da janela

# Carregar e definir o ícone da janela
try:
    icone_path = resource_path("seno.png") # Obtem o caminho da imagem do ícone
    icone = Image.open(icone_path) # Abre a imagem do ícone
    icone = ImageTk.PhotoImage(icone) # Converte a imagem para um formato compativel com Tkinter
    janela.iconphoto(True, icone) # Define a imagem como ícone da janela
except FileNotFoundError:
    print("Imagem 'seno.png' não encontrada para o icone") # Cao o arquivo não seja encontrado, exibir mensagem de erro 

# Imagem seno2.png
try:
    imagem_path = resource_path("seno2.png") # Obtém o caminho da imagem principal
    imagem = Image.open(imagem_path) # Abre a imagem 
    imagem = imagem.resize((380,200), Image.LANCZOS) # Redimenciona a imagem 
    foto = ImageTk.PhotoImage(imagem) # Converte a imagem para um formato compativel com Tkinter
    label_imagem = tk.Label(janela, image=foto, bg="#f0f0f0", borderwidth=0)
    label_image = foto # Mantem uma referencia da imagem para evitar que o garbage collector a remova
    label_imagem.pack(pady=20) # Posiciona a imaegm ba janela
except FileNotFoundError: 
    # Caso a imagem não seja encontrada, exibe uma mensagem de texto no lugar da imagem 
    label_imagem = tk.Label(janela, text="imagem 'seno2.png' não encontrada", bg="#f0f0f0")
    label_imagem.pack(pady=20)

    # Entrada do angulo 
    frame_entrada = tk.Frame(janela, bg="#f0f0f0") # Cria um frame para organizar a entrada
    frame_entrada.pack(pady=10) # Posiciona o frame na janela com um espaçamento vertical

    label_angulo = tk.Label(frame_entrada, text="Angulo (0 a 90):", font=('Arial,14'), bg="#f0f0f0 ")
    label_angulo.pack(pady=(0, 5)) # Posiciona o label com um pequeno espaçamento inferior

    validacao = janela.register(validar_entrada) # Registra a função de validação para a entrada
    entrada_angulo = tk.Entry(frame_entrada, width=3, justify='center', font=('Arial', 16), bd=0, highlightthickness=0, relief="flat", bg="#f0f0f0", fg='red',
                              validate="key", validatecommand=(validacao, '%')) # Cria o campo de angulo
    entrada_angulo.pack() # Posiciona o campo de entrada

    # Linha abaixo do campo de entrada 
    linha = tk.Frame(frame_entrada, bg="black", height=1, width=entrada_angulo.winfo_reqheight()) # decorativa abaixo do campo de entrada
    linha.pack(pack=(0, 5)) # Posiciona a linha com um pequeno espaçamento inferior



