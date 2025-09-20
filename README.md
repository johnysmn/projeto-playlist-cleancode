# Clean Code - Python

Este projeto é um exemplo de aplicação Python seguindo princípios de Clean Code, com foco em organização, legibilidade e boas práticas de programação.

## Funcionalidades

- Cadastro de músicas
- Criação de playlists automáticas
- Validação de dados de entrada
- Separação clara entre camadas de **view**, **controller**, **model** e **repository**

## Estrutura de Pastas

```
src/
├── main/
│   └── process_handler.py
├── view/
│   └── song_register_view.py
├── controllers/
│   ├── song_register_controller.py
│   └── playlist_creator_controller.py
├── models/
│   ├── entities/
│   │   └── music.py
│   └── repositories/
│       └── musics_repository.py
```

## Como Executar

1. Instale o Python 3.8 ou superior.
2. Clone este repositório.
3. Execute o arquivo principal:

```bash
python src/main/process_handler.py
```

## Requisitos

- Python 3.8+
- Não há dependências externas (apenas bibliotecas padrão)

## Princípios Utilizados

- **Responsabilidade única:** Cada classe e função tem uma única responsabilidade.
- **Nomes claros:** Classes em PascalCase, funções e variáveis em snake_case.
- **Tratamento de erros:** Uso de exceções para validação de dados.

## Autor

Projeto criado para estudos de Clean Code com Python.
