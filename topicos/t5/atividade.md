```
Leitura em blocos de 1KB: 2591.19 ms 
Leitura em blocos de 2KB: 1621.81 ms 
Leitura em blocos de 4KB: 1063.20 ms 
Leitura em blocos de 8KB: 814.11 ms 
Leitura em blocos de 16KB: 682.28 ms 
Leitura em blocos de 32KB: 614.75 ms 
Leitura em blocos de 64KB: 586.38 ms 
Leitura em blocos de 128KB: 573.87 ms 
Leitura em blocos de 256KB: 568.07 ms 
Leitura em blocos de 512KB: 593.38 ms 
Leitura em blocos de 1024KB: 926.80 ms 
Leitura em blocos de 2048KB: 897.85 ms 
Leitura em blocos de 4096KB: 909.98 ms 
Leitura em blocos de 8192KB: 1012.25 ms 
Leitura em blocos de 16384KB: 962.41 ms 
Leitura em blocos de 32768KB: 972.18 ms 
Leitura em blocos de 65536KB: 1057.09 ms 
Leitura em blocos de 131072KB: 1230.62 ms
```

Para analisar a variação dos tempos de leitura de um arquivo, foram realizados testes utilizando diferentes tamanhos de blocos para a leitura completa de um arquivo de 128MB. O tamanho inicial do bloco foi de 1KB, dobrando-se progressivamente até atingir 128MB.

Os resultados mostraram que, à medida que o tamanho dos blocos aumenta, o tempo de leitura diminui de forma significativa até aproximadamente 256KB. Esse comportamento ocorre porque blocos maiores reduzem a quantidade de operações de leitura e chamadas de sistema, permitindo um melhor aproveitamento dos mecanismos de cache do sistema operacional, diminuindo a sobrecarga de operações e melhorando o desempenho.

Entre 128KB e 512KB, o tempo de leitura atinge uma faixa de estabilidade, indicando o ponto de equilíbrio entre o aproveitamento do cache e a eficiência do acesso sequencial. Tal comportamento indica que blocos nessa faixa tendem a ser o tamanho ideal para maximizar a performance de leitura.  A partir de blocos maiores que 1MB, o tempo de leitura volta a crescer. Esse aumento pode estar ocorrendo devido ao esforço adicional para alocar e desalocar grandes blocos de memória contígua e à utilização dos diferentes níveis de cache do processador.
