# Controle de Concorrência em Sistemas Distribuídos
Este projeto visa desenvolver e implementar um sistema de controle de concorrência para garantir a exclusão mútua em um ambiente de múltiplos processos. Para isso, serão utilizados diferentes algoritmos de sincronização e eleição discutidos na disciplina de Sistemas Operacionais.

1. Introdução
A concorrência em sistemas operacionais pode levar a problemas como a condição de corrida, onde múltiplos processos competem pelo acesso a recursos compartilhados. Para garantir a integridade dos dados e evitar inconsistências, é necessário implementar mecanismos que garantam a exclusão mútua, permitindo que apenas um processo acesse uma seção crítica por vez.

2. Algoritmos de Exclusão Mútua
Algoritmo Token-Ring
Um token circula entre os processos, garantindo acesso exclusivo à seção crítica. Apenas o processo detentor do token pode acessar a seção crítica, passando o token para o próximo processo após sua utilização.

Algoritmo do Valentão
Os processos realizam uma eleição para escolher um coordenador. O processo com o maior identificador assume o papel de coordenador, garantindo a exclusão mútua e a coordenação das operações.

3. Requisitos Funcionais
Garantir exclusão mútua, evitando acesso simultâneo à mesma seção crítica por múltiplos processos.
Implementar mecanismos para evitar inanição e deadlocks, garantindo que todos os processos tenham a oportunidade de acessar as seções críticas.
Detectar e lidar com a falha de processos, assegurando a continuidade das operações mesmo na ausência de um coordenador ativo.
