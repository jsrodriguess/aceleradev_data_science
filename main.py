#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[72]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[3]:


black_friday.shape


# In[5]:


black_friday.columns


# In[6]:


black_friday.head()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[4]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[53]:


black_friday.groupby('Gender')['Age'].value_counts()


# In[54]:


q2 = pd.DataFrame(black_friday.groupby('Gender')['Age'].value_counts())
q2['Age'][0]


# In[5]:


def q2():
    # Retorne aqui o resultado da questão 2.
    q2 = pd.DataFrame(black_friday.groupby('Gender')['Age'].value_counts())
    return int(q2['Age'][0])


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[6]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return len(black_friday.User_ID.unique())


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return len(black_friday.dtypes.unique())


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[35]:


black_friday.isna().sum().sum()


# In[91]:


black_friday.isna().sum() / black_friday.shape[0]


# In[114]:


(black_friday.isna().sum() / black_friday.shape[0]).max()


# In[93]:


def q5():
    # Retorne aqui o resultado da questão 5.
    return float((black_friday.isna().sum() / black_friday.shape[0]).max())


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[38]:


black_friday.isna().sum()


# In[39]:


black_friday.isna().sum().max()


# In[9]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return black_friday.isna().sum().max()


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[40]:


black_friday.Product_Category_3.value_counts()


# In[43]:


black_friday.Product_Category_3.isna().sum()


# In[41]:


black_friday.Product_Category_3.value_counts().sum()


# In[52]:


black_friday.Product_Category_3.mode()[0]


# In[10]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return black_friday.Product_Category_3.mode()[0]


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[58]:


black_friday['Purchase'].mean()


# In[65]:


black_friday_copia = black_friday
normalized_df=(black_friday_copia['Purchase']-black_friday_copia['Purchase'].min())/(black_friday_copia['Purchase'].max()-black_friday_copia['Purchase'].min())


# In[68]:


normalized_df.mean()


# In[71]:


def q8():
    # Retorne aqui o resultado da questão 8.
    purchase_normalized = (black_friday['Purchase']-black_friday['Purchase'].min())/(black_friday['Purchase'].max()-black_friday['Purchase'].min())
    return purchase_normalized.mean()


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[81]:


padronized_df = (black_friday['Purchase'] - black_friday['Purchase'].mean()) / (black_friday['Purchase'].std())


# In[82]:


padronized_df


# In[83]:


((padronized_df >=-1) & (padronized_df <=1)).sum()


# In[12]:


def q9():
    # Retorne aqui o resultado da questão 9.
    padronized_df = (black_friday['Purchase'] - black_friday['Purchase'].mean()) / (black_friday['Purchase'].std())
    return int(((padronized_df >=-1) & (padronized_df <=1)).sum())


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[103]:


black_friday['Product_Category_2'].shape


# In[104]:


p2_null = black_friday[(black_friday['Product_Category_2'].isna() == True)]


# In[107]:


p2_null.shape


# In[113]:


p2_null['Product_Category_2'].equals(p2_null['Product_Category_3'])


# In[90]:


def q10():
    # Retorne aqui o resultado da questão 10.
    p2_null = black_friday[(black_friday['Product_Category_2'].isna() == True)]
    return p2_null['Product_Category_2'].equals(p2_null['Product_Category_3'])

