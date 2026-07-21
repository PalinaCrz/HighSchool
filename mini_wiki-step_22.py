# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: MiniWiki
def check_expired_reminders():
    now = time.time()
    expired = [r for r in reminders if r.get("time") and now > r["time"]]
    if not expired:
        return None
    return {
        "expired": expired,
        "message": f"Время истекло для {len(expired)} напоминания(я):\n" + "\n".join(f"- [{r['type']}] {r.get('content', '')}" for r in expired)
    }

def add_expiration_to_reminder(note):
    if not note.get("reminder"):
        return note
    reminder = note["reminder"]
    if not reminder.get("time") and not reminder.get("expire_in_hours"):
        expire_in_hours = ask_for_int("Сколько часов до истечения напоминания? (0 для безграничного)", 72)
        reminder["expire_in_hours"] = int(expire_in_hours) if expire_in_hours else None
    return note

def save_reminders_with_expiration():
    reminders_file = REMINDERS_FILE
    expired = check_expired_reminders()
    result = {
        "reminders": [r for r in reminders if not (r.get("time") and time.time() > r["time"])],
    }
    if expired:
        print(f"\n⚠️  Просрочено напоминаний:")
        print(expired["message"])
        result["expired_reminders"] = expired["expired"]
    save_json(reminders_file, result)
    return result
