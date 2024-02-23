from random import randint

def riscar_texto(texto):
  texto_riscado = ' '
  for letra in texto:
    texto_riscado += letra + '\u0336'
  return texto_riscado


def ver_checklist(lista):
  cont = 0

  for i in lista:
    cont += 1
    print(f'[{cont}]' + i)


checklist, xp, level, xpNecessario = [], 0, 1, 100

while True:
  print('-=' * 20)
  print('MENU DE OPÇÕES'.center(40))
  print('-=' * 20)
  print('1- Ver checklist')
  print('2- Adicionar tarefa a checklist')
  print('3- Concluir tarefa')
  print('4- Limpar checklist')
  print('5- Sair')
  print('-=' * 20)

  opcao = int(input('O que você deseja fazer? '))

  if opcao == 1:
    print('-=' * 20)
    
    if len(checklist) > 0:
      ver_checklist(checklist)
    else:
      print('Não há tarefas na sua checklist')

  if opcao == 2:
    print('-=' * 20)
    
    tarefa = input('Qual tarefa você deseja adicionar? ')
    checklist.append(tarefa)

  if opcao == 3:
      print('-=' * 20)

      if len(checklist) > 0:
        numero = randint(10, 50)
    
        ver_checklist(checklist)
        
        n = int(input('Qual tarefa você concluiu? '))
  
        i = riscar_texto(checklist[n-1])
        checklist[n-1] = i

        xp += numero
        print(f'Você ganhou {numero}XP por ter concluido a tarefa.')
      else:
        print('Não há tarefas pra se concluir.')

  if opcao == 4:
    print('-=' * 20)

    r = input('Tem certeza que deseja limpar a checklist? ').strip().upper()

    if r[0] == 'S':
      checklist.clear()
      print('Checklist limpada com sucesso!')
    elif r[0] == 'N':
      continue

  if opcao == 5:
    break

  if xp >= xpNecessario:
    level += 1
    xp = 0
    xpNecessario += 100

    print(f'Você subiu para o level {level}')
    
