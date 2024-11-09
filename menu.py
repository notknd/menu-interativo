import curses
import os
import platform

def executar_comando(opcao):
    if opcao == 0:
        comando = "nmap localhost"  # Comando para Opção 1
    elif opcao == 1:
        comando = "ping -c 4 google.com"  # Comando para Opção 2
    elif opcao == 2:
        comando = "ls -l"  # Comando para Opção 3
    elif opcao == 3:
        return  # Sair do programa
    else:
        comando = ""
    
    if comando:
        if platform.system() == "Windows":
            os.system(f'cmd /c {comando}')
        else:
            os.system(comando)

def mostrar_menu(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    # Define as opções do menu com seus respectivos ícones
    menu = [
        ("nmap", " 🌐 "),     # Rede
        ("ping", " 📶 "),     # Conexão
        ("listar", " 📂 "),   # Pasta
        ("Sair", " ❌ ")               # Sair
    ]
    opcao_selecionada = 0

    # Habilita o uso do mouse em curses
    curses.mousemask(1)
    curses.mouseinterval(0)

    # Dimensões e espaçamento dos botões
    button_width = 20
    button_height = 5
    padding = 3

    while True:
        stdscr.clear()

        # Organize as opções em uma grade de 2x2
        for idx, (opcao, icone) in enumerate(menu):
            row = idx // 2  # Linha para organizar em 2x2
            col = idx % 2   # Coluna para organizar em 2x2

            # Calcula a posição x e y para cada botão
            x = col * (button_width + padding)
            y = row * (button_height + padding)

            # Configura estilo do botão selecionado
            if idx == opcao_selecionada:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y + 1, x + 3, f"{icone.center(button_width - 2)}")
                stdscr.addstr(y + 3, x + 3, f"[{opcao.center(button_width - 2)}]")
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y + 1, x + 3, f"{icone.center(button_width - 2)}")
                stdscr.addstr(y + 3, x + 3, f" {opcao.center(button_width - 2)} ")

        # Atualiza a tela
        stdscr.refresh()

        # Lê a entrada do usuário
        key = stdscr.getch()

        # Navegação com teclado
        if key == curses.KEY_UP and opcao_selecionada > 1:
            opcao_selecionada -= 2
        elif key == curses.KEY_DOWN and opcao_selecionada < 2:
            opcao_selecionada += 2
        elif key == curses.KEY_LEFT and opcao_selecionada % 2 != 0:
            opcao_selecionada -= 1
        elif key == curses.KEY_RIGHT and opcao_selecionada % 2 == 0:
            opcao_selecionada += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if opcao_selecionada == 3:
                break  # Sair
            executar_comando(opcao_selecionada)
        elif key == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()
            # Verifica se o clique foi em algum dos botões
            for idx, (opcao, _) in enumerate(menu):
                row = idx // 2
                col = idx % 2
                x = col * (button_width + padding)
                y = row * (button_height + padding)
                
                # Detecta o clique dentro da área do botão
                if y <= my < y + button_height and x <= mx < x + button_width:
                    if idx == 3:
                        return  # Sair
                    executar_comando(idx)

# Configuração de cores para o menu
curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)

# Executa o menu
curses.wrapper(mostrar_menu)
