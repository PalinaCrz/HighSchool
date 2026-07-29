# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: MiniWiki
def reset_demo_data():
    """Сбрасывает все данные в дефолтные демо-значения."""
    global notes, links, tags, revisions, history, current_user_id, current_page
    notes = {i: DEMO_NOTE_CONTENT[i] for i in range(len(DEMO_NOTE_CONTENT))}
    links = {}
    tags = {}
    revisions = []
    history = []
    revision_counter = 0
    if DEFAUL_USER_ID is not None:
        current_user_id = DEFAUL_USER_ID
    else:
        current_user_id = generate_uuid()
    current_page = ""

def clear_state():
    """Полностью очищает все данные и сбрасывает состояние."""
    global notes, links, tags, revisions, history, current_user_id, current_page
    notes = {}
    links = {}
    tags = {}
    revisions = []
    history = []
    revision_counter = 0
    current_user_id = generate_uuid() if DEFAUL_USER_ID is not None else generate_uuid()
    current_page = ""

def demo():
    """Запускает демо-сценарий: создает несколько заметок и показывает результат."""
    reset_demo_data()
    print("Демо-данные сброшены. Добро пожаловать в MiniWiki!")
