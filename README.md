# Menu Interativo com Suporte a Mouse, Teclado e Tela Touch no Terminal

Este projeto cria um menu interativo no terminal que permite ao usuário navegar entre opções usando o teclado, mouse, ou toques na tela touch. Cada opção executa um comando específico no sistema, podendo ser adaptado para rodar scripts ou comandos personalizados. O menu funciona diretamente no terminal, sendo ideal para uso em **Termux**, especialmente em celulares Android.

## Funcionalidades

- **Navegação com Teclado**: Use as setas para cima e para baixo para escolher uma opção e pressione **Enter** para selecionar.
- **Navegação com Mouse e Tela Touch**: Clique ou toque em uma opção para selecioná-la.
- **Compatível com Windows, Linux e Termux**: Comandos são executados no terminal, adaptando-se ao sistema operacional.

## Dependências

Este programa é desenvolvido em Python e utiliza a biblioteca padrão `curses`, que normalmente está disponível no Python para sistemas Unix.

### Requisitos no Termux

Para rodar este programa no Termux, é necessário instalar o **Python** e o **pacote `ncurses`** para suporte ao `curses`.

1. **Instalar Python**:
   ```bash
   pkg install python
