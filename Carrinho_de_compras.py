carrinho = []

while True:
    print('1 - Comprar: ')
    print('2 - Ver carrinho: ')
    print('3 - Remover itens do carrinho: ')
    print('4 - Calcular total da compra: ')
    print('5 - Sair: ')

    opcao = input('Digite a opção: ')
    print('')
    if opcao == "1":
        compras = str(input('Digite o produto: '))
       
        quantidade = []
        quantidade_produto = int(input('Quantidade produto:'))
        quantidade.append(quantidade_produto)

        preco = []
        quantidade_preco = float(input('Preço do produto(R$): '))
        preco.append(quantidade_preco)

        carrinho.append([compras, quantidade_produto, quantidade_preco])
        print('Carrinho feito')
        print('')
    elif opcao == '2':
        if len(carrinho) == 0:
            print("Carrinho vazio.")
        else:
            for produto_quantidade_preco in carrinho:    
                print('/////////////////////////////')
                print('Produto: ', produto_quantidade_preco[0])
                
                print('Quantidade: ', produto_quantidade_preco[1])
                
                print('Preço(R$): ', produto_quantidade_preco[2])
    elif opcao == '3':
        remover_compra = str(input('Digite o item que quer remover: '))
        removido = False

        for produto_quantidade_preco in carrinho:
            if produto_quantidade_preco[0] == remover_compra:
                carrinho.remove(produto_quantidade_preco)
                print('Produto removido')
                print('')
                removido = True
                break
            
        if not removido:
            print('Item não encontrado')
            print('')
    elif opcao == '4':
        if len(carrinho) == 0:
            print('Carrinho vazio')
        else: 
            total = 0

            for produto_quantidade_preco in carrinho:
                total += produto_quantidade_preco[1] * produto_quantidade_preco[2]
                
        print('O total da compra é:R$', total)
        print('')

    elif opcao == '5':
        print('Encerrando o programa...')
        break
    else:
        print('Opção inválida!')
            





