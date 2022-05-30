# nome repositiorio 
## 1- Acrónimo do trabalho
BitScrapper

## 2- Instalação e dependências
No meu trabalho utilizei 3 librarias específicas que me ajudaram a desenvolver no meu software.
   Requests - é uma parte integrante do Python para fazer solicitações HTTP para um URL especifico.
   Pickle - implementa protocolos binários para serializar e desserializar uma estrutura de objeto Python.
   Beautiful Soup - Beautiful Soup é uma biblioteca Python que facilita a extração de informações de páginas da web.

## 3- Descrição do trabalho
### 3.1- Identificação
O meu programa consiste na serialização e na desserialização de um bloco de bitcoin.Um bloco de bitcoin possui informações importantes acerca dele mesmo, como a sua hash, o seu mineiro, a sua altura, e o seu tamanho, o seu número de transações e estes dados precisam de ser serializados,transformando o numa estruturas de dados em que possa ser armazenado e serem transmitidos, de uma forma mais robusta e tornar estes objetos persistentes.

### 3.2- Documentação
  Serialização
  Desserialização
  
### 3.4- Funcionamento
Primeiro precisaremos importar a biblioteca de requests e depois fazer o download  da página usando o método requests.get a atribuindo a página a variavel page
Depois temos que importar a biblioteca, e criar um exemplo da classe BeautifulSoup
Na variável soap conseguimos analisar o nosso documento e assim podemos ver todo conteúdo HTML da página e scrappear todo o conteúdo que nós quisermos.
Depois guardei na variável lists toda a informação do bloco que vinha da div com a sua classe especifica.
A seguir, criei um loop  para correr todos campos da minha listas com os seus spans específicos e a sua classe específica que possui o bloco da bitcoin e colocar na variável lists e, depois fazer um print destes valores numa lista.
E depois através da biblioteca pickle serializar esta lista de valores.

## 5- Bibliografia
Material dado pelo o docente
Tutorial: Web Scraping with Python Using Beautiful Soup – Dataquest
pickle — Python object serialization — Python 3.10.4 documentation
Blockchain Explorer - Pesquise o Blockchain | BTC | ETH | BCH
What is Beautiful Soup? (educative.io)

