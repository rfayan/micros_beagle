# micros_beagle

## Instalação do openalpr na BeagleBone  Black 

### openalpr

No repositório de usuário do Arch Linux existe o pacote openalpr, podemos baixar o arquivo PKGBUILD utilizando o comando:

```
git clone https://aur.archlinux.org/openalpr.git
```

Se tentassemos criar o pacode a partir do arquivo iriamos receber uma mensagem de erro dizendo que o pacote é incompatível com a arquitetura.
Para resolver este problema nós alteramos o arquivo PKGBUILD, mais expecificamente a linha onde é especificado a arquitetura do pacote para:

```
arch('armv7h' 'i686' 'x86_64')
```
