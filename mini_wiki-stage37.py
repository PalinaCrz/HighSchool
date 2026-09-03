# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: MiniWiki
import unittest
from MiniWiki import App

class TestMiniWiki(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.app.init_db()

    def test_create_and_read_note(self):
        self.app.create_note("test", "Hello World", tags=["intro"])
        note = self.app.get_note("test")
        self.assertEqual(note["title"], "Hello World")
        self.assertEqual(note["tags"], ["intro"])

    def test_search_notes(self):
        self.app.create_note("n1", "Python is great", tags=["lang"])
        self.app.create_note("n2", "Python rocks", tags=["lang"])
        self.app.create_note("n3", "Java is okay", tags=["lang"])
        results = self.app.search_notes("Python")
        self.assertEqual(len(results), 2)

    def test_note_history(self):
        self.app.create_note("h", "First version")
        self.app.edit_note("h", "Second version", tags=["update"])
        history = self.app.get_note_history("h")
        self.assertEqual(len(history), 2)
        self.assertEqual(history[1]["title"], "Second version")

    def test_link_between_notes(self):
        self.app.create_note("src", "Source note")
        self.app.create_note("dst", "Destination note")
        self.app.add_link("src", "dst", "see here")
        links = self.app.get_links("src")
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0]["target"], "dst")

    def test_invalid_note_id(self):
        note = self.app.get_note("nonexistent")
        self.assertIsNone(note)

if __name__ == "__main__":
    unittest.main()
