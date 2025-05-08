|                             | Plano A | Plano B | Plano C |
|-----------------------------|---------|---------|---------|
| Tuples loaded               | 11      | 11      | 11      |
| Accessed blocks             | 541     | 541     | 544     |
| Loaded blocks               | 0       | 0       | 0       |
| Saved blocks                | 0       | 0       | 0       |
| Filter comparations         | 3179    | 3179    | 3179    |
| Memory Used                 | 21840   | 737     | 637     |
| Next Calls                  | 284     | 295     | 73      |
| Primary key searches        | 0       | 0       | 7       |
| Records Read                | 3419    | 3419    | 3433    |
| Sorted tuples               | 0       | 0       | 0       |

O Plano A consumiu aproximadamente 30 vezes mais memória do que os demais, pois precisou construir uma tabela hash com todos os registros da tabela `movie`. No entanto, esse alto uso de memória não resultou em um menor número de blocos acessados, tornando-o o menos eficiente entre os planos analisados. Já os Planos B e C apresentaram desempenhos similares tanto em relação ao número de blocos acessados quanto ao uso de memória. O Plano B realiza uma varredura (scan) completa na tabela `movie`, o que o torna mais adequado quando os registros com `cast_order > 60` pertencem a diversos filmes distintos. Por outro lado, o Plano C é mais eficiente quando esses registros estão concentrados em poucos filmes. Considerando que a maioria dos registros com `cast_order > 60` irão pertencer a um mesmo filme, o Plano C se mostra mais vantajoso, pois consome menos memória do que o Plano B, acessando apenas 3 páginas a mais.