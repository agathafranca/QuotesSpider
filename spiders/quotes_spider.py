import scrapy

class QuoteSpider(scrapy.Spider): #pt-br: Criação da classe que herda de scrapy, que herda de Spider #en-us: Creation of the class that inherits from scrapy, that inherits from Spider

    name = 'quotes' #pt-br: Nome do Spider #en-us: Name os Spider
    start_urls = ['http://quotes.toscrape.com/'] #pt-br: Lista de URLS a serem raspadas/ envia o código fonte para o parâmetro response do método parse #en-us: List of URLs to be scraped / send the source code to the response parameter of the parse method

    """
    pt-br: Não altere o nome das variáveis acima porque a classe scrapy.Spider espera que essas variáveis sejam declaradas 
    en-us: Don't change the name of the above variables because the scrapy.Spider class expects these variables to be declared
    """

    #pt-br: Método _parse (self -> autoreferência | response -> contém o código fonte do site a ser raspado) #en-us: _Parse method (self -> reference to itself | response -> contains the source code of the site to be scratched)
    def _parse(self, response, **kwargs):
        all_div_quotes = response.css('div.quote') #pt-br: Armazena o conteúdo da classe quote na variável all_div_quotes #en-us: Stores the contents of the class quote in the variable all_div_quotes

        for quotes in all_div_quotes:

            title = quotes.css('span.text::text').extract() #pt-br: Extrai o texto da classe texto contida na tag span a partir do seletor css que faz a busca dentro da tag div e armazena na variável quote #en-us: Extracts the text of the text class contained in the span tag from the css selector that searches within the div tag and stores it in the quote variable
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
            yield{
                'title': title, #pt-br: Contém o dado extraído #en-us: contains the extracted data
                'author': author,
                'tag': tag
            } #pt-br: Requer um dicionário, chave de valores/ retorna o resultado da extração como um dicionário JSON #en-us: Requires a dictionary, key values ​​/ returns the result of the extraction as a JSON
