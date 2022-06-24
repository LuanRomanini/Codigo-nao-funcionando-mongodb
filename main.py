import ssl

import pymongo


myclint = pymongo.MongoClient("mongodb+srv://user2:123@cluster0.j0vhm.mongodb.net/projeto")
#myclint = pymongo.MongoClient("mongodb+srv://user2:123@cluster0.j0vhm.mongodb.net/projeto", ssl_cert_reqs=ssl.CERT_NONE,ssl=False)
mydb = myclint['projeto']
mycol = mydb['proj']


opcao = 0
while opcao != 5:
    print('Bem vindo ao programa: \n\n')
    print('''        [ 1 ] Criar a entrada manual das informações
        [ 2 ] Criar uma rotina que tem o objetivo de fazer a leitura de um arquivo CSV e Inserir essas informações em uma base de dados do MongoDB
        [ 3 ] Criar uma rotina que que irá ler essas informações do banco de dados (MongoDB) e irá gerar um arquivo *.txt
        [ 4 ] Sair do programa''')

    opcao = int(input('    \nSelecione uma opcao: '))

    if opcao == 1:
        print('-=-\n')
        print('Hora de apresentar seus dados\n')
        print('-=-\n')
        nome = str(input('Digite seu nome \n'))
        idade = int(input('Digite sua idade \n'))
        bens = int(input('Digite a quantidade de bens que te pertencem \n'))
        cidade = str(input('Digite em qual cidade você reside \n'))
        estado = str(input('Digite qual estado você reside \n'))
        todosbens = str(input('Digite todos os seus bens aqui \n'))

        mydb.proj.insert_one({
            "nome": nome,
            "idade": idade,
            "bens": bens,
            "cidade": cidade,
            "estado": estado,
            "todosbens": todosbens
        })

    elif opcao == 2:
        mydoc = mycol.find().sort("place",1)
        f = open("C:\\Users\\Usuário\\Downloads\\bens-imveis-06-2022.csv", encoding='UTF-8')
        csv = f.readlines()
        for x in csv:

            item = x.split(",")
            mydb.proj.insert_one({
                "nome": item[0],
                "idade": item[1],
                "bens": item[2],
                "cidade": item[3],
                "estado": item[4],
                "todosbens": item[5]
            })

    elif opcao == 3:
        mydoc = mycol.find().sort("place",1)
        fw = open("C:\\Users\\Usuário\\Desktop\\Estudos\\projetotexto.txt")
        dadosout = []
        for dout in mydoc:
            dadosout.append(str(dout))

        fw.writelines(dadosout)
        fw.close()

    elif opcao == 4:
        print('Programa parou')
        exit()