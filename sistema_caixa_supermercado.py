# Sistema de Caixa de SuperMercado

print("=== BEM-VINDO AO SUPERMERCADO PYTHON ===")

total = 0.0
continuar = "s"

while continuar == "s":
    produto = input("\nDigite o nome do produto: ")
    preco = float(input(f"Preço do {produto}: R$ "))
    total += preco

    continuar = input("Você deseja adicionar mais produtos? (s/n): ").lower().strip()

# Cálculo do desconto
if total >= 200:
    desconto = total * 0.10
elif total >= 100:
    desconto = total * 0.05
else:
    desconto = 0

# Total final
total_final = total - desconto

# Exibição dos valores
print("\n=== RESUMO DA COMPRA ===")
print(f"Total da compra: R$ {total:.2f}")
print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_final:.2f}")

# Pagamento e troco
pago = float(input("\nValor pago pelo cliente: R$ "))
troco = pago - total_final

print(f"Troco: R$ {troco:.2f}")

print("\nCompra finalizada com sucesso!")
print("Volte sempre ao SuperMercado Python 🛒")