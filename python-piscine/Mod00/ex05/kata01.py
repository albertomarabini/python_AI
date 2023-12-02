# Dictionary
kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

def display_creators(languages):
    for language, creator in languages.items():
        print(f"{language} was created by {creator}")

# Calling the function
display_creators(kata)