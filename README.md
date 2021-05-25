# adm-professor
Um programa de gestão escolar voltado ao professor, rode localmente e facilite sua vida.
### instale as dependências:
- __MySql Server__:
    - Windows:
      |__Versão__|__links__|
      |:---|:---|
      |Oficial --community (clique na segunda opção)|[mysql-installer-community-8.0.25.0.msi](https://dev.mysql.com/downloads/installer/)|
      |Xampp|[Pagina de downloads](https://www.apachefriends.org/download.html)|
      |Chocolatey --community-server|[Página do download](https://community.chocolatey.org/packages/mysql)|
    - Ubuntu:
      |__Versão__|__links__|
      |:---|:---|
      |Xamp|[Pagina de downloads](https://www.apachefriends.org/download.html)|
      |Apt-get|```sudo apt-get install mysql-community-server```|
- __Python3__:
    - __[https://www.python.org/downloads/](https://www.python.org/downloads/)__
- __Bibliotecas do Python3__:
    - windows `pip install -r requirements.txt` || linux `pip3 install -r requirements` <br> 
    ou se preferir, acesse os links [Flask](https://pypi.org/project/Flask/) e [Mysql connector](https://pypi.org/project/mysql-connector-python/) ainda se preferir ative o ambiente virtual com os comandos <br>`[source] bin/activate`

### Configurando:
Após instalar e configurar o servidor mysql, crie um database chamado __escola__.
Abra o arquivo __configurar.ini__ e insira as configurações de seu servidor.
 ```ini
[BASE]
server = localhost
password = sua-senha
database = escola
user = root
 ```
Tudo pronto agora rode o servidor `server.bat` para Windows ou  `server.sh` para Linux.
 
### Abrindo:
Abra qualquer browser e navegue para `localhost:5000`.
As paginas são intuitivas com pequenos blocos de explicação, leia e faça tudo com atenção.
 
    
    
