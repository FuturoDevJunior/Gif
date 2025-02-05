# Conversor de Vídeo para GIF com Marca d'Água - DevFerreiraG

Este projeto é um script em Python que converte um vídeo em um GIF animado, adicionando uma marca d'água personalizada ("DevFerreiraG") no vídeo.

## Funcionalidades

- **Conversão de vídeo para GIF:** Converte seu vídeo para GIF especificando parâmetros como FPS, largura e altura.
- **Marca d'água personalizada:** Adiciona uma marca d'água com opacidade ajustável e posição configurável.
- **Redimensionamento dinâmico:** Caso seja informado tamanho de saída, o vídeo é redimensionado.
- **Instalação automática de dependências:** Se o pacote `moviepy` não estiver instalado, o script tenta instalá-lo automaticamente.

## Requisitos

- **Python:** Recomenda-se utilizar uma versão compatível, como Python 3.11, pois a versão atual do Pillow (10.4.0) ainda não fornece binários pré-compilados para Python 3.13 em Windows.
- **ffmpeg:** Certifique-se de que o `ffmpeg` está instalado e incluído no PATH do sistema.
- **Pillow/ MoviePy:** O script instala automaticamente o `moviepy`, que depende do Pillow. No entanto,  
  se você encontrar erros durante a instalação do Pillow (por exemplo, relacionados à ausência de zlib), siga as instruções abaixo.

## Problema com a Instalação do Pillow

Durante a instalação do `moviepy`, a instalação do Pillow pode falhar, especialmente no Python 3.13, devido à falta de pré-compilados e dependências como o zlib. Se você ver mensagens de erro como:

RequiredDependencyException: The headers or library files could not be found for zlib 

## Soluções para o Problema do Pillow

### 1. Utilizar uma Versão do Python Suportada

A solução mais simples e recomendada é utilizar uma versão do Python suportada, como o Python 3.10 ou 3.11. Dessa forma, você terá acesso aos binários pré-compilados do Pillow, evitando a necessidade de compilar a partir do código fonte.

### 2. Instalar Dependências de Compilação (Avançado)

Caso você opte por continuar utilizando o Python 3.13, será necessário instalar os arquivos de cabeçalho e bibliotecas do zlib manualmente. Consulte a [documentação do Pillow](https://pillow.readthedocs.io/en/latest/installation/basic-installation.html) para obter orientações detalhadas.

### 3. Instalar uma Versão Anterior do Pillow

Outra abordagem é instalar uma versão anterior do Pillow que seja compatível com o Python 3.13 (se disponível), por exemplo:

```bash
pip install pillow==9.5.0
```

**Nota:** Verifique a compatibilidade com o `moviepy` antes de optar por esta solução.

## Como Usar

1. **Verifique se o ffmpeg está instalado:**  
   O script verifica se o `ffmpeg` está disponível no sistema. Certifique-se de que o ffmpeg esteja instalado e configurado no PATH.

2. **Execute o Script:**  
   Execute o script pelo terminal, por exemplo:
   ```bash
   python Gif.py caminho/do/video.mp4 gif_saida.gif --fps 10 --width 320 --height 240 --watermark_pos "10,10" --watermark_opacity 0.7 --optimize
   ```

## Considerações Finais

- **Ambiente Virtual:** Recomenda-se utilizar um ambiente virtual para isolar as dependências do projeto.
- O script abortará a execução e exibirá mensagens de erro se ocorrer algum problema, como a ausência do arquivo de vídeo ou do `ffmpeg`.

Boa utilização! 