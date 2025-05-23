# -projeto-final-QA-Alda
Testes Python

## 1. Apresentação
Meu nome é Alda, sou aluno do curso de Gestão de TI no 5º semestre. Durante esta disciplina de Quality Assurance, aprendi sobre os fundamentos dos testes de software e como implementar testes automatizados em Python, focando na qualidade do produto final.

## 2. O que é Quality Assurance (QA)?
QA é o processo de garantir a qualidade do software através de testes sistemáticos e processos bem definidos. É importante porque ajuda a prevenir defeitos, reduzir custos com retrabalho e entregar produtos mais confiáveis aos usuários finais.

## 3. Conceitos Aprendidos Durante o Semestre
Aprendi sobre os diferentes níveis de teste (unitário, integração, sistema), como planejar casos de teste eficientes e a importância da automação. Utilizei ferramentas como Colab para desenvolvimento e GitHub para versionamento. Também entendi como os testes se integram com CI/CD e como métricas ajudam no controle de qualidade.

## 4. Ferramentas e Sites Utilizados
- https://jsonplaceholder.typicode.com/
- https://colab.research.google.com/
- https://github.com/
- https://pytest.org/
- https://docs.python-requests.org/

## 5. Explicação dos Testes Entregues

### ✅ Teste 01 – API Alternativo Funcional
**Biblioteca:** Requests  
**Objetivo:** Testar endpoints CRUD em API real (JSONPlaceholder)  
**Resultado esperado:** Todos os endpoints devem retornar status codes corretos  
**Arquivo:** [testes/teste_01_api_alternativo.py](testes/teste_01_api_alternativo.py)
Link teste 01  https://colab.research.google.com/drive/1JZ24PGhMa6PMQNvQijEP4tQsWcDG_Ed8#scrollTo=HwPx8dNtkV7G&line=1&uniqifier=1


### ✅ Teste 02 – Validação de Schema JSON
**Biblioteca:** requests + jsonschema  
**Objetivo:** Validar estrutura dos dados retornados pela API  
**Resultado esperado:** Resposta deve corresponder exatamente ao schema definido  
**Arquivo:** [testes/teste_02_validacao_schema.py](testes/teste_02_validacao_schema.py)
Link teste 02 https://colab.research.google.com/drive/1JZ24PGhMa6PMQNvQijEP4tQsWcDG_Ed8#scrollTo=sWtGuyFiruAM&line=1&uniqifier=1

### ✅ Teste 03 – Teste de Performance
**Biblioteca:** requests + time  
**Objetivo:** Verificar tempo de resposta da API  
**Resultado esperado:** Tempo < 1s e status 200  
**Arquivo:** [testes/teste_03_performance.py](testes/teste_03_performance.py)
Link testec 03 https://colab.research.google.com/drive/1JZ24PGhMa6PMQNvQijEP4tQsWcDG_Ed8#scrollTo=CZpGeOrDk5J-&line=1&uniqifier=1


Meu notebook Colab. https://colab.research.google.com/drive/1JZ24PGhMa6PMQNvQijEP4tQsWcDG_Ed8?usp=sharing

## 6. Conclusão Final
O aprendizado mais importante foi entender como os testes automatizados podem prevenir erros. Vejo QA como uma área essencial no desenvolvimento de software, e o que mais me chamou atenção foi a validação de schemas, por garantir a integridade dos dados retornados por APIs.
