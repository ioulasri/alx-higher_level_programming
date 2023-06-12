#!/usr/bin/python3
if __name__ == "__main__":
    """printing items in list"""
    def multiple_returns(sentence):
        if sentence == None:
            return (0, None)
        return (len(sentence), sentence[0])
