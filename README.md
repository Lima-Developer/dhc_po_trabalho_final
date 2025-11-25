# Sistema de Planejamento de Investimentos

## 📋 Descrição

Este projeto implementa um modelo de **Programação Linear Inteira Mista (MILP)** para otimização de alocação de investimentos em projetos corporativos. O sistema utiliza a biblioteca PuLP para resolver o problema de maximização de retorno sobre investimento, considerando restrições orçamentárias, dependências entre projetos e requisitos mínimos por área.

## 🎯 Problema de Negócio

A empresa possui **5 projetos** distribuídos em três áreas estratégicas:
- **Lojas**: Projetos 1 e 3
- **Marketing**: Projetos 2 e 5
- **Logística**: Projeto 4

### Objetivo
Maximizar o retorno total dos investimentos, que é composto por:
- **Retorno Fixo (F_i)**: Ganho garantido ao selecionar o projeto
- **Retorno Variável (P_i)**: Ganho proporcional ao valor investido

### Restrições
1. **Orçamento total**: R$ 500.000,00
2. **Exigências mínimas por área**:
   - Lojas: R$ 60.000,00
   - Marketing: R$ 40.000,00
   - Logística: R$ 30.000,00
3. **Dependência lógica**: Projeto 3 só pode ser selecionado se o Projeto 4 estiver ativo
4. **Custo fixo**: Cada projeto tem um custo fixo de ativação

## 📊 Dados dos Projetos

| Projeto | Retorno Fixo (F) | Retorno Variável (P) | Custo Fixo (C) | Área |
|---------|-----------------|---------------------|----------------|------|
| 1 | R$ 80.000 | 12% | R$ 90.000 | Lojas |
| 2 | R$ 60.000 | 10% | R$ 70.000 | Marketing |
| 3 | R$ 120.000 | 15% | R$ 110.000 | Lojas |
| 4 | R$ 150.000 | 18% | R$ 130.000 | Logística |
| 5 | R$ 50.000 | 9% | R$ 60.000 | Marketing |

## 🔧 Instalação

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone ou baixe o repositório**
```powershell
git clone URL_DO_Repositorio
```

2. **Crie um ambiente virtual (recomendado)**
```powershell
python -m venv venv
```

3. **Ative o ambiente virtual**
```powershell
.\venv\Scripts\Activate.ps1
```

> **Nota**: Se você receber um erro de política de execução, execute:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

4. **Instale as dependências**
```powershell
pip install pulp
```

### Instalação Alternativa (sem ambiente virtual)
```powershell
pip install pulp
```

## 🚀 Como Rodar

### Método 1: Executar diretamente
```powershell
python modelo_PO_final.py
```

### Método 2: Com ambiente virtual ativo
```powershell
.\venv\Scripts\Activate.ps1
python modelo_PO_final.py
```

### Método 3: Especificando o caminho completo do Python
```powershell
python.exe .\modelo_PO_final.py
```

## 📈 Saída Esperada

Ao executar o programa, você verá uma saída similar a:

```
Status: 1
Valor ótimo: 560000.0

Decisão por projeto:
Projeto 1: y=1.0, x=60000.0
Projeto 2: y=1.0, x=40000.0
Projeto 3: y=1.0, x=0.0
Projeto 4: y=1.0, x=30000.0
Projeto 5: y=0.0, x=0.0
```

### Interpretação dos Resultados

- **Status = 1**: Solução ótima encontrada
- **Valor ótimo**: Retorno total maximizado
- **y_i = 1**: Projeto foi selecionado
- **y_i = 0**: Projeto não foi selecionado
- **x_i**: Valor do investimento variável no projeto

## 🧮 Modelo Matemático

### Variáveis de Decisão
- **y_i**: Variável binária (0 ou 1) indicando se o projeto i é selecionado
- **x_i**: Valor do investimento variável no projeto i (contínua, ≥ 0)

### Função Objetivo
```
Maximizar: Σ(F_i × y_i) + Σ(P_i × x_i)
```

### Restrições

1. **Orçamento Total**:
```
Σ(C_i × y_i + x_i) ≤ B
```

2. **Acoplamento (Big-M)**:
```
x_i ≤ M × y_i, ∀i
```
(Garante que x_i só pode ser positivo se y_i = 1)

3. **Dependência Lógica**:
```
y_3 ≤ y_4
```
(Projeto 3 depende do Projeto 4)

4. **Exigências Mínimas por Área**:
```
Σ(x_i para i ∈ Lojas) ≥ 60.000
Σ(x_i para i ∈ Marketing) ≥ 40.000
Σ(x_i para i ∈ Logística) ≥ 30.000
```

## 📁 Estrutura do Código

```python
# 1. PARÂMETROS DO PROBLEMA
#    - Definição de projetos, orçamento, retornos, custos e áreas

# 2. MODELO
#    - Criação do problema de otimização
#    - Definição de variáveis
#    - Função objetivo
#    - Restrições

# 3. SOLVER
#    - Resolução do problema

# 4. RESULTADOS
#    - Exibição da solução ótima
```

## 🔍 Personalização

Para modificar os parâmetros do problema, edite as seguintes seções em `modelo_PO_final.py`:

### Alterar número de projetos:
```python
N = 5  # Altere para o número desejado
```

### Modificar orçamento:
```python
B = 500000.0  # Altere o valor do orçamento
```

### Ajustar retornos e custos:
```python
F = {1: 80000, 2: 60000, ...}  # Retornos fixos
P = {1: 0.12, 2: 0.10, ...}    # Retornos variáveis
C = {1: 90000, 2: 70000, ...}  # Custos fixos
```

### Modificar exigências por área:
```python
L = {
    "Lojas": 60000,
    "Marketing": 40000,
    "Logistica": 30000
}
```

## 🛠️ Solução de Problemas

### Erro: "No module named 'pulp'"
**Solução**: Instale o PuLP com `pip install pulp`

### Erro: "Cannot run scripts on this system"
**Solução**: Ajuste a política de execução do PowerShell:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Solver não encontrado
**Solução**: O PuLP vem com solver padrão (CBC). Se necessário, instale outros solvers:
```powershell
pip install pulp[cbc]
```

## 📚 Dependências

- **PuLP** (≥ 2.0): Framework de otimização linear e inteira
  - Documentação: https://coin-or.github.io/pulp/

## 👨‍💻 Autores

- Rafael De Andrade Alves
- Vinicius Barros Marinho
- João Victor Fernandes Lima
- João Gabriel Ribeiro Holanda

---

**Desenvolvido com Python e PuLP** 🐍
