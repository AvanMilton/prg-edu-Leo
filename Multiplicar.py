import random

#iniciando variáveis
pv=10
monstropv=3
n_questao=10

#funções
def definir_atq():
    ataques = ['um soco', 'um chute', 'uma cabeçada', 'uma facada', 'uma mordida']
    tipo_de_atq = ataques[random.randint(0,4)]
    return tipo_de_atq

def definir_mstr():
    monstros = ['Sirenhead', 'Chucky', 'Slenderman', 'IT']
    tipo_de_mrst = monstros[random.randint(0,3)]
    return tipo_de_mrst

def resolver_acao(facao):
    if facao == 'e':
        print('você tenta esquivar')
        print('para conseguir voce precisa acertar essa conta de subtração')
        fdano=conta_sub()
    elif facao == 'd':
        print('você se prepara pra receber o golpe')
        print('para se defender voce precisa acertar essa conta de soma')
        fdano=conta_soma()
    elif facao == 'a':
        print('você resolve atacar')
        print('para conseguir atacar primeiro voce precisa acertar essa conta de multiplicação')
        fdano=conta_mult()
    else:
        print('Você ficou nervoso e não soube o que fazer, o monstro acerta o ataque!')
        fdano=1
    return(fdano)

def conta_sub():    
    x=random.randint(0,10)
    y=random.randint(0,10)
    while x < y:
        x=random.randint(0,10)
    gabarito=x-y
    print ('Quanto é', x, 'menos', y, '?')
    resposta = input()
    if int(resposta) == gabarito:
        print('Resposta certa')
        print('você pula pro lado evitando o ataque')
        return 0
    else:
        print('Resposta errada, você não consegue esquivar e o mostro te acerta')
        return 1

def conta_soma():    
    x=random.randint(0,10)
    y=random.randint(0,10)    
    gabarito=x+y
    print ('Quanto é', x, 'mais', y, '?')
    resposta = input()
    if int(resposta) == gabarito:
        print('Resposta certa')
        print('parabéns, você defende o ataque facilmente')
        return 0
    else:
        print('Resposta errada, você não consegue defender a tempo e o mostro te acerta')
        return 1

def conta_mult():    
    x=random.randint(0,10)
    y=random.randint(0,10)    
    gabarito=x*y
    print ('Quanto é', x, 'vezes', y, '?')
    resposta = input()
    if int(resposta) == gabarito:
        print('Resposta certa')
        print('parabéns, você foi mais rápido e ataca')
        return 2
    else:
        print('Resposta errada, você tenta atacar mas erra, o ataque do monstro acerta você primeiro')
        return 1

#programa
print('Oi Paulo Leonardo')
print('Você está numa arena de batalha, na sua frente aparece ',definir_mstr())

while pv > 0:
    print('ele corra na sua direção e tenta te dar',definir_atq())
    print('o que você vai fazer? esquivar(e), defender(d) ou atacar(a)?')
    acao_combate = input()
    dano=resolver_acao(acao_combate)
    if dano == 1:
        pv=pv-1
    elif dano == 2:
        n_questao=n_questao-1
        monstropv=monstropv-1
        if monstropv == 0:
            print('Parabens, você matou o monstro')
            if n_questao>0:
                print('Mas agora aparece um novo monstro, é o ',definir_mstr())
                monstropv = 3
            else:
                print('Você derrotou os monstros por hoje e sai vitorioso')
                pv=-1
    else:
        n_questao=n_questao-1

if pv==0:
    print('você está cansado demais pra continuar e cai no chão desmaiado')