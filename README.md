# -projeto-final-QA-Alda
Testes Python

## 1. Apresentação
Meu nome é Alda, sou aluno do curso de Gestão de TI no 5º semestre. Durante esta disciplina de Quality Assurance, aprendi sobre os fundamentos dos testes de software e como implementar testes automatizados em Python, focando na qualidade do produto final. Foi uma experiência transformadora entender como os testes sistemáticos podem impactar positivamente o resultado final de um projeto de software.

## 2. O que é Quality Assurance (QA)?
QA, ou Garantia de Qualidade, é o conjunto de processos e atividades que asseguram que um produto de software atenda aos requisitos especificados e às expectativas dos usuários. Através de testes planejados e metodologias bem definidas, o QA ajuda a identificar problemas antes que eles cheguem ao usuário final, economizando tempo e recursos valiosos para a equipe de desenvolvimento. É como um "controle de qualidade" digital que verifica cada parte do sistema para garantir que tudo funcione perfeitamente junto.
## 3. Conceitos Aprendidos Durante o Semestre
Foi um semestre cheio de aprendizado sobre como garantir que um software não só funcione, mas seja bom de verdade. Aqui estão os principais pontos que peguei:

Qualidade no Software
Descobri que qualidade não é só o código rodar sem bugs – tem a ver com o software ser fácil de usar, rápido e fazer exatamente o que o usuário precisa. Basicamente, é entregar algo que não só funciona, mas que as pessoas gostam de usar.

Tipos de Testes
Aprendi que existem vários jeitos de testar:

Testes Unitários: Tipo verificar peça por peça do código, como testar cada função separadamente.

Testes de Integração: Quando junta as peças e vê se elas trabalham bem juntas.

Testes de Sistema: Testar o software inteiro, como se fosse o usuário final.

Planejamento de Testes
Antes, eu só testava "no feeling". Agora aprendi a planejar: criar casos de teste claros, definir o que é "aceitável" e documentar tudo direitinho. Isso evita aquela dor de cabeça de "será que testei tudo?"

Ferramentas que Usei

Google Colab: Pra rodar códigos Python sem complicação.

GitHub: Pra guardar e organizar os projetos (e não perder tudo se o PC der pau).

Bibliotecas Python: requests pra testar APIs, unittest pra automatizar testes.

CI/CD (Integração Contínua)
Vi como dá pra automatizar testes pra rodarem sempre que alguém manda uma atualização pro código. Assim, se algo quebrar, a gente descobre na hora – bem melhor do que o usuário reclamar depois!

Métricas e Dados
Aprendi que números ajudam a entender a qualidade:

Quantos bugs tão aparecendo?

Quanto do código foi testado?
Isso ajuda a tomar decisões melhores, tipo "precisamos testar mais essa parte aqui".


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
Como analista de qualidade atuante, esta disciplina trouxe insights valiosos que complementam meu trabalho diário na Vila Velha Corretora. O aprendizado em automação de testes com Python e validação de dados se conecta diretamente com minhas atividades de homologação de sistemas em C# e análise de relatórios financeiros.

Vejo o QA como uma área em expansão onde minha dupla experiência - operacional e técnica - será cada vez mais valorizada. O conteúdo sobre testes de API e validação de schemas foi especialmente relevante, pois me deu ferramentas para implementar verificações mais robustas nos dashboards do Power BI e relatórios que gerencio.

Estou aplicando esses conhecimentos para:

Documentar casos de teste formais para homologações

Implementar verificações automatizadas de qualidade de dados

Melhorar a comunicação entre times técnicos e operacionais

Pretendo me aprofundar na automação de testes para Crystal Reports e na criação de métricas de qualidade mais precisas - transformando a teoria acadêmica em melhorias tangíveis para meus projetos profissionais.

Esta formação não apenas complementou, mas elevou minha atuação em QA, mostrando como a abordagem sistemática pode agregar valor mesmo em ambientes já consolidados.
