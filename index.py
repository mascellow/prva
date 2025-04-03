import customtkinter as ctk

ctk.set_appearance_mode('Dark')

janela = ctk.CTk('#712b7d')
janela.geometry('400x300')
janela.resizable(False,False)
janela.title('Sistema de Acesso 2025')

ctk.CTkLabel(janela,text='Sistema de Acesso',
             font=('Roboto',30,'bold'),
             text_color='whitesmoke').pack(pady=(20))

login = ctk.CTkEntry(janela,
                     width=250,
                     height=30,
                     placeholder_text='Digite o seu login',
                     font=('Roboto',15))
password = ctk.CTkEntry(janela,
                        width=250,
                        height=30,
                        placeholder_text='Digite o seu senha',
                        show='•',
                        font=('Roboto',15))

login.pack(pady=(20))
password.pack(pady=(10))

botao = ctk.CTkButton(janela,
                      width=80,
                      height=30,
                      fg_color='#321b37',
                      text_color='whitesmoke',
                      text='Login',
                      font=('Roboto',15,'bold'),
                      hover_color='#0e0019')

botao.pack(pady=(20))
janela.mainloop()