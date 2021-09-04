import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets


def first_order_plot(k):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6*2, 6))
    t = np.linspace(0, 100, 101)
    
    plt.suptitle("First-Order Reaction\nk = %.2f s$^{-1}$" %k, fontsize=28)
    
    ax1.set_ylim(0, 1)
    ax1.plot(t, np.exp(-k*t), label="Reactant")

    ax1.plot(t, 1-np.exp(-k*t), label="Product", c='orange')
    
    ax1.tick_params(axis='both', labelsize=20)
    ax1.set_xlabel("Time (s)", fontsize=24)
    ax1.set_ylabel("[A]/[A]$_0$", fontsize=24)
    
    ax1_twin = ax1.twinx()
    ax1_twin.tick_params(axis='both', labelsize=20)
    ax1_twin.set_ylim(0, 1)
    ax1_twin.set_ylabel("[P]/[A]$_0$", fontsize=24)
    
    ax1.legend(loc="upper right", fontsize=20)
    
    ax2.set_ylim(-20, 0)
    ax2.plot(t, -k*t)
    ax2.tick_params(axis='both', labelsize=20)
    ax2.set_xlabel("Time (s)", fontsize=24)
    ax2.set_ylabel("ln([A]/[A]$_0$)", fontsize=24)
    
    plt.tight_layout()
    plt.show()
    
interactive_first_order_plot = widgets.interactive(first_order_plot, k=(1e-2, 5e-1, 5e-2))

def second_order_plot_type1(k):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6*2, 6))
    t = np.linspace(0, 100, 101)
    
    plt.suptitle("Second-Order Reaction (Type I)\nk$_{eff}$ = %.2f s$^{-1}$" %k, fontsize=28)
    
    A0 = 1
    A_inv = 1/A0 + k*t
    A = 1/A_inv
    
    ax1.set_ylim(0, 1)
    ax1.plot(t, A)
    ax1.tick_params(axis='both', labelsize=20)
    ax1.set_xlabel("Time (s)", fontsize=24)
    ax1.set_ylabel("[A]/[A]$_0$", fontsize=24)
    
    ax2.set_ylim(1, 20)
    ax2.plot(t, A_inv)
    ax2.tick_params(axis='both', labelsize=20)
    ax2.set_xlabel("Time (s)", fontsize=24)
    ax2.set_ylabel("([A]/[A]$_0$)$^{-1}$", fontsize=24)
    
    plt.tight_layout()
    plt.show()
    
interactive_second_order_plot = widgets.interactive(second_order_plot_type1, k=(1e-2, 5e-1, 5e-2))


def sequential_first_order(ka, ki):
    fig, ax1 = plt.subplots(1, 1, figsize=(6, 6))
    t = np.linspace(0, 100, 101)
    
    plt.suptitle("Sequential First-Order Reaction\nk$_A$ = %.3f s$^{-1}$ and k$_i$ = %.3f s$^{-1}$" %(ka, ki), fontsize=28)
    
    A = np.exp(-ka*t)
    I = ka/(ki-ka) * (np.exp(-ka*t) - np.exp(-ki*t))
    P = (ka*np.exp(-ki*t) - ki*np.exp(-ka*t))/(ki-ka) + 1
    
    t_max = 1/(ka-ki) * np.log(ka/ki)
    
    ax1.set_ylim(0, 1)
    ax1.vlines(t_max, 0, np.max(I), colors=["black"])
    ax1.plot(t, A, label="[A]")
    ax1.plot(t, I, label="[I]")
    ax1.plot(t, P, label="[P]")
    ax1.tick_params(axis='both', labelsize=20)
    ax1.set_xlabel("Time (s)", fontsize=24)
    ax1.set_ylabel("[X]/[A]$_0$", fontsize=24)
    
    ax1.legend(loc="upper right", fontsize=20)
    
    plt.tight_layout()
    plt.show()
    
interactive_sequential_first_order = widgets.interactive(sequential_first_order, ka=(1e-2, 5e-1, 5e-2), ki=(1.1e-2, 5.1e-1, 5e-2))