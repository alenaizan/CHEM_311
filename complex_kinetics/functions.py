import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets


def langmuir_isotherm(K):
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    p = np.linspace(0, 50, 51)
    
    plt.suptitle("Langmuir Isotherm\n $k_a/k_d$ = %.2f/atm" %K, fontsize=28)
    
    ax.set_ylim(0, 1)
    ax.plot(p, K*p/(K*p + 1))

    ax.tick_params(axis='both', labelsize=20)
    ax.set_xlabel("Pressute (atm)", fontsize=24)
    ax.set_ylabel("$\\theta$", fontsize=24)
   
    plt.tight_layout()
    plt.show()
    
interactive_langmuir_isotherm = widgets.interactive(langmuir_isotherm, K=(0.05, 5, 0.05))

def inhibited_catalysis(I):
    k2 = 1
    E0 = 1
    Km = 1
    Ki = 1
    
    S0 = np.linspace(0, 10, 51)
    
    R = k2*S0*E0/(S0 + Km*(1 + I/Ki))
    
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    plt.suptitle("Competitive Inhibitor\n [I] = %.2f" %I, fontsize=28)
    
    ax.set_ylim(0, 1)
    ax.plot(S0, R)

    ax.tick_params(axis='both', labelsize=20)
    ax.set_xlabel("[S]$_0$", fontsize=24)
    ax.set_ylabel("Rate", fontsize=24)
   
    plt.tight_layout()
    plt.show()
    
interactive_inhibited_catalysis = widgets.interactive(inhibited_catalysis, I=(0, 10, 0.02))