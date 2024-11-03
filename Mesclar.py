# importar as bibliotecas
import PyPDF2
import os

#criando o mesclador
merger = PyPDF2.PdfMerger()

#listando os arquivos 
lista_arquivos = os.listdir("PDF")
#listando para ordenação
lista_arquivos.sort()
print(lista_arquivos)
#percorrer a lista de
for PDF in lista_arquivos:
#criando uma condição para visualizar os arquivos pdf
    if ".pdf" in PDF:
#mesclar
        merger.append(f"PDF/{PDF}")
     
#Para salvar 
#dentro coloque o nome do arquivo que for melhor
merger.write("PDF final.pdf")