import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import scipy.optimize as op
st.set_page_config(page_title="Least squares method",  page_icon="🧊") #, layout="wide"
def linear(x, a, b):
    return a * x + b

def fit_with_curve_fit(x, y):
    popt, err = op.curve_fit(linear, x, y)
    return popt, np.sqrt(err.diagonal())


x=[None]*10
y=[None]*10
st.write("Введите значения x (все поля заполнять необязательно)")
row1 = st.columns(10)
for i, col in enumerate(row1):
#on_change=capture_x_0,
    inp_key="x_"+str(i)
    x[i]=col.number_input("", key=inp_key)
st.write("Введите значения y")
row2 = st.columns(10)
for i, col in enumerate(row2):
    inp_key="y_"+str(i)
    y[i]=col.number_input("", key=inp_key)

placeholder = st.empty()
X=np.array(x)
Y=np.array(y)
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(X[(X!=0) & (Y!=0)],Y[(X!=0) & (Y!=0)])
#ax.set_xlim(left=0)
#ax.set_ylim(bottom=0)
ax.tick_params(axis='both',which='both', direction="in", labelsize=10)
#ax.xaxis.set_minor_locator(MultipleLocator(0.2))
#ax.yaxis.set_minor_locator(MultipleLocator(0.5))
placeholder.pyplot(fig)
if (st.button("Аппроксимировать прямой y=a+bx") and len(X[(X!=0) & (Y!=0)])>1):
    if (len(X[(X!=0) & (Y!=0)])>2):
        popt, perr=fit_with_curve_fit(X[(X!=0) & (Y!=0)],Y[(X!=0) & (Y!=0)])
        st.write("Результаты обработки с помощью МНК:")
        st.write("b= "+ str(np.round(popt[0],3))) 
        st.write("a= "+ str(np.round(popt[1],3)))    
        st.write("$\Delta_{b}$= "+ str(np.round(perr[0],3)))
        st.write("$\Delta_{a}$= "+ str(np.round(perr[1],3)))
        X2=np.linspace(min(X),max(X),5)
        ax.plot(X2,X2*popt[0]+popt[1], linestyle = '--', color="black")
        placeholder.pyplot(fig)
        st.write("Не забудьте округлить значения величин и их погрешности в соответствии с правилами округления, добавить единицы измерения а также названия осей на графике")
    else:
        st.write("Введите не менее трех значений!")

