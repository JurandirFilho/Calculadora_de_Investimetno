from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import locale

# Defina a localidade para o pais
locale.setlocale(locale.LC_ALL,'pt-BR.UTF-8')

# cores ------------------

co0 = '#2e2d2b' # preta
co1 = '#feffff' # branca
co2 = '#4fa882' # verde
co3 = '#38576b' # valor
co4 = '#403d3d' 
co5 = '#F3E99F' # amarelo
co6 = '#03091f' # azul

janela = Tk()
janela.title('')
janela.geometry('400x350')
janela.configure(background=co1)
janela.resizable(width=False, height=False)

style = Style(janela)
style.theme_use('clam')

frameCima = Frame(janela, width=450, height=50, bg=co1, relief='flat')
frameCima.grid(row=0, column=0)

framePergunta = Frame(janela, width=450, height=100, bg=co1, relief='solid')
framePergunta.grid(row=1, column=0, padx=5, sticky=NSEW)

frameResultado = Frame(janela, width=300, height=310, bg='#4E6E81', relief='raised')
frameResultado.grid(row=3, column=0, sticky=NSEW)


frameDia = Frame(frameResultado, width=200, height=100, bg=co1, relief='solid')
frameDia.grid(row=0, column=0, padx=1, pady=1, sticky=NSEW)

frameSemana = Frame(frameResultado, width=200, height=100, bg=co1, relief='solid')
frameSemana.grid(row=0, column=1, padx=1, pady=1, sticky=NSEW)

frameMes = Frame(frameResultado, width=200, height=100, bg=co1, relief='solid')
frameMes.grid(row=1, column=0, padx=1, pady=1, sticky=NSEW)

frameToal = Frame(frameResultado, width=200, height=100, bg=co1, relief='solid')
frameToal.grid(row=1, column=1, padx=1, pady=1, sticky=NSEW)


#Logo-----------------

#abrindo imagem

app_img = Image.open('logo.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=' Caluladora de investimento', font=('Verdana 14'), width=350, compound=LEFT, padx=5, anchor=CENTER, bg=co1, fg=co0)
app_logo.place(x=5, y=0)

label_linha = Label(frameCima, font=('Verdana 1'), width=450, height=1, bg='#4E6881', fg=co1)
label_linha.place(x=0, y=48)


# Frame Pergunta ---------------------------

app_ = Label(framePergunta, text='Investimeto', font=('Verdana 10'), width=20, anchor=NW, bg=co1, fg=co0)
app_.place(x=50, y=15)
entry_valor = Entry(framePergunta, width=10, font=('Ivy 22'), justify='center', relief='solid', bg='#F3E99F', fg='#4E6881')
entry_valor.place(x=5, y=50)

app_ = Label(framePergunta, text='Dias*', font=('Verdana 10'), width=10, anchor=NW, bg=co1, fg=co0)
app_.place(x=200, y=15)
entry_valor_dias = Entry(framePergunta, width=5, font=('Ivy 22'), justify='center', relief='solid', bg='#F3E99F', fg='#4E6881')
entry_valor_dias.place(x=174, y=50)

app_ = Label(framePergunta, text='Percentual %', font=('Verdana 10'), width=13, anchor=CENTER, bg=co1, fg=co0)
app_.place(x=260, y=15)
entry_valor_Percentual = Entry(framePergunta, width=5, font=('Ivy 22'), justify='center', relief='solid', bg='#F3E99F', fg='#4E6881')
entry_valor_Percentual.place(x=270, y=50)


#função para calcular -----------------------

# criando função para calcular
def calcular_lucro(envento):
    try:
        investimento_inicial = float(entry_valor.get())
        dias_de_investimento = int(entry_valor_dias.get())
        retorno_garantido = float(entry_valor_Percentual.get())
        
        retorno_diario = retorno_garantido / 100 / dias_de_investimento
        
        lucro_diario = investimento_inicial * retorno_diario
        lucro_semanal = lucro_diario * 7
        lucro_mensal = lucro_diario * 30
        lucro_total = investimento_inicial *(1 + retorno_garantido / 100)
        
        app_dia['text'] = locale.currency(lucro_diario, symbol=True, grouping=True)
        app_semana['text'] = locale.currency(lucro_semanal, symbol=True, grouping=True)
        app_mes['text'] = locale.currency(lucro_mensal, symbol=True, grouping=True)
        app_total['text'] = locale.currency(lucro_total, symbol=True, grouping=True)
 
        
    except ValueError as e:
        pass

# Frame Resultado----------------------------

# Diario
app_ = Label(frameDia, text='Lucro Diario', font=('Verdana 11'), width=15, anchor=CENTER, bg=co1, fg='#4E6881')
app_.place(x=20, y=7)

app_dia = Label(frameDia, text='', font=('Verdana 15'), width=10, anchor=CENTER, bg=co1, fg=co0)
app_dia.place(x=20, y=35)


# Semanal
app_ = Label(frameSemana, text='Lucro Semanal', font=('Verdana 11'), width=15, anchor=CENTER, bg=co1, fg='#4E6881')
app_.place(x=20, y=7)

app_semana = Label(frameSemana, text='', font=('Verdana 15'), width=10, anchor=CENTER, bg=co1, fg=co0)
app_semana.place(x=20, y=35)

# Mensal
app_ = Label(frameMes, text='Lucro Mensal', font=('Verdana 11'), width=15, anchor=CENTER, bg=co1, fg='#4E6881')
app_.place(x=20, y=7)

app_mes = Label(frameMes, text='', font=('Verdana 15'), width=10, anchor=CENTER, bg=co1, fg=co0)
app_mes.place(x=20, y=35)

# Total
app_ = Label(frameToal, text='Lucro Total', font=('Verdana 11'), width=15, anchor=CENTER, bg=co1, fg='#4E6881')
app_.place(x=20, y=7)

app_total = Label(frameToal, text='', font=('Verdana 15'), width=10, anchor=CENTER, bg=co1, fg=co0)
app_total.place(x=20, y=35)


# Vincule o eventeo KeyRelease ao widget Entry e came a funçao calcular_lucro
entry_valor.bind('<KeyRelease>', calcular_lucro)
entry_valor_dias.bind('<KeyRelease>', calcular_lucro)
entry_valor_Percentual.bind('<KeyRelease>', calcular_lucro)


janela.mainloop()