# Projeto Embarcados

Desenvolvendo um controle remoto.

## Entrega 1

### Integrantes

- Pedro Osborn Mahfuz
- Pedro Von Dannecker

### Ideia

Nosso dispositivo será de aplicação, ele irá controlar certas funções no canal de streaming Netflix, iremos implementar botões com as seguintes funções: controlar o volume (se segurar abaixa se clicar aumenta), avançar 10 segundos na reprodução, voltar 10 segundos na reprodução, joystick com função de selecionar e além disso funciona como analógico que controla o mouse. 

### Nome

Pedro

### Usuários 

Qulquer usuário do canal de streaming Netflix, que deseja utilizar o computador para assistir o conteúdo disponível.

### Software/Jogo 

Nosso controle irá possibilitar ações dentro da plataforma de streaming Netflix, sendo funcional apenas se usado no notebook.  

### Jornada do usuários (3 pts)

<!-- Descreva ao menos duas jornadas de usuários distintos, é para caprichar! -->
Cenário 1: 
  O usuário chega em casa cansado de um longo dia de aulas no Insper, e decide que o resto do dia será dedicado a acabar de assistir sua séria favorita. Mas ao sentar no sofá percebe que o controle da televisão não se encontra em nenhum lugar. Como já estava exausto e com sua mochila ao seu alcance, ele decide conectar seu computador a TV, acessar a Netflix e utilizar o controle "Pedro". Desse modo, consegue assistir a série na sua televisão, com um controle que fica do seu lado no sofá!
  
  
Cenário 2: 
  Um usuário quer ter mais conforto ao assistir filmes e series em seu computador, ele gostaria de poder controlar tudo de alguma maneira sem ser pelo touchpad/mouse. Então ele utiliza o controle "Pedro" com intenção de poder deixar seu computador um pouco mais afastado e poder controlar as funções do filme/serie ao mesmo tempo, podendo adiantar e retornar o filme/serie ou aumentar e diminuir o volume diretamente a partir de botoes próximos a ele. 

### Comandos/ Feedbacks (2 pts)

<!-- 
Quais são os comandos/ operacões possíveis do seu controle?

Quais os feedbacks que seu controle vai fornecer ao usuário?
-->
Movimentação do mouse e função selecionar:Joystick
 -- Através do Joystick, que possui dois sensores analógicos, o usuário ao moviment-lo poderá realizar as mesmas funções de um mouse, ou seja, movimentação em plano xy e opção de selecionar, que será indicada através de um LED.
 
 
Adiantar episodio: Push button amarelo
-- O usuário pode utilizar da função do streaming de avançar 10 segundos do filme/episodio ao clicar o botão amarelo.


Retornar episodeo:Push button verde
-- O usuário pode utilizar da função do streaming de retornar 10 segundos do filme/episodio ao clicar o botão verde.


Liga/Desliga: botão com led
-- O usuário poderá liga e desligar o bluetooth do controle ao clicar este botão, que por sua vez, indica pressionamento através de um LED.


Variar volume: Push button vermelho
--O usuário pode aumentar o volume ao clicar e soltar o botão vermelho ou diminuir o volume caso pressione e segure o mesmo.



## In/OUT (3 pts)

<!--
Para cada Comando/ Feedback do seu controle, associe qual sensores/ atuadores pretende utilizar? Faca em formato de lista, exemplo:

- Avanca música: Push button amarelo
- Volume da música: Fita de LED indicando potência do som
-->
Movimentação do mouse e função selecionar:Joystick e LED da placa SAME-70


Adiantar episodio: Push button amarelo


Retornar episodeo:Push button verde


volume da musica:Push button vermelho


Liga/Desliga: botão com led




### Design (2 pts)

![WhatsApp Image 2022-09-16 at 4 18 50 PM](https://user-images.githubusercontent.com/62957998/190798022-d4c5e137-e7fd-43bc-b35a-e6cc1da1a127.jpeg)
<!--
Faca um esboco de como seria esse controle (vai ter uma etapa que terão que detalhar melhor isso).
-->
