import matplotlib.pyplot as plt

# Dados para o gráfico
#num_proc = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]  # número de processadores
num_proc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]  # número de processadores

# Tempo sequencial: Send, Isend, Rsend e Ssend
t_seq_send = 302.119
t_seq_Isend = 298.040
t_seq_Rsend = 306.456
t_seq_Ssend = 292.911

# tempo de execução paralelo 1
t_par1 = [302.119,177.534,134.230,112.639,102.105,95.611,94.865,92.525,92.274,90.780,91.109,90.270,91.197,90.319,89.420,89.018,90.600]  
# tempo de execução paralelo 2
t_par2 = [298.040,178.219,133.118,113.376,101.035,94.395,93.084,91.780,91.734,90.576,90.247,89.390,89.350,89.444,90.500,89.696,88.630]
# tempo de execução paralelo 3
t_par3 = [306.456,174.755,132.153,113.167,104.172,97.962,95.385,94.537,94.010,92.301,91.817,91.906,729.365,88.370,87.999,89.380,90.160] 
# tempo de execução paralelo 4
t_par4 = [292.911,175.889,138.260,115.796,104.909,98.155,96.900,95.295,97.029,96.950,97.090,90.597,90.590,89.850,89.860,88.792,92.230]  

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
plt.title('Gráfico de Eficiência do Bag of Tasks| N=200.000.000 | IRECV')
plt.legend()
plt.savefig('Eficiencia-irecv2-bag.png')

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
plt.title('Gráfico de Speedup do Bag of Tasks | N=200.000.000 | IRECV')
plt.legend()
plt.savefig('Speedup-irecv2-bag.png')

# Exibindo o gráfico de speedup
plt.show()
