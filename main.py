from bs4 import BeautifulSoup
import requests
import pickle

url = "https://www.blockchain.com/btc/block/3"
page = requests.get(url)


print(page)

soup = BeautifulSoup(page.content, 'html.parser')
#print(type(soup))
lists = soup.find_all('div', class_="hnfgic-0 enzKJw")
#print(type(lists))

outputFile = open('Listas', 'wb')

for list in lists:
    hash = list.find('span', class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC").text
    confirmacoes = list.find_all('span', class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC")[1].text
    data_hora = list.find_all('span', class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC")[2].text
    altura = list.find_all('span', class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC" )[3].text
    mineiro = list.find('a', class_="sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk").text
    transacoes = list.find_all('span', class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC" )[4].text
    dificuldade = list.find_all('span', class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC" )[5].text
    raiz_Merkle = list.find_all('span', class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC" )[6].text
    versao = list.find_all('span', class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC" )[7].text
    bits = list.find_all('span', class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC" )[8].text
    peso = list.find_all('span', class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC" )[9].text
    tamanho = list.find_all('span', class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC" )[10].text
    nonce = list.find_all('span', class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC" )[11].text
    volume_transacao = list.find_all('span', class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC" )[12].text

    info = [hash, confirmacoes, data_hora, altura, mineiro, transacoes, dificuldade, raiz_Merkle, versao, bits, peso, tamanho, nonce, volume_transacao]
    print(info)
    pickle.dump(info, outputFile)
    outputFile.close()



























