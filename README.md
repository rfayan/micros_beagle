# micros_beagle

## Instalação do openalpr na BeagleBone  Black 

### openalpr

No repositório de usuário do Arch Linux existe o pacote openalpr, podemos baixar o arquivo PKGBUILD utilizando o comando:

```
git clone https://aur.archlinux.org/openalpr.git
```

Se tentassemos criar o pacodte a partir do arquivo (com o comando `makepkg`) iriamos receber uma mensagem de erro dizendo que o pacote é incompatível com a arquitetura.

Para resolver este problema nós alteramos o arquivo PKGBUILD, mais expecificamente a linha onde é especificado a arquitetura do pacote para:

```
arch('armv7h' 'i686' 'x86_64')
```

Fazendo isso, fomos aptos a rodar o `makepkg` e receber apenas o erro que faltam dependências.

### Dependências

Na prórpria página do pacote `openalpr` as dependências são listadas. Elas são

- beanstalkd
- curl
- leptonica
- log4cplus
- opencv
- tesseract
- cmake

Os pacotes `curl`, `cmake` e `opencv` podem ser instalados facilmente com o comando:

```
sudo pacman -S curl cmake opencv
```

As outras dependências também não tem compatibilidade com ARM, então temos que baixar o arquivo PKGBUILD e alterar a mesma linha já citada antes para que possamos compilar os pacotes.

Como o pacote `tesseract` depende do pacote `leptonica` deve-se instalar `leptonica` antes.
