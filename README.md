# Programa de Transcrição de Áudio

Este programa converte arquivos de áudio `.opus` para o formato `.wav` usando `ffmpeg` e, em seguida, transcreve o conteúdo dos arquivos `.wav` para texto utilizando o serviço de reconhecimento de fala do Google através da biblioteca `SpeechRecognition`. O programa processa todos os arquivos `.opus` presentes em um diretório e exibe as transcrições diretamente no console.

## Funcionalidades

- Converte arquivos de áudio `.opus` para o formato `.wav`.
- Transcreve áudio em texto usando o reconhecimento de fala do Google.
- Suporta transcrição em Português Brasileiro.

## Pré-requisitos

Este programa requer Python e as seguintes bibliotecas:

- **pydub**: Para manipulação de áudio.
- **speech_recognition**: Para funcionalidade de reconhecimento de fala.
- **ffmpeg**: Ferramenta externa usada para converter formatos de áudio, acessível via linha de comando.

## Instalando as Bibliotecas

Instale as bibliotecas necessárias usando `pip`:

```shell
pip install pydub speechrecognition
```

## Instalando o FFmpeg

Certifique-se de que o ffmpeg está instalado no sistema. Para Ubuntu:

```shell
sudo apt update
sudo apt install ffmpeg
```

Para Windows ou macOS, siga as instruções no site do [FFmpeg](https://ffmpeg.org/download.html).

## Estrutura de Diretórios

O programa espera a seguinte estrutura de pastas:

```
pasta_do_projeto/
│
├── audios/
│   ├── OPUS/        # Pasta de entrada para os arquivos .opus
│   └── WAV/         # Pasta de saída para os arquivos .wav (criada se não existir)
└── speechtotext.py
```

## Uso

1. Coloque os arquivos `.opus` dentro da pasta `audios/OPUS/`.
2. Execute o script:

```shell
python3 speechtotext.py
```
O programa irá:

- Converter cada arquivo `.opus` em `audios/OPUS/` para o formato `.wav` e salvá-lo em `audios/WAV/`.
- Transcrever cada arquivo `.wav` e imprimir a transcrição no console.

## Visão Geral do Código

- **Caminhos de Arquivos**: O programa define os caminhos para os arquivos de entrada `.opus` e de saída `.wav`.
- **Conversão de Áudio**: Utiliza `ffmpeg` para converter `.opus` em .`wav`.
- **Reconhecimento de Fala**: Transcreve o texto de cada arquivo de áudio e imprime no console.


## Exemplo de Saída

Após a execução do script, o console poderá exibir uma saída semelhante a esta:

```
Transcrição para file1.opus: "Este é o texto transcrito."
Transcrição para file2.opus: "Não foi possível entender o áudio."
```

