import shutil
from rich.console import Console
from rich.markdown import Markdown

from config.config import theme_char
from src.ui.ui_helpers import parse_user_input

con = Console()
state = ""


def run():
    while True:
        try:
            size = shutil.get_terminal_size()
            columns = size.columns
            lines = size.lines

            global state
            state = f"""
{"=" * columns}
[bold green]OPTIONS[/]  [dim]Enter 'exit' or 'x' or 'c' to exit[/]\n\n
{theme_char}    setup_sim
{theme_char}    run_sim
{theme_char}    predict
{theme_char}    optimization
{"=" * columns}
            """
            con.print(state)
            user_input = input("> ")

            # Handle explicit exit commands here (or in parse_user_input)
            if user_input.strip().lower() in ("exit", "x", "c", "q", "quit"):
                con.print("[yellow]Goodbye![/]")
                break

            parse_user_input(user_input)

        except KeyboardInterrupt:
            # Ctrl+C pressed 
            con.print("\n[yellow]Interrupted. Exiting...[/]")
            break

        except EOFError:
            # Ctrl+D pressed 
            con.print("\n[yellow]EOF received. Exiting...[/]")
            break

        except Exception as e:
            # Catch real runtime errors but keep the loop alive
            con.print(f"[red]Error:[/] {e}")


if __name__ == "__main__":
    run()