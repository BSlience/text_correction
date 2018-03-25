# encoding:utf-8


class NonWordCorrection(object):

    @staticmethod
    def detection(word):
        return word.is_realword()

    @staticmethod
    def correction(word):
        pass


class RealWordCorrection(object):

    @staticmethod
    def detection():
        pass

    @staticmethod
    def correction(self):
        pass


class SpellCorrection(object):
    """拼写纠错"""

    @staticmethod
    def correction(essay):
        corrections = {}
        for word in essay.iter_word():
            if NonWordCorrection.detection(word):
                NonWordCorrection.correction(word)


if __name__ == '__main__':
    SpellCorrection.correction("hallo, my name is zhang. I'm 25 years old")




