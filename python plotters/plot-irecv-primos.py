import matplotlib.pyplot as plt

# Dados para o gráfico
num_proc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]  # número de processadores

# Tempo sequencial: Send, Isend, Rsend e Ssend
t_seq_send = 178.371
t_seq_Isend = 179.471
t_seq_Rsend = 177.825
t_seq_Ssend = 178.487

# tempo de execução paralelo 1
t_par1 = [178.371,110.082,123.142,71.681,76.481,84.724,62.109,51.240,76.400,66.776,63.060,82.551,59.711,62.625,957.358,54.585,55.916,82.370]  
# tempo de execução paralelo 2
t_par2 = [179.471,109.335,124.202,71.580,79.898,89.286,63.806,56.840,81.146,68.810,65.990,84.032,57.835,64.057,97.270,53.060,56.102,79.980]  
# tempo de execução paralelo 3
t_par3 = [177.825,110.986,122.994,71.056,77.323,86.317,62.790,51.468,79.702,67.000,62.640,85.950,60.270,63.210,341.084,51.710,55.224,78.310] 
# tempo de execução paralelo 4
t_par4 = [178.487,109.297,126.534,71.491,77.543,86.050,62.974,51.839,79.342,68.752,62.570,83.599,57.790,61.419,151.601,51.800,55.580,78.420]  

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
plt.title('Gráfico de Eficiência | N=100.000.000 | IRECV')
plt.legend()
plt.savefig('Eficiencia-irecv-primos.png')

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
plt.title('Gráfico de Speedup | N=100.000.000 | IRECV')
plt.legend()
plt.savefig('Speedup-irecv-primos.png')

# Exibindo o gráfico de speedup
plt.show()
