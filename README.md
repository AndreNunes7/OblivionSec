# OblivionSec

OblivionSec é uma ferramenta de cybersecurity desenvolvida para realizar diversas atividades de teste de segurança, como parsing de HTML, banner grabbing, ataques DoS, scanning de portas, knocking de portas, consultas WHOIS e DNS scanning. A ferramenta foi criada com o objetivo de auxiliar em testes de penetração e análise de vulnerabilidades em redes e sistemas.

## Funcionalidades

- **Parsing HTML**: Extrai e resolve URLs de uma página HTML.
- **Banner Grabbing**: Captura banners de serviços em portas específicas.
- **DoS Attack**: Realiza ataques de negação de serviço (DoS) em servidores web e FTP.
- **Port Scanning**: Escaneia portas de um IP alvo para identificar serviços abertos.
- **Whois**: Consulta informações WHOIS de domínios.
- **Port Knocking**: Realiza port knocking para abrir portas protegidas.
- **DNS Scan**: Realiza scanning de DNS para identificar subdomínios e servidores DNS.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `requests`
  - `beautifulsoup4`
  - `socket`
  - `threading`
  - `signal`
  - `time`
  - `random`
  - `string`
  - `os`
  - `re`
  - `urlparse`

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/AndreNunes7/OblivionSec.git
````

2. Navegue até o diretório do projeto:
``` bash
cd OblivionSec
```

3. Instale as dependências necessárias:
``` bash
pip install -r requirements.txt
```

### Uso
- Execute o script principal para iniciar a ferramenta:
``` bash
python oblivionsec.py
``` 

### Menu Principal

Ao executar o script, você verá o menu principal com as seguintes opções:

![image](https://github.com/user-attachments/assets/feae37b0-3e56-4e99-9559-2c77e3ea2a55)


Selecione a opção desejada digitando o número correspondente e siga as instruções na tela.

- **Parsing HTML**
  Digite uma URL para extrair e resolver URLs contidas na página HTML.

- **Banner Grabbing**
  Digite um IP e uma porta para capturar o banner do serviço.

- **DoS Attack**
  Escolha entre atacar um servidor web ou FTP e siga as instruções para iniciar o ataque.

- **Port Scanning**
  Digite um IP para escanear as portas abertas.

- **Whois**
  Digite um domínio para consultar informações WHOIS.

- **Port Knocking**
  Digite um IP e uma sequência de portas para realizar port knocking.

- **DNS Scan**
  Digite um domínio para realizar scanning de DNS e identificar subdomínios.




**Aviso Legal:** OblivionSec foi desenvolvida para fins educacionais e de teste de segurança. O uso desta ferramenta para atividades maliciosas ou ilegais é estritamente proibido. O autor não se responsabiliza por qualquer uso indevido da ferramenta.



**Contribuições:** Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests no repositório.

