#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        try:
            if not isinstance(value, str):
                raise TypeError("The value must be a string.")
            self.value = value
        except TypeError as e:
            print(str(e))

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        value_with_separators = self.value.replace(".", "@PERIOD@").replace("?", "@QUESTION@").replace("!", "@EXCLAMATION@")
        sentences = value_with_separators.split()
        sentences = [s.replace("@PERIOD@", ".").replace("@QUESTION@", "?").replace("@EXCLAMATION@", "!") for s in sentences]
        sentences = [s for s in sentences if s.endswith(".") or s.endswith("?") or s.endswith("!")]
        return len(sentences)