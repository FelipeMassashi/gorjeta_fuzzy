# Sistema de Inferência Fuzzy para Cálculo de Gorjeta

## Descrição
Este é um projeto que implementa um sistema de inferência fuzzy para determinar a gorjeta em um restaurante com base na qualidade do serviço e da comida. O código utiliza lógica fuzzy para modelar a incerteza e a imprecisão envolvidas nas decisões humanas, tornando-o mais flexível do que os sistemas tradicionais baseados em regras rígidas.

## Contexto
Imagine que você está em um restaurante e deseja calcular a gorjeta apropriada para deixar ao garçom. A qualidade do serviço e da comida são fatores importantes na determinação dessa gorjeta. No entanto, esses fatores são subjetivos e podem variar de pessoa para pessoa. Aqui entra a lógica fuzzy, que permite modelar essa incerteza de forma mais próxima à maneira como os humanos pensam e tomam decisões.

## Lógica Fuzzy
A lógica fuzzy é uma extensão da lógica booleana tradicional, onde as variáveis podem ter valores entre "verdadeiro" e "falso", expressando assim a incerteza e a imprecisão. Em vez de simplesmente verdadeiro ou falso, as variáveis em lógica fuzzy podem ter valores em um intervalo contínuo de 0 a 1, representando o grau de pertinência a um conjunto.

## Funcionamento
1. **Pertinência:**
   - As funções de pertinência são usadas para mapear os valores de entrada (como qualidade do serviço e da comida) em valores de pertinência em um intervalo de 0 a 1.
   - Essas funções definem o quão "verdadeira" uma afirmação é, como "o serviço é bom" ou "a comida é ruim", em relação a um conjunto específico.

2. **Regras Fuzzy:**
   - As regras fuzzy são declarações do tipo "SE... ENTÃO..." que relacionam as variáveis de entrada às variáveis de saída.
   - Essas regras são definidas com base no conhecimento humano e na experiência.

3. **Inferência Fuzzy:**
   - O sistema utiliza as regras fuzzy e os valores de pertinência das variáveis de entrada para determinar os valores de pertinência das variáveis de saída.
   - Isso é feito aplicando as regras fuzzy e combinando os valores de pertinência de maneira apropriada.

4. **Defuzzificação:**
   - A etapa final é a defuzzificação, onde os valores de pertinência das variáveis de saída são convertidos em valores nítidos ou concretos.
   - Isso nos dá um valor específico, como a porcentagem de gorjeta apropriada com base nas entradas fornecidas.

## Instruções de Uso
1. Execute o código Python fornecido em um ambiente que suporte a biblioteca Plotly.
2. Insira valores para a qualidade do serviço e da comida.
3. O sistema calculará a gorjeta apropriada com base nos valores fornecidos.

## Referências
- [Introdução à Lógica Fuzzy](https://en.wikipedia.org/wiki/Fuzzy_logic)
- [Princípios de Sistemas de Inferência Fuzzy](https://www.sciencedirect.com/topics/engineering/fuzzy-inference-system)

