import matplotlib.pyplot as plt

# Dados para o gráfico
num_proc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]  # número de processadores

# Tempo sequencial: Send, Isend, Rsend e Ssend
t_seq_send = 185.137
t_seq_Isend = 189.842
t_seq_Rsend = 191.764
t_seq_Ssend = 186.682

# tempo de execução paralelo 1
t_par1 = [185.137,112.593,127.946,74.222,80.820,90.601,66.431,54.017,79.965,70.421,65.860,79.785,69.675,68.655,106.400,56.950,59.780,82.234 ]  
# tempo de execução paralelo 2
t_par2 = [189.842,114.446,131.806,75.195,82.382,90.774,65.854,57.855,85.010,70.845,68.996,82.911,65.830,63.570,97.727,55.838,56.350,80.840]  
# tempo de execução paralelo 3
t_par3 = [191.764,109.654,129.797,74.667,81.372,90.571,66.672,53.873,80.393,78.098,67.558,86.630,62.140,68.434,111.510,64.700,61.807,84.162] 
# tempo de execução paralelo 4
t_par4 = [186.682,114.900,132.899,88.838,82.407,90.519,69.449,58.090,83.313,73.938,68.859,88.850,69.467,87.970,106.720,53.850,56.868,80.270]  

# Calculando o speedup
speedup1 = [t_seq_send  / t_par1[i] for i in range(len(num_proc))]
speedup2 = [t_seq_Isend / t_par2[i] for i in range(len(num_proc))]
speedup3 = [t_seq_Rsend / t_par3[i] for i in range(len(num_proc))]
speedup4 = [t_seq_Ssend / t_par4[i] for i in range(len(num_proc))]

# Calculando a eficiência
eficiencia1 = [(speedup1[i] / num_proc[i])*100 for i in range(len(num_proc))]
eficiencia2 = [(speedup2[i] / num_proc[i])*100 for i in range(len(num_proc))]
eficiencia3 = [(speedup3[i] / num_proc[i])*100 for i in range(len(num_proc))]
eficiencia4 = [(speedup4[i] / num_proc[i])*100 for i in range(len(num_proc))]

# Plotando o gráfico de eficiência
plt.plot(num_proc, eficiencia1, 'bo-', label='Send')
plt.plot(num_proc, eficiencia2, 'go-', label='Isend')
plt.plot(num_proc, eficiencia3, 'mo-', label='Rsend')
plt.plot(num_proc, eficiencia4, 'yo-', label='Ssend')
plt.xlabel('Número de Processadores (n)')
plt.xticks(range(0, 19, 1))
plt.ylabel('Eficiência (%)')
plt.yticks(range(0, 110, 10))
plt.title('Gráfico de Eficiência | N=100.000.000 | RECV')
plt.legend()
plt.savefig('Eficiencia-recv-primos.png')

# Exibindo o gráfico de eficiência
plt.show()

# Plotando o gráfico de speedup
plt.plot(num_proc, speedup1, 'bo-', label='Send')
plt.plot(num_proc, speedup2, 'go-', label='ISend')
plt.plot(num_proc, speedup3, 'mo-', label='RSend')
plt.plot(num_proc, speedup4, 'yo-', label='Ssend')
plt.plot(num_proc, num_proc, 'ro-', label='SpeedUp Ideal')
plt.xlabel('Número de Processadores (n)')
plt.xticks(range(0, 19, 1))
plt.ylabel('Speedup')
plt.yticks(range(0, 20, 2))
plt.title('Gráfico de Speedup | N=100.000.000 | RECV')
plt.legend()
plt.savefig('Speedup-recv-primos.png')

# Exibindo o gráfico de speedup
plt.show()
