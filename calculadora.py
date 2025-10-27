from tkinter import *
from tkinter import ttk
import ast
import operator

# Cores
cor1 = '#1f1d1d'
cor2 = '#feffff'
cor3 = '#38576b'
cor4 = '#ECEFF1'
cor5 = '#FFAB40'

# Frames
janela = Tk()
janela.title('Calculadora')
janela.geometry('300x337')
janela.config(bg=cor1)

frame_tela = Frame(janela, width=300, height=80, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=300, height=255)
frame_corpo.grid(row=1, column=0)

# Variáveis
todos_valores = ''
valor_texto = StringVar()

# ----------------- Função segura de cálculo -----------------
_OPERACOES = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

def calcular_expressao(expr: str):
    if not expr:
        raise ValueError("Expressão vazia")

    try:
        arvore = ast.parse(expr, mode='eval')
    except Exception:
        raise ValueError("Erro de sintaxe")

    def _avaliar(no):
        if isinstance(no, ast.Expression):
            return _avaliar(no.body)

        elif isinstance(no, ast.BinOp):
            op_tipo = type(no.op)
            if op_tipo not in _OPERACOES:
                raise ValueError("Operação não permitida")
            left = _avaliar(no.left)
            right = _avaliar(no.right)
            if op_tipo is ast.Div and right == 0:
                raise ValueError("Divisão por zero")
            return _OPERACOES[op_tipo](left, right)

        elif isinstance(no, ast.UnaryOp):
            op_tipo = type(no.op)
            if op_tipo not in _OPERACOES:
                raise ValueError("Operação unária não permitida")
            return _OPERACOES[op_tipo](_avaliar(no.operand))

        elif isinstance(no, ast.Constant):  # Python 3.8+
            if isinstance(no.value, (int, float)):
                return no.value
            raise ValueError("Constante inválida")
        
        else:
            raise ValueError("Expressão inválida")

    return _avaliar(arvore)

# ----------------- Funções da interface -----------------
def entrada_valores(evento):
    global todos_valores
    todos_valores += str(evento)
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    try:
        resultado = calcular_expressao(todos_valores)
        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado)
        valor_texto.set(str(resultado))
        todos_valores = str(resultado)
    except Exception:
        valor_texto.set("Erro")
        todos_valores = ""

def limpar():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# ----------------- Interface -----------------
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2,
                  padx=7, relief=FLAT, anchor='e', justify=RIGHT,
                  font=('Ivy 23'), bg=cor3)
app_label.place(x=0, y=0)

# Botões
b1 = Button(frame_corpo, command=limpar, text='C', width=16, height=2, bg=cor4,
            font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(frame_corpo, command=lambda: entrada_valores('%'), text='%', width=7, height=2, bg=cor4,
            font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=150, y=0)
b3 = Button(frame_corpo, command=lambda: entrada_valores('/'), text='/', width=7, height=2, bg=cor5,
            font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=227, y=0)

b4 = Button(frame_corpo, command=lambda: entrada_valores('7'), text='7', width=7, height=2, bg=cor4,
            font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=52)
b5 = Button(frame_corpo, command=lambda: entrada_valores('8'), text='8', width=7, height=2, bg=cor4,
            font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=76, y=52)
b6 = Button(frame_corpo, command=lambda: entrada_valores('9'), text='9', width=7, height=2, bg=cor4,
            font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=150, y=52)
b7 = Button(frame_corpo, command=lambda: entrada_valores('*'), text='*', width=7, height=2, bg=cor5,
            font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=227, y=52)

b8 = Button(frame_corpo, command=lambda: entrada_valores('4'), text='4', width=7, height=2, bg=cor4,
            font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=104)
b9 = Button(frame_corpo, command=lambda: entrada_valores('5'), text='5', width=7, height=2, bg=cor4,
            font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=76, y=104)
b10 = Button(frame_corpo, command=lambda: entrada_valores('6'), text='6', width=7, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=150, y=104)
b11 = Button(frame_corpo, command=lambda: entrada_valores('-'), text='-', width=7, height=2, bg=cor5,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=227, y=104)

b12 = Button(frame_corpo, command=lambda: entrada_valores('1'), text='1', width=7, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=156)
b13 = Button(frame_corpo, command=lambda: entrada_valores('2'), text='2', width=7, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=76, y=156)
b14 = Button(frame_corpo, command=lambda: entrada_valores('3'), text='3', width=7, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=150, y=156)
b15 = Button(frame_corpo, command=lambda: entrada_valores('+'), text='+', width=7, height=2, bg=cor5,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=227, y=156)

b16 = Button(frame_corpo, command=lambda: entrada_valores('0'), text='0', width=16, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=208)
b17 = Button(frame_corpo, command=lambda: entrada_valores('.'), text='.', width=7, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=150, y=208)
b18 = Button(frame_corpo, command=calcular, text='=', width=7, height=2, bg=cor5,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=227, y=208)

janela.mainloop()
