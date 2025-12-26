from ts4lib.utils.unveil import Unveil


class TestUnveil:
    def do(self, text):
        obfuscated_text = Unveil.illuminate(text)
        print(f"r'{obfuscated_text}'  # {Unveil.self(obfuscated_text)}")


if __name__ == "__main__":
    TestUnveil().do('text')
