from translate import Translator

translator = Translator(to_lang="pl")
try:
    with open('text.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
    with open('text_pl.txt', mode='w') as result:
        result.write(translation)

except FileNotFoundError:
    print('Cannot find file')
