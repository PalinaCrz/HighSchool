# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: MiniWiki
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
import sys

console = Console()

def show_menu():
    table = Table(title="MiniWiki CLI", box=None)
    table.add_column("ID", justify="center")
    table.add_column("Действие", style="cyan")
    actions = [
        ("1", "Создать/Просмотреть заметку"),
        ("2", "Поиск по тексту или тегам"),
        ("3", "История правок выбранной заметки"),
        ("4", "Удалить заметку"),
        ("5", "Выйти из программы")
    ]
    for idx, (id_, action) in enumerate(actions):
        table.add_row(id_, action)
    
    console.print(table)
    choice = Prompt.ask("Выберите действие", choices=[str(i) for i in range(1, len(actions)+1)], default="1")
    return int(choice), actions[int(choice)-1][0]

def handle_action(action_id):
    if action_id == "5":
        console.print("[bold green]До свидания![/bold green]")
        sys.exit()
    
    note_title = Prompt.ask("Введите название заметки (или оставьте пустым для поиска)", default="")
    
    if not note_title:
        search_query = Prompt.ask("Ключевые слова или теги для поиска", default="")
        results = wiki.search(search_query)  # Предполагается, что есть функция search в глобальном scope
        if results:
            for r in results[:5]:
                console.print(Panel(r['title'] + f" ({r.get('tags', [])})", title=f"[bold]{r['id']}[/bold]"))
        else:
            console.print("[yellow]Ничего не найдено.[/yellow]")
    else:
        note = wiki.get_note(note_title)  # Предполагается, что есть функция get_note в глобальном scope
        if not note:
            console.print(f"[red]Заметка '{note_title}' не найдена.[/red]")
            return
        
        table = Table(title=f"Заметка: {note['title']}")
        table.add_column("Ключ", justify="left")
        table.add_column("Значение", style="white")
        
        for key, value in note.items():
            if isinstance(value, list):
                value_str = ", ".join(str(v) for v in value)
            else:
                value_str = str(value)
            table.add_row(key, value_str)
        
        console.print(table)
        
        # История правок (упрощенно)
        if 'history' in note and note['history']:
            hist_table = Table(title="История изменений")
            hist_table.add_column("Версия", justify="center")
            hist_table.add_column("Автор", style="yellow")
            hist_table.add_column("Комментарий", style="green")
            
            for i, h in enumerate(note['history'][-5:], 1): # Показать последние 5 правок
                hist_table.add_row(str(i), str(h.get('author', 'unknown')), str(h.get('comment', '')))
            console.print(hist_table)

        edit_comment = Prompt.ask("Комментарий к изменению (или Enter для пропуска)", default="")
        if edit_comment:
            wiki.edit_note(note_title, note['content'], comment=edit_comment) # Предполагается функция edit_note
