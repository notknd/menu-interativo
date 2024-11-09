import curses
import os
import platform

def executar_comando(opcao):
    comandos = {
        0: "nmap localhost",
        1: "ping -c 4 google.com",
        2: "ls -l"
    }
    comando = comandos.get(opcao, "")
    if comando:
        os.system(f'cmd /c {comando}' if platform.system() == "Windows" else comando)

def mostrar_menu_compacto(stdscr):
    curses.curs_set(0)
    menu = ["nmap", "ping", "listar", "Sair"]
    opcao_selecionada = 0

    while True:
        stdscr.clear()
        for idx, opcao in enumerate(menu):
            if idx == opcao_selecionada:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(idx + 2, 5, f"> {opcao}")
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(idx + 2, 5, f"  {opcao}")
        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_UP and opcao_selecionada > 0:
            opcao_selecionada -= 1
        elif key == curses.KEY_DOWN and opcao_selecionada < len(menu) - 1:
            opcao_selecionada += 1
        elif key in [10, 13]:
            if opcao_selecionada == 3:
                break
            executar_comando(opcao_selecionada)

def mostrar_menu_completo(stdscr):
    curses.curs_set(0)
    curses.mousemask(1)
    curses.mouseinterval(0)
    stdscr.clear()
    stdscr.refresh()

    menu = [
        ("nmap", " 🌐 "),
        ("ping", " 📶 "),
        ("listar", " 📂 "),
        ("Sair", " ❌ ")
    ]
    opcao_selecionada = 0
    button_width, button_height, padding = 20, 5, 3

    while True:
        stdscr.clear()
        for idx, (opcao, icone) in enumerate(menu):
            row, col = divmod(idx, 2)
            x, y = col * (button_width + padding), row * (button_height + padding)
            is_selected = idx == opcao_selecionada
            stdscr.attron(curses.color_pair(1 if is_selected else 2))
            stdscr.addstr(y + 1, x + 3, icone.center(button_width - 2))
            stdscr.addstr(y + 3, x + 3, f"[{opcao.center(button_width - 2)}]" if is_selected else f" {opcao.center(button_width - 2)} ")
            stdscr.attroff(curses.color_pair(1 if is_selected else 2))
        stdscr.refresh()

        key = stdscr.getch()
        if key in (curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT):
            if key == curses.KEY_UP and opcao_selecionada > 1:
                opcao_selecionada -= 2
            elif key == curses.KEY_DOWN and opcao_selecionada < 2:
                opcao_selecionada += 2
            elif key == curses.KEY_LEFT and opcao_selecionada % 2:
                opcao_selecionada -= 1
            elif key == curses.KEY_RIGHT and opcao_selecionada % 2 == 0:
                opcao_selecionada += 1
        elif key in [10, 13]:
            if opcao_selecionada == 3:
                break
            executar_comando(opcao_selecionada)
        elif key == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()
            for idx, (opcao, _) in enumerate(menu):
                row, col = divmod(idx, 2)
                x, y = col * (button_width + padding), row * (button_height + padding)
                if y <= my < y + button_height and x <= mx < x + button_width:
                    if idx == 3:
                        return
                    executar_comando(idx)

def tela_inicial(stdscr):
    stdscr.clear()
    stdscr.addstr(2, 2, "Escolha o modo de interface:")
    stdscr.addstr(4, 4, "1. Compacto (apenas texto)")
    stdscr.addstr(5, 4, "2. Completo (botões maiores e mouse)")
    stdscr.addstr(7, 2, "Pressione '1' ou '2' para selecionar.")
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key == ord('1'):
            return "compacto"
        elif key == ord('2'):
            return "completo"

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    modo = tela_inicial(stdscr)
    if modo == "compacto":
        mostrar_menu_compacto(stdscr)
    elif modo == "completo":
        mostrar_menu_completo(stdscr)

curses.wrapper(main)