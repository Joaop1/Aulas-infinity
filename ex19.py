import math
from math import ceil
areap = float(input("Informe o tamanho da área a ser pintada, em metros quadrados: "))
qtdlatas = (areap/54)
qtdlatas = math.ceil()(qtdlatas,0)
print(f"Quantidade de latas: {qtdlatas}")
valor = qtdlatas*80
print(f"Valor a ser pago: R$ {valor}")