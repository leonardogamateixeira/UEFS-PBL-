# Essa parte é apenas para qual menu inicial, onde o usuario seleciona
# se vai configurar o progama, usar a versão padrão(a do problema) 
# ou encerrar o progama
NumOpMenu = int(input('''
-------Menu de inicial---------
                      
1- Para configurar o progama
2- Para usar versão padrão(Evento EngComp da UEFS)
3- Para encerrar o progama
                      
Selecione uma opção: '''))

match NumOpMenu:
# Após o usuario selecionar uma opção alguma das opções será iniciada
    case 1:          
# O progama será configurado pelo usuario e depois
# o progama irá para a tela de vendas
            ingressos = int(input("Digite a quantidade de ingressos: "))
            precoInt = float(input("Digite o preço do ingresso: R$"))
            precoMeia = float(input("Digite o preço da meia-entrada: R$"))
            precoDesc = float(input("Caso aja algum desconto digite-o, caso não digite 0: R$"))
    case 2:
# Versão do problema proposto vai ser selecionada e as os valores
# do problema serão utilizados nas respectivas variáveis
        print("Versão padrão selecionada\n")
        ingressos = 2000
        precoInt = 30      
        precoMeia = 15
        precoDesc = 10
    case 3:
# Encerra o progama
        print("Encerrando progama")
        exit()

# Após selecionar ou a versão ou configurar começa a tela de vendas onde eu pré-criei algumas
# variaveis fora do while para guardar as informações e elas não serem perdidas nos loops

IntVendas = 0
DAcortesias = 0
EstudanteVendas = 0
IdosoVendas = 0
CortesiaVenda = 0
DescontoVendas = 0
EventoFim = 2

while ingressos > 0 and EventoFim > 1:
    NumOpIng = int(input('''
-------Tela de Vendas------

1- Inteira
2- Meia-entrada(Estudante)
3- Meia-entrada(idoso)
4- Descontos
5- Cortesia
                         
Selecione um tipo de ingresso: '''))
# o usuario seleciona qual tipo de ingresso será vendido e pergunta quantos ingressos foram vendidos e soma suas idades com o uma estrutura de repetição, que repetira a pergunta de idade para cada ingresso que foi vendido.
    VendasIng = 0
    VendasIng = int(input("Quantos ingressos foram vendidos? "))
    IdadeSoma = 0
    for idade in range(0,VendasIng):
        idade = int(input("Digite a idade de cada cliente: "))
        IdadeSoma += idade

    Cortesia = VendasIng // 10

    match NumOpIng:
#inteira
        case 1:
            ingressos -= VendasIng
            IntVendas += VendasIng
#meia-estudante
        case 2:
            NumOpTipo = int(input("Todas compras foram mostradas a carteira de estudante?\n1-Sim\n2-Não"))
            if NumOpTipo == 1:
                ingressos -= VendasIng
                EstudanteVendas += VendasIng
            else:
                comprovante = 0
                print("Garanta que todas as compras sejam comprovadas antes de continuar com o cadastro por favor.")
#meia-idoso
        case 3:
            NumOpTipo = int(input("Todas compras foram mostradas a carteira idoso?\n1-Sim\n2-Não"))
            if NumOpTipo == 1:
                ingressos -= VendasIng
                EstudanteVendas += VendasIng
            else:
                comprovante = 0
                print("Garanta que todas as compras sejam comprovadas antes de continuar com o cadastro por favor.")
#desconto
        case 4:
            NumOpTipo = int(input("Todas compras foram mostradas o devido comprovante de desconto?\n1-Sim\n2-Não"))
            if NumOpTipo == 1:
                ingressos -= VendasIng
                EstudanteVendas += VendasIng
            else:
                comprovante = 0
                print("Garanta que todas as compras sejam comprovadas antes de continuar com o cadastro por favor.")
#cortesia DA
        case 5:
            ingressos -= VendasIng
            DAcortesias += VendasIng

    if (ingressos - Cortesia) >= 0:
        ingressos -= Cortesia
        if ingressos > 0:
            print(f"Foram dadas {Cortesia} cortesias\nainda restam {ingressos} ingressos.")
            EventoFim = int(input("Gostaria de encerrar o evento?\n1-Sim\n2-Não"))
        else:
            print(f"Foram dadas {Cortesia} cortesias\nnão restam mais ingressos.")   
    else:
        print(f"Não foi possivel adcionar as as {Cortesia} cortesias,pois restam apenas {ingressos} ingressos.")

RsMeia = ((EstudanteVendas+IdosoVendas)*precoMeia)
RsInt = (IntVendas*precoInt)
RsDesc = (DescontoVendas*precoDesc)
RsTotal = RsMeia + RsInt + RsDesc

VendasIngFinal = IntVendas + EstudanteVendas + IdosoVendas + DescontoVendas + Cortesia

MediaIdade = IdadeSoma / VendasIngFinal

if EstudanteVendas > IdosoVendas and EstudanteVendas > IntVendas and EstudanteVendas > DescontoVendas:
    MaisVendas = "Meia-entrada para estudantes"
elif IdosoVendas > EstudanteVendas and IdosoVendas > IntVendas and EstudanteVendas > DescontoVendas:
    MaisVendas = "Meia-entrada para idosos"
elif DescontoVendas > EstudanteVendas and DescontoVendas > IdosoVendas and DescontoVendas > IntVendas:
    MaisVendas = "Desconto"
else:
    MaisVendas = "Inteira"

print(f'''
Total de ingressos emitidos: {VendasIngFinal};\n 
Ingressos não emitidos: {ingressos};\n 
Total de meia-entradas para estudantes vendidas: {EstudanteVendas};\n
Total de meia-entradas para idosos vendidas: {IdosoVendas};\n
Total de inteiras vendidas: {IntVendas};\n
Total de descontos vendidos: {DescontoVendas};\n
Cortesias para DA e convidados: {DAcortesias};\n
Total de cortesias para vendedores comissionados: {Cortesia};
Total de dinheiro arrecadado: R${RsTotal};\n
Total de dinheiro das meia-entradas: R${RsMeia};\n
Total de dinheiro das inteiras: R${RsInt};\n
Total de dinheiro das descontos: R${RsDesc};\n
Ingresso mais vendido: {MaisVendas};\n
Média de idade dos compradores: {round(MediaIdade, 2)} 
''')
