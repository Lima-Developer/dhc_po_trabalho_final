from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpBinary, value

# ============================
# PARÂMETROS DO PROBLEMA
# ============================

N = 5
projetos = range(1, N+1)

# Orçamento total
B = 500000.0

# Big-M igual ao orçamento
M = B

# Retorno fixo F_i
F = {
    1: 80000,
    2: 60000,
    3: 120000,
    4: 150000,
    5: 50000
}

# Retorno variável P_i
P = {
    1: 0.12,
    2: 0.10,
    3: 0.15,
    4: 0.18,
    5: 0.09
}

# Custo fixo C_i
C = {
    1: 90000,
    2: 70000,
    3: 110000,
    4: 130000,
    5: 60000
}

# Exigências mínimas por área
areas = {
    "Lojas": [1, 3],
    "Marketing": [2, 5],
    "Logistica": [4]
}

L = {
    "Lojas": 60000,
    "Marketing": 40000,
    "Logistica": 30000
}

# ============================
# MODELO
# ============================

prob = LpProblem("Planejamento_Investimentos", LpMaximize)

# Variáveis
y = {i: LpVariable(f"y_{i}", cat=LpBinary) for i in projetos}
x = {i: LpVariable(f"x_{i}", lowBound=0) for i in projetos}

# Função Objetivo
prob += (
    lpSum(F[i] * y[i] for i in projetos) +
    lpSum(P[i] * x[i] for i in projetos)
)

# Restrição de orçamento
prob += lpSum(C[i] * y[i] + x[i] for i in projetos) <= B

# Big-M (acoplamento)
for i in projetos:
    prob += x[i] <= M * y[i]

# Restrição lógica: P3 só se P4 estiver selecionado
prob += y[3] <= y[4]

# Exigências por área
for area_nome, projs in areas.items():
    prob += lpSum(x[i] for i in projs) >= L[area_nome]

# ============================
# SOLVER
# ============================
prob.solve()

# ============================
# RESULTADOS
# ============================

print("Status:", prob.status)
print("Valor ótimo:", value(prob.objective))
print("\nDecisão por projeto:")
for i in projetos:
    print(f"Projeto {i}: y={value(y[i])}, x={value(x[i])}")
