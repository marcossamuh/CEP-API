import requests

def main():
    cep_input = input('Insira o cep pra pesquisa:')

    if len(cep_input)!=8:
        print('Quantidade de digitos invalida')
        exit()

    req = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    adreess_data = req.json()

    if 'erro' not in adreess_data:
        print('==>CEP ENCONTRADO<==')
        print('CEP:{}'.format(adreess_data['cep']))
        print('LOGRADOURO:{}'.format(adreess_data['logradouro']))
        print('COMPLEMENTO:{}'.format(adreess_data['complemento']))
        print('BAIRRO:{}'.format(adreess_data['bairro']))
        print('LOCALIDADE:{}'.format(adreess_data['localidade']))
        print('UF:{}'.format(adreess_data['uf']))
    else:
        print('Cep Ivalido {}'.format(cep_input))

    option = input('Deseja realizar uma nova consulta? \n1. Sim \n2. Sair')    
    if option == 1:
        main()
    else:
        exit()    

if __name__=='__main__':
    main()
