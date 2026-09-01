# === Stage 43: Добавь пагинацию длинных списков ===
# Project: NoteWeaver
class PaginatedList:
    def __init__(self, items, page_size=20):
        self._items = items
        self._page_size = page_size
        self._pages = [items[i:i + page_size] for i in range(0, len(items), page_size)]

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._pages)

    def __getitem__(self, idx):
        return self._pages[idx]

    @property
    def total(self):
        return len(self._items)

    @property
    def pages(self):
        return self._pages

    @property
    def page_count(self):
        return len(self._pages)

    def get_page(self, page_num):
        if 0 <= page_num < len(self._pages):
            return self._pages[page_num]
        return []
