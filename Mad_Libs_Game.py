def get_input(prompt):
    return input(prompt)

def create_story(template):
    placeholders = {
        "<noun>": "a noun",
        "<verb>": "a verb",
        "<adjective>": "an adjective",
        "<adverb>": "an adverb",
        "<plural_noun>": "a plural noun",
        "<place>": "a place",
        "<person>": "a person"
    }
    
    for placeholder, description in placeholders.items():
        while placeholder in template:
            word = get_input(f"Enter {description}: ")
            template = template.replace(placeholder, word, 1)
    return template

def main():
    template = (
        "Once upon a time in <place>, there was a <adjective> <noun> named <person>. "
        "Every day, <person> would <verb> <adverb> with the <plural_noun>. "
        "One day, they decided to <verb> to the <place> and had a <adjective> adventure."
    )
    
    print("Welcome to the Mad Libs Game!")
    print("Fill in the blanks to create a fun story.")
    print()
    
    story = create_story(template)
    
    print()
    print("Here is your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    main()
