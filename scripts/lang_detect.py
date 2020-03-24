def detect_language(word: str) -> str:
    if u'\u0980' <= word <= u'\u09FF':
        return 'asm'
    return 'en'
