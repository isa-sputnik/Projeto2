
# <font color="#DAA520">Resilia - Projeto do Módulo-2</font>

![](https://raw.githubusercontent.com/isa-sputnik/Projeto2/main/capa.png)

## Objetivo do Projeto

Este projeto foi feito como parte integrante da avaliação do Módulo 2 do curso Data Analytics da Resilia Educação da turma 20. Este projeto foi desenvolvido pelo Squad 2, que é composto pelos estudantes:

- Bárbara de Avelar;

- Isabelle Cavalcante;

- Luiza Sampaio;

- Stephanie Fernandes;

- Thiago Vasconcelos.


## Descrição do Projeto

Este é um projeto é representa um instrumento de pesquisa digital com a população de várias cidades do Brasil com o objetivo de armazenar os dados da pesquisa realizada em um arquivo .csv para utilização em análises futuras. Na realização da pesquisa a equipe sairá com o projeto nas ruas para coletar as respostas.

### Tema abordado

A Organização Mundial da Saúde (OMS) publicou em 18 de março de 2019 um relatório intitulado "A pandemia da COVID-19": Saúde mental e bem-estar". Ele se baseia em observações abertas e pesquisas realizadas entre dezembro de 2017 e janeiro de 2019, que incluíram entrevistas com mais de 1.700 pessoas que vivem em países que sofreram um surto.

Este relatório destaca que existem muitas formas diferentes de estresse, como dificuldades financeiras ou separações familiares devido à migração. Além disso, há um aumento no isolamento social, o que pode levar a depressão ou distúrbios de ansiedade.[^1]

A partir desta temática nossa pesquisa procura simular a identificação do impacto da pandemia na saúde mental da população, a partir da comparação da escala de casos de depressão antes e pós pandemia. 

Como base de dados para comparação inicial temos valores de casos de depressão documentados até o ano de 2019, sintetizado neste gráfico.

![](https://raw.githubusercontent.com/isa-sputnik/Projeto2/main/PESSOAS%20COM%20DEPRESSÃO%20(MILHÕES)%20X%20ANO.png)


## Estrutura do projeto

A pesquisa realizada contém 4 perguntas que podem ser respondidas com Sim (1), Não (2) e Não sei responder (3). Para elaboração da pesquisa foi utilizado o paradigma de orientação a objetos.

### Funcionamento do código

No início do questionário é solicitado ao entrevistado que informe a sua idade e
gênero.  A pesquisa solicita respostas em um laço de repetição que fica
inserindo as respostas informadas em dicionários até que a idade de valor = 0
seja informada, assim finalizando a pesquisa e gerando um arquivo de saída .csv em que cada linha contém os seguintes dados de uma uma pessoa entrevistada: idade, gênero, resposta_1, resposta_2, resposta_3, resposta_4, data e hora da resposta.
	
### Fluxograma de funcionamento do código
		
![](https://raw.githubusercontent.com/isa-sputnik/Projeto2/main/fluxograma.png)

### Perguntas escolhidas para a pesquisa

- Após informar a sua idade e gênero o usuário responderá as seguintes perguntas e opções de resposta:

		[1] Você concluiu o ensino médio? Sim (1), Não (2) e Não sei responder (3)
		
		[2] Sua média salarial ultrapassa 2 salários mínimos? Sim (1), Não (2) e Não sei responder (3)
		
		[3] Durante o período de pandemia, você ou alguém próximo, sofreu com alguma doença psicológica, agravada pelo isolamento social? Sim (1), Não (2) e Não sei responder (3)
		
		[4] Você consideraria procurar uma rede de apoio como forma de auxílio? Sim (1), Não (2) e Não sei responder (3)

#### Validação de dados
		
- Existem duas validações de entrada no código, que estão em funções: uma para o caso do input ser um inteiro ou uma string. No caso, se eu desejo que minha entrada seja um inteiro, meu código só aceita esse tipo de entradas, e em caso de outro tipo, ele entra em um loop, informando que a entrada está no formato incorreto e pedindo para o usuário inserir uma entrada válida. O mesmo se aplica a entrada de texto: se o usuário entrar com um número, entra no loop, até ser fornecido uma entrada do tipo string.

### Referências

[^1]: MATTA, G.C., REGO, S., SOUTO, E.P., and SEGATA, J., eds. Os impactos sociais da Covid-19 no Brasil: populações vulnerabilizadas e respostas à pandemia [online]. Rio de Janeiro: Observatório Covid 19; Editora FIOCRUZ, 2021, 221 p. Informação para ação na Covid-19 series. ISBN: 978-65-5708-032-0.
