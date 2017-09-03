# micros_beagle

## Instalação do openalpr na BeagleBone Black

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

### Compilando openalpr

Executamos o comando `makepkg` para compilar o pacote `openalpr`e cirar um pacote para o Arch Linux.

Obtivemos o seguinte erro:

```
In file included from /usr/include/tesseract/ltrresultiterator.h:26:0,
                 from /usr/include/tesseract/resultiterator.h:26,
                 from /usr/include/tesseract/baseapi.h:31,
                 from /home/alarm/openalpr/src/openalpr-2.3.0/src/openalpr/ocr/tesseract_ocr.h:36,
                 from /home/alarm/openalpr/src/openalpr-2.3.0/src/openalpr/ocr/tesseract_ocr.cpp:20:
/usr/include/tesseract/unichar.h:164:10: error: ‘string’ does not name a type; did you mean ‘stdin’?
   static string UTF32ToUTF8(const std::vector<char32>& str32);
          ^~~~~~
          stdin
make[2]: *** [openalpr/CMakeFiles/openalpr.dir/build.make:375: openalpr/CMakeFiles/openalpr.dir/ocr/tesseract_ocr.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:587: openalpr/CMakeFiles/openalpr.dir/all] Error 2
make: *** [Makefile:152: all] Error 2
==> ERROR: A failure occurred in build().
    Aborting...
```

Para solucionar tivemos que editar o arquivo `/usr/include/tesseract/unichar.h`e adicionar logo antes dos `includes` as seguintes linhas:

```
#include <string>
using std::string ;
```

### Captura de Imagens

Para o desenvolvimento do projeto, utilizamos para a captura de imagens a camera ODROID USB-CAM 720P, que foi conectada ao port USB presente na placa de desenvolvimento Beagle Bone Black. Caso o periférico tenha sido reconhecido pelo sistema operacional, o sistema deve criar uma pasta em `/dev/video0`. Para verificar se a placa foi reconhecida com sucesso, basta executar o seguinte comando no terminal:

```
ls -ltrh /dev/video*
```

O comando acima deve retornar uma resposta similar a isto:

```
crw-rw---- 1 root video 81, 0 Aug 16 09:20 /dev/video0
```
Feito isto, a próxima etapa realizada foi instalar o software necessário para que a camera capture imagens e armazene-as em formato .jpg. Para isso, foi necessário instalar o pacote `fswebcam`. Para distribuições baseadas em Ubuntu, basta realizar o seguinte comando no terminal da placa:

```
sudo apt-get install fswebcam
```

Para distribuições baseadas em Arch Linux é preciso realizar o comando abaixo:

```
sudo pacman -S fswebcam
```

Após a instalação, a captura de imagens pode ser feita através da execução do seguinte comando:

```
fswebcam -r 640x480 -D 1 --no-banner --jpeg 50 /home/alarm/jsmpeg/shot.jpg
```

O comando acima solicita a execução do comando `fswebcam` para captura de imagem pela camera conectada no port USB da BeagleBone Black. Caso esteja sendo utilizada uma outra placa de desenvolvimento com mais de uma camera conectada, deve-se especificar o dispositivo através do argumento `-d /dev/video0`. Os restantes dos argumentos, em ordem de escrita, se referem a resolução da imagem a ser capturada `-r 640x480`, delay de captura da imagem após a execução do comando `-D 1`, remove o banner da imagem `--no-banner`, especifica o formato de imagem ao capturar a imagem e sua qualidade `--jpeg 50` e o último argumento especifica a pasta em que a imagem será armazenada e o nome do arquivo `/home/alarm/jsmpeg/shot.jpg`.

