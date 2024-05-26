
<p align="center">
  <a href="https://github.com/AyslanBatista/encryptdef">
    <img src="/assets/logo_encryptdef.jpg" alt="encryptdef" style="width: 80%; height: auto;">
  </a>
</p>

<p align="center">
<a href="https://github.com/AyslanBatista/encryptdef?tab=Unlicense-1-ov-file#readme" target="_blank">
    <img src="https://img.shields.io/badge/license-MIT-007EC7.svg?color=%2334D058" alt="License">
</a>
</p>

---
**Encryptdef** é uma ferramenta de linha de comando em Python para encriptar e desencriptar dados e arquivos de forma segura, utilizando criptografia de última geração e uma chave de criptografia fornecida pelo usuário. Proteja suas informações confidenciais e arquivos importantes contra acesso não autorizado com o Encryptdef.

### Como Funciona

Encryptdef utiliza o método de criptografia **AES GCM (Galois/Counter Mode)** com chave derivada pelo algoritmo **Scrypt**, fornecendo uma camada de segurança robusta para seus dados.

#### Detalhes Técnicos
- **AES (Advanced Encryption Standard)**: Algoritmo de criptografia seguro e amplamente utilizado.
- **GCM (Galois/Counter Mode)**: Modo de operação que oferece confidencialidade e integridade dos dados.
- **Scrypt**: Função de derivação de chave resistente a ataques de força bruta, intensiva em memória e computacionalmente cara.

## Instalação
1. Clone o repositório:
```bash
git clone https://github.com/AyslanBatista/encryptdef.git
```
2. Navegue até o diretório do projeto:
```bash
cd encryptdef
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso:
- Dentro do diretório encryptdef, rode o comando:
```bash
python3 __main__.py
```

## Encriptar/Desencriptar Dados:

<code><b>Importante: Mantenha a chave de encriptação em segredo e não a perca. Sem a chave correta, não será possível desencriptar os dados ou arquivos.</b></code>

##### 🔒 ENCRIPTAÇÃO

1. Escolha a opção `1`.

```bash
 [E N C R I P T A Ç Ã O] / [D E C R I P T A Ç Ã O] ?

 [1] 🔒 ENCRIPTAÇÃO.
 [2] 🔓 DECRIPTAÇÃO.

 [?] : 1
 ```

2. Digite os dados que deseja encriptar.
3. Digite a chave que será usada para desencriptar esses dados.

 ```bash
 🔒 [E N C R I P T A Ç Ã O]

 [!] 🔠 DEGITE A INFORAMAÇÃO QUE DESEJA ENCRYPTA: encriptando essa frase
 [!] 🔑 DEGITE A KEY PARA ENCRIPTAÇÃO:12345

 [-] 🔒 ENCRIPTADO: Vrq94RCrSK8RTo6ZcI/ZeTkDttCgRQ==*NDqpAuKi6JbhylWKghksDA==*FLCQDFgq+qbtaLGvjHt0lA==*FLRIxTFgf0lYIwtaz7xx1A==
 [-] 🔑 KEY: 12345

 [?] PRESSIONE ENTER PARA CONTINUAR, OU QUALQUER TECLA PARA SAIR:
 ```


 ##### 🔑 DECRIPTAÇÃO
1. Escolha a opção `2`.

```bash
 [E N C R I P T A Ç Ã O] / [D E C R I P T A Ç Ã O] ?

 [1] 🔒 ENCRIPTAÇÃO.
 [2] 🔓 DECRIPTAÇÃO.

 [?] : 2
```
2. Digite os dados encriptados.
3. Digite a chave usada para encriptar os dados.

```bash
 🔓 [D E C R I P T A Ç Ã O]

 [!] 🔠 DEGITE O TEXTO ENCRIPTADO: Vrq94RCrSK8RTo6ZcI/ZeTkDttCgRQ==*NDqpAuKi6JbhylWKghksDA==*FLCQDFgq+qbtaLGvjHt0lA==*FLRIxTFgf0lYIwtaz7xx1A==
 [!] 🔑 DEGITE A KEY DA ENCRIPTAÇÃO:12345

 🔐 [D E C R I P T A N D O. . .]


 [!] 🔓 DECODIFICADO: encriptando essa frase
 [!] 🔑 KEY: 12345

 [?] PRESSIONE ENTER PARA CONTINUAR, OU QUALQUER TECLA PARA SAIR:
```


## Encriptar/Desencriptar Arquivos:
##### 🔒 ENCRIPTAÇÃO

1. Escolha a opção `1`.

```bash
 [E N C R I P T A Ç Ã O] / [D E C R I P T A Ç Ã O] ?

 [1] 🔒 ENCRIPTAÇÃO.
 [2] 🔓 DECRIPTAÇÃO.

 [?] : 1
 ```
1. Digite o nome do arquivo que deseja encriptar _(o arquivo deve estar na raiz do programa)_.

2. Digite a chave que será usada para desencriptar os dados do arquivo.

3. Digite um nome para o arquivo encriptado que será gerado.

```bash
 [file] 📄 DIGITE O NOME DO ARQUIVO QUE DESEJA ENCRIPTAR: teste
 [key] 🔑 DEGITE A KEY PARA ENCRIPTAÇÃO: 123
 [new-file] 🔒📄 DIGITE O NOME PARA O NOVO ARQUIVO ECRIPTADO: encript-teste

 🔒 [A R Q U I V O -- E N C R I P T A D O]

 /tmp/encript-teste

 [?] PRESSIONE ENTER PARA CONTINUAR, OU QUALQUER TECLA PARA SAIR:
```

 ##### 🔑 DECRIPTAÇÃO
1. Escolha a opção `2`.

```bash
 [E N C R I P T A Ç Ã O] / [D E C R I P T A Ç Ã O] ?

 [1] 🔒 ENCRIPTAÇÃO.
 [2] 🔓 DECRIPTAÇÃO.

 [?] : 2

```
1. Digite o nome do arquivo que deseja decriptar _(o arquivo deve estar na raiz do programa)_.

2. Digite a chave usada para encriptar os dados do arquivo.

3. Digite um nome para o arquivo decriptado que será gerado.
```bash
 [file] 🔒📄 DIGITE O NOME DO ARQUIVO ENCRIPTADO: encript-teste
 [key] 🔑 DEGITE A KEY DA ENCRIPTAÇÃO: 123
 [new-file] 📄 DIGITE O NOME PARA O NOVO ARQUIVO DECRIPTADO: testando

 🔓 [A R Q U I V O -- D E C R I P T A D O]

 📄 /tmp/testando

 [?] PRESSIONE ENTER PARA CONTINUAR, OU QUALQUER TECLA PARA SAIR:
```

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Para contribuir, siga estas etapas:

1. Faça um fork do projeto.
2. Crie uma nova branch: `git checkout -b minha-nova-feature`.
3. Faça suas alterações e adicione commits: `git commit -am 'Adiciona nova feature'`.
4. Faça push para a branch: `git push origin minha-nova-feature`.
5. Abra um Pull Request no GitHub.

Obrigado por contribuir!

