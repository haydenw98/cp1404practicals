from prac_06.programming_language import ProgrammingLanguage


def main():
    """Create ProgrammingLanguage objects, store in a list and print dynamic languages"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [python, ruby, visual_basic]
    print(python)
    print(ruby)
    print(visual_basic)

    print_dynamic(languages)
    #print(languages)
    #print(python)


def print_dynamic(languages):
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()