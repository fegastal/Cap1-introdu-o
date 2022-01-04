''' Teste seus conhecimentos | Introdução


1. Quais as componentes de base da arquitetura de um computador?

Do ponto de vista da sua dinâmica, um computador executa programas que foram previamente
armazenados na sua memória externa (ex: um disco duro). Esses programas são formados
por instruções, que são transferidas para a memória interna (ex: RAM) e executadas pela
máquina graças à unidade central de processamento  (CPU). Eventualmente, pode haver recurso
à entrada de dados através de dispositivos apropriados (ex: teclado e visualização
de resultados graças aos dispositivos de saída (ex: o monitor). Esta é a arquitetura
dita de Von Neuman, que ainda hoje é predominante.


2. Compiladores e interpretadores: o que são e quais as diferenças entre eles?

O programa começa a ser traduzido pelo compilador num novo programa escrito em linguagem de máquina
(ex: em uma linguagem que aquela arquitetura particular de computador entende). O programa
traduzido é posteriormente executado, havendo lugar, eventualmente, à entrada de dados
e saída de resultados. Já no caso de um recurso a um interpretador, o programa não é todo traduzido.
O que acontece é que cada instrução que o compõe é interpretada e executada de acordo com uma dada
ordem especificada pelo programa.
À velocidade da compilação podemos contrapor a maior facilidade de desenvolvimento ou
a portabilidade quando optamos por um interpretador.
Existem modelos que podemos considerar híbridos: o programa é compilado para código intermédio,
sendo de seguida interpretadas as suas instruções graças a uma máquina virtual. Ex: Java ou Python.


3. O que é um paradigma de programação?

Paradigma de programação é um tipo de estruturação ao qual a linguagem deverá respeitar, a depender do
objetivo proposto. O que vai definir o paradigma utilizado será a tratativa dada ao problema.
É como se você tivesse que resolver um simples problema durante a execução. Há opções mais trabalhosas e opções
mais elegantes e sofisticadas (em termos de código). Assim é a programação: um paradigma pode oferecer
técnicas apropriadas para uma aplicação específica.


4. Que tipo de paradigmas de programação conhece? O que os distingue?

a) Imperativo ou Procedural: as instruções devem ser passadas ao computador na sequência
em que devem ser executadas (foco no "como" resolver o problema). Espécie de passo-a-passo
de procedimentos. Ex: Cobol, Fortran e Pascal.

b) Declarativo: foca mais em “o quê” deve ser resolvido do que, necessariamente, em “como”
isso deve ser feito. Há declarações iniciais de verdades lógicas que são imutáveis.

c) Funcional: o uso de funções é destaque (daí seu nome). É fortemente dependente de uma base
matemática. Assim, subdivide-se o problema proposto e as funções implementadas farão os cálculos
matemáticos. Ao final, a pessoa programadora deve também integrar a solução entregue.
Ex: LISP, o Scheme e o Haskell.

d) Lógico: Utiliza formas de lógica simbólica como padrões de entrada e saída.
A partir daí, realiza inferências para produzir os resultados. QLISP, Mercury e Prolog — esta
última sendo a mais popular de todas. São utilizadas na solução de problemas que envolvem
inteligência artificial, criação de programas especialistas e comprovação de teoremas.

e) Orientada a Objetos: Década de 90 (Java). Resolver gargalos da indústria de software, como produzir
programas de forma mais rápida, com maior confiabilidade e a um custo menor. Para isso, buscou apoiar-se
nas características de classe e objeto ao tentar retratar a programação tal qual se enxerga o mundo real.
Segundo esse paradigma, todos os objetos têm determinados estados e comportamentos. Esses estados
são descritos pelas classes como atributos. Já a forma como eles se comportam (sua funcionalidade)
é definida por meio de métodos, que são equivalentes às funções do paradigma funcional.
Possui três alicerces básicos, que são conceito de herança, polimorfismo e encapsulamento.
Alguns exemplos de linguagens orientadas a objetos são Java, C++, C# e Python.

f) Orientado a eventos: Usado por toda linguagem de programação que tem uso de recursos gráficos,
como jogos e formulários. Imagine uma caixa de formulário que precisa do preenchimento do
usuário. Os eventos descritos no código fonte serão executados à medida que se realiza o
preenchimento dos campos solicitados. Além disso, ocorrem execuções também quando se decide
enviar os dados clicando no botão de envio. São eventos que disparam outros eventos.
Obs: é um diferencial no mercado de trabalho.


5. O que são módulos, expressões, instruções e objetos?

a) Módulos: um objeto que serve como uma unidade organizacional de código Python.
Os módulos têm um espaço de nomes contendo objetos Python arbitrários. Os módulos são
carregados pelo Python através do processo de importação.

b) Expressão: uma parte da sintaxe que pode ser avaliada para algum valor. Em outras palavras,
uma expressão é a acumulação de elementos de expressão como literais, nomes, atributos de acesso,
operadores ou chamadas de funções, todos os quais retornam um valor. Em contraste com muitas outras
linguagens, nem todas as construções de linguagem são expressões. Também existem instruções, as quais
não podem ser usadas como expressões, como, por exemplo, while. Atribuições também são instruções, não expressões.

c) Instruções: uma instrução é parte de uma suíte (um “bloco” de código). Uma instrução é ou uma
expressão ou uma de várias construções com uma palavra reservada, tal como if, while ou for.

d) Objetos: Tudo em Python é objeto. Existem alguns tipos de objetos, como:

_ objeto byte ou similar _
Um objeto com suporte ao o Protocolo de Buffer e que pode exportar um buffer C contíguo.
Isso inclui todos os objetos bytes, bytearray e array.array, além de muitos objetos memoryview comuns.
Objetos byte ou similar podem ser usados para várias operações que funcionam com dados binários; isso
inclui compactação, salvamento em um arquivo binário e envio por um soquete. Algumas operações precisam
que os dados binários sejam mutáveis. A documentação geralmente se refere a eles como “objetos byte
ou similar para leitura e escrita”. Exemplos de objetos de buffer mutável incluem bytearray e um
memoryview de um bytearray. Outras operações exigem que os dados binários sejam armazenados em objetos
imutáveis (“objetos byte ou similar para somente leitura”); exemplos disso incluem bytes e a
memoryview de um objeto bytes.

_ objeto arquivo _
Um objeto que expõe uma API orientada a arquivos (com métodos tais como read() ou write()) para um recurso subjacente).
Dependendo da maneira como foi criado, um objeto arquivo pode mediar o acesso a um arquivo real
no disco ou outro tipo de dispositivo de armazenamento ou de comunicação (por exemplo a entrada/saída
padrão, buffers em memória, soquetes, pipes, etc.). Objetos arquivo também são chamados de objetos
arquivo ou similares ou fluxos.
Atualmente há três categorias de objetos arquivo: arquivos binários brutos,
arquivos binários em buffer e arquivos textos. Suas interfaces estão definidas no módulo io.
A forma canônica para criar um objeto arquivo é usando a função open().


6. O que entende por parâmetros formais?

Parâmetro é uma entidade nomeada na definição de uma função (ou método) que específica um argumento
(ou em alguns casos, argumentos) que a função pode receber.

Parâmetros podem especificar tanto argumentos opcionais quanto obrigatórios,
assim como valores padrão para alguns argumentos opcionais.

Parâmetros formais são as variáveis declaradas no cabeçalho do subprograma.
Parâmetros reais são as variáveis passadas no instante da chamada do subprograma. Existem cinco tipos de parâmetros:

a) posicional-ou-nomeado: especifica um argumento que pode ser tanto posicional quanto nomeado.
Esse é o tipo padrão de parâmetro, por exemplo foo e bar a seguir:
def func(foo, bar=None): ...

b) somente-posicional: especifica um argumento que pode ser fornecido apenas
por posição. Parâmetros somente-posicionais podem ser definidos incluindo o
caractere / na lista de parâmetros da definição da função após eles, por exemplo
posonly1 e posonly2 a seguir:
def func(posonly1, posonly2, /, positional_or_keyword): ...

c) somente-nomeado: especifica um argumento que pode ser passado para a função somente por nome.
Parâmetros somente-nomeados podem ser definidos com um simples parâmetro var-posicional ou
um * antes deles na lista de parâmetros na definição da função, por exemplo kw_only1 and kw_only2 a seguir:
def func(arg, *, kw_only1, kw_only2): ...

d) var-posicional: especifica que uma sequência arbitrária de argumentos posicionais pode ser
fornecida (em adição a qualquer argumento posicional já aceito por outros parâmetros). Tal
parâmetro pode ser definido colocando um * antes do nome do parâmetro, por exemplo args a seguir:
def func(*args, **kwargs): ...

e) var-nomeado: especifica que, arbitrariamente, muitos argumentos nomeados podem ser fornecidos
(em adição a qualquer argumento nomeado já aceito por outros parâmetros). Tal parâmetro pode definido
colocando-se ** antes do nome, por exemplo kwargs no exemplo acima.


7. O que faz a instrução de atribuição (=)?

Define ou re-define o valor armazenado no local de armazenamento indicado por um nome de variável.
Na maioria das linguagens de programação imperativas o comando de atribuição é uma das declarações básicas.
A instrução de atribuição muitas vezes permite que o mesmo nome de variável possa conter valores diferentes
em momentos diferentes durante a execução do programa.


7. O que são estruturas de controle?

São utilizadas para modificar o fluxo linear de um programa. Sem elas, o nosso programa iria executar uma
instrução após outra sempre no sentido início->fim. Com as estruturas de controle podemos decidir ir
por diferentes caminhos, seja realizar um laço localizado, voltar ao inicio, pular algumas instruções
em função de algum evento que ocorreu, etc.


8. Que instruções de controlo conhece e para que servem?

if -> se uma dada condição for verdade , executa um trecho de código.
else -> se a condição anterior for falso, executa outro trecho.
for -> dentro de um for, você pode sair imediatamente com um break.

elif -> serve para quando você está testando mais de uma condição,
na forma “se este caminho não for válido, este outro é”?

while -> enquanto uma dada condição for válida, fica executando um laço.

continue -> volta o controle ao topo do laço, pode ser utilizado em laços while e for.

for -> repete um laço por um determinado número de vezes.

try -> tente executar uma função. se não der erro execute a função e o código associado,
em caso de erro except executa outro trecho de código. Ao final do trecho do try ou do except execute
o trecho de código que estiver após o label finally.

with -> combina um conjunto de try e finally numa maneira elegante e sucinta.


9. O que entende pelo modelo PCAP?

Quando pensamos em linguagem de programação, a maneira de ver baseada nas ideias de Primitivas,
Composição, Abstração e Padrões (PCAP), pode ser instanciada tendo em atenção duas componentes (processos e dados).
A apresentação da linguagem Python e o modo como podemos construir programas será feito de acordo com a
identificação destes quatro aspectos, caminhando do mais simples (primitivas) para o mais complexo (padrões).

primitivas -> +, *, <= (números, cadeias, caracteres)
composição -> if, for (listas, dicionários e conjuntos)
abstração -> def (tipos de dados abstratos, classes)
padrões -> funções de segunda ordem (funções genéricas)

10. O que entende por ciclo lê-avalia-escreve?

No modo interativo, o interpretador funciona num ciclo conhecido por lê-avalia-escreve (read-eval-print): é lida
uma expressão (read), é determinado o valor associado à expressão (eval) e é visualizado o resultado (escreve).
Quando compomos objetos e operações, formamos expressões.

'''