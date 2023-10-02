try:
  x=float(input('Informe o primeiro valor: '))
  y=float(input('Informe o segundo valor: '))

  operacao= input('Digite: \n + para somar \n - para subtrair \n * para multiplicar ou \n / para dividir' + "\n")

  if operacao =='+':
    resultado = x + y

  elif operacao =='-':
    resultado = x - y

  elif operacao =='*':
    resultado = x * y

  elif operacao =='/':
    resultado = x / y

  else:
    print('Informe uma opração válida!')
except ValueError:
  print("Dados de entrada incorretos")
except ZeroDivisionError:
  print("divisão por zero! Digite um divisor diferente de zero.")
else:
  print("Resultado: ", resultado)
finally:
  print("Obrigada por utilizar nosso sistema!")