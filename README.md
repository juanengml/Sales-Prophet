# Sales Prophet

![](src/SalesProphetV1.png)

## Descrição do Projeto

Sales Prophet é um projeto para controle e previsão de vendas. Ele possui recursos para cadastro de vendas, consultas, atualização e exclusão. Além disso, conta com um sistema de previsão de vendas que utiliza as bibliotecas do Facebook.


## Como Executar

Para executar o projeto, é necessário ter o Docker instalado na sua máquina. Em seguida, basta seguir os passos abaixo:

1. Clone o repositório para a sua máquina:

``` bash
git clone https://github.com/seu-usuario/sales-prophet.git

```

2. Acesse a pasta do projeto:

``` bash
$ cd  sales-prophet

```

3. Para Iniciar o Backend, execute o seguinte comando: 

``` bash
$ make backend-start

```
4. Para Iniciar o frontend, execute o seguinte comando: 

``` bash
$ make frontend-start

```

5. Pronto! Agora você pode acessar o sistema em **http://localhost:8501**

6. Caso deseje parar a execução, execute os seguintes comandos:

``` bash
make backend-stop
```

7. Para parar o frontend:

``` bash
make frontend-stop
```

8. Para parar ambos:

``` bash
make stop
```

## Autor 

* Juan Marinho(juanengml@gmail.com)
