#!/usr/bin/env python
# coding: utf-8

# Gerador de jogos 'surpresinha' da  mega-sena

# In[178]:


import random
import secrets


# In[179]:


def gerar_jogos():
    random.seed()
    jogo = random.sample(range(1, 61), 6)
    jogo = sorted(jogo)
    output.insert(tk.END, f"{' --- '.join(map(str, jogo))}\n\n")


# In[180]:


def limpar():
    output.delete("1.0", tk.END)


# Janela para o gerador

# In[181]:


import tkinter as tk


# In[182]:


bg_janela="#eee8aa"
bg_button_gerar="#228b22"
bg_button_limpar="#ff2401"


# In[183]:


janela = tk.Tk()
janela.title("Gerador de Jogos da Mega-Sena")
janela.configure(bg=bg_janela)

botao_gerar = tk.Button(janela, height=1, width=25, text="Gerar",bg=bg_button_gerar, fg="white", command=gerar_jogos)
botao_gerar.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

output = tk.Text(janela, height=15, width=50)
output.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

botao_limpar = tk.Button(janela, height=1, width=25, text="Limpar", bg=bg_button_limpar, fg="white", command=limpar)
botao_limpar.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

janela.mainloop()

