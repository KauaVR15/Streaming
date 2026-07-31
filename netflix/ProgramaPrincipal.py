from Obra import Obra
from Filme import Filme
from Serie import Serie
from Documentario import Documentario


def catalogo():

        print("-----Catálogo-----")
        print(f"|1- Filme \n|2- Serie \n|3- Documentario \n|4- Voltar")

        tipo_obra()

def tipo_obra():

        try:            
            escolha_tipo = int(input("-> Escolha qual tipo de obra deseja visualizar: "))
        except ValueError:
            print(" !Erro! Tipo de dado esperado: Número")

        match escolha_tipo:

            case 1:

                if len(lista_filme) == 0:
                    print("Não há filmes disponíveis no momento...")

                else:
                    print("|Filmes: ")
                    for i, filme in  enumerate(lista_filme):
                        print(f"|{i + 1}- {filme.get_titulo()}")

                    try:
                        escolha_filme = int(input("-> Escolha qual filme voce deseja ver as informacoes: "))
                    except ValueError:
                        print(" !Erro! Tipo de dado esperado: Número")

                    if 1 <= escolha_filme <= len(lista_filme):

                        filme_escolhido = lista_filme[escolha_filme - 1] 

                        print(filme_escolhido.exibir_info())

                    else:
                        print("!Erro!")

            case 2:

                if len(lista_serie) == 0:
                    print("Não há series disponíveis no momento...")

                else:
                    print("|Series: ")
                    for i, serie in  enumerate(lista_serie):
                        print(f"|{i + 1}- {serie.get_titulo()}")

                    try:
                        escolha_serie = int(input("-> Escolha qual serie voce deseja ver as informacoes: "))
                    except ValueError:
                        print(" !Erro! Tipo de dado esperado: Número")

                    if 1 <= escolha_serie <= len(lista_serie):

                        serie_escolhido = lista_serie[escolha_serie - 1] 

                        print(serie_escolhido.exibir_info())

                    else:
                        print("!Erro!")

            case 3:

                if len(lista_documentario) == 0:
                    print("Não há documentarios disponíveis no momento...")

                else:
                    print("|Documentarios: ")
                    for i, documentario in  enumerate(lista_documentario):
                        print(f"|{i + 1}- {documentario.get_titulo()}")

                    try:
                        escolha_documentario = int(input("-> Escolha qual documentario voce deseja ver as informacoes: "))
                    except ValueError:
                        print(" !Erro! Tipo de dado esperado: Número")

                    if 1 <= escolha_documentario <= len(lista_documentario):

                        documentario_escolhido = lista_documentario[escolha_documentario - 1] 

                        print(documentario_escolhido.exibir_info())

                    else:
                        print("!Erro!")

            case 4:
                print("Voltando...")
           
def registrar_obra():

        
        print("-----Registro de Obras-----")
        print(f"|1- Filmes \n|2- Series \n|3- Documentarios \n|4- Voltar \n")

        try:

            escolha_obra = int(input("-> Digite qual obra deseja inserir: "))

        except ValueError:
                    print(" !Erro! Tipo de dado esperado: Número")
        

        match(escolha_obra):

            case 1:
                
                print(" -----Resgistro-----")

                while True:

                    try:
                    
                        titulo_filme = input("|Digite o titulo do filme: ")
                        ano_lancamento_filme = int(input("|Digite o ano de lançamento: "))
                        duracao_filme = int(input("|Digite a duracao: "))
                        class_indicativa_filme = input("|Digite a classificação indicativa: ")
                        diretor_filme = input("|Digite o nome do diretor: ")
                        genero_filme = input("|Digite o genero do filme: ")
                        bilheteria_filme = float(input("|Digite a bilheteria: "))
        
                        novo_filme = Filme(titulo_filme, ano_lancamento_filme, duracao_filme,
                                      class_indicativa_filme, diretor_filme, genero_filme, bilheteria_filme)

                        lista_filme.append(novo_filme)

                        print("Filme catalogado com sucesso!")

                        continuar = input("Voce deseja continuar? ('S'/'N')").strip().upper()
    
                        if continuar == 'N':
                            break

                    except ValueError:
                        print(" !Erro! Tipo de dado esperado: Número")
                
                print(f"Total de filmes cadastrados: {len(lista_filme)}")

            case 2:
                
                print(" -----Resgistro-----")

                while True:

                    try:
                    
                        titulo_serie = input("|Digite o titulo da serie: ")
                        ano_lancamento_serie = int(input("|Digite o ano de lançamento: "))
                        duracao_serie = int(input("|Digite a duracao: "))
                        class_indicativa_serie = input("|Digite a classificação indicativa: ")
                        qtde_temp_serie = int(input("|Digite a quantidade de temporadas: "))
                        qtde_eps_serie = int(input("|Digite a quantidade de episodios: "))

                        nova_serie = Serie(titulo_serie, ano_lancamento_serie, duracao_serie,
                                    class_indicativa_serie, qtde_temp_serie, qtde_eps_serie)

                        lista_serie.append(nova_serie)

                        print("Serie catalogado com sucesso!")

                        continuar = input("Voce deseja continuar? ('S'/'N')").strip().upper()
    
                        if continuar == 'N':
                            break
                    
                    except ValueError:
                        print(" !Erro! Tipo de dado esperado: Número")
                
                print(f"Total de series cadastrados: {len(lista_serie)}")

            case 3:
                
                print(" -----Resgistro-----")
                     
                while True:

                    try:
                    
                        titulo_documentario = input("|Digite o titulo do documentario: ")
                        ano_lancamento_documentario = int(input("|Digite o ano de lançamento: "))
                        duracao_documentario = int(input("|Digite a duracao: "))
                        class_indicativa_documentario = input("|Digite a classificação indicativa: ")
                        tema_documentario = (input("|Digite o tema do documentario: "))
                        narrador_documentario = (input("|Digite o narrador do documentario: "))

                        novo_documentario = Documentario(titulo_documentario, ano_lancamento_documentario, duracao_documentario,
                                    class_indicativa_documentario, tema_documentario, narrador_documentario)

                        lista_documentario.append(novo_documentario)

                        print("Documentario catalogado com sucesso!")

                        continuar = input("Voce deseja continuar? ('S'/'N')").strip().upper()
    
                        if continuar == 'N':
                            break

                    except ValueError:
                        print(" !Erro! Tipo de dado esperado: Número")


                print(f"Total de documentarios cadastrados: {len(lista_documentario)}")

            case 4:
                print("Voltando...")    
  

lista_filme = []
lista_serie = []
lista_documentario = []

while True:

    print(" ------Menu------")
    print("|1- Catálogo")
    print("|2- Inserir obras")
    print("|3- Sair")


    try:    
        escolha_menu = int(input("-> Digite qual opcão deseja escolher: "))
    except ValueError:
        print(" !Erro! Tipo de dado esperado: Número")
    
    match(escolha_menu):

        case 1:

            catalogo()
            
        case 2:

            registrar_obra()

        case 3:
            print("Saindo...")
            break

