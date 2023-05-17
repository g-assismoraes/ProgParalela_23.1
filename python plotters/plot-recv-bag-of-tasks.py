import matplotlib.pyplot as plt

# Dados para o gráfico
num_proc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]  # número de processadores

# Tempo sequencial: Send, Isend, Rsend e Ssend
t_seq_send = 310.651
t_seq_Isend = 298.848
t_seq_Rsend = 303.424
t_seq_Ssend = 294.136

# tempo de execução paralelo 1
t_par1 = [310.651,185.862,138.578,119.108,110.210,105.242,98.152,99.793,96.424,96.576,93.187,96.106,93.317,93.730,94.690,97.660,93.258]  
# tempo de execução paralelo 2
t_par2 = [298.848,178.473,140.483,120.515,110.629,103.083,107.389,99.997,98.570,100.896,107.525,93.830,95.400,99.047,96.820,98.438,104.759]  
# tempo de execução paralelo 3
t_par3 = [303.424,174.923,133.243,117.231,106.924,98.637,97.330,95.371,95.584,102.615,91.769,91.180,90.810,88.732,90.252,92.400,88.670] 
# tempo de execução paralelo 4
t_par4 = [294.136,178.506,135.243,117.843,103.657,100.181,96.277,94.529,95.994,92.900,92.640,92.400,93.368,90.900,92.340,91.084,91.880]  

# Calculando o speedup
speedup1 = [t_seq_send / t_par1[i] for i in range(len(num_proc))]
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
plt.title('Gráfico de Eficiência do Bag of Tasks| N=200.000.000 | RECV')
plt.legend()
plt.savefig('Eficiencia-recv2-bag.png')

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
plt.title('Gráfico de Speedup do Bag of Tasks | N=200.000.000 | RECV')
plt.legend()
plt.savefig('Speedup-recv2-bag.png')

# Exibindo o gráfico de speedup
plt.show()
