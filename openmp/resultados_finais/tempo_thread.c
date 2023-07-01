#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

int primo (long int n) { 
    int i;   
    for (i = 3; i < (int)(sqrt(n) + 1); i+=2) {
        if(n%i == 0) return 0;
    }
    return 1;
}

int main(int argc, char *argv[]) {
    double t_inicial, t_final;
    double *thread_times;
    int total = 0;
    int i, n, t;

    if (argc < 3) {
        printf("Valor inválido! Entre com um valor e com o numero de threads\n");
        return 0;
    } else {
        n = strtol(argv[1], (char **) NULL, 10);
        t = strtol(argv[2], (char **) NULL, 10);
    }

    omp_set_num_threads(t);
    t_inicial = omp_get_wtime();

    // Alocando memória para armazenar os tempos de execução de cada thread
    thread_times = (double*)malloc(t * sizeof(double));
    for (i = 0; i < t; i++)
        thread_times[i] = 0.0;

    #pragma omp parallel for reduction(+:total) schedule(dynamic, 50000)
    for (i = 3; i <= n; i+=2) {
        double t_inicial_thread = omp_get_wtime();  // Início da medição de tempo para a thread atual
        if(primo(i) == 1) total++;
        thread_times[omp_get_thread_num()] += omp_get_wtime() - t_inicial_thread;  // Adiciona o tempo de execução da thread
    }

    total += 1; //Adds 2, which is also a prime number
    t_final = omp_get_wtime();

    printf("Quant. de primos entre 1 e %d: %d \n", n, total);
    printf("Tempo de execucao: %1.3f \n", t_final - t_inicial);
    
    // Impressão do tempo de execução de cada thread
    for (i = 0; i < t; i++) {
        printf("Tempo de execucao da thread %d: %1.3f \n", i, thread_times[i]);
    }

    // Liberação da memória alocada para os tempos de execução das threads
    free(thread_times);

    return(0);
}
