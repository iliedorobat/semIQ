import numpy
from ro.webdata.oniq.model.sentence.Noun import Noun


def get_noun_list(chunk, *dependencies: []):
    """
    Get the list of nouns in a sentence

    :param dependencies: The list of dependencies used for filtering
    :param chunk: The sentence
    :return: The list of nouns
    """

    nouns = []

    for token in chunk:
        if token.tag_[0:2] == "NN" and (
                len(dependencies) == 0 or token.dep_ in numpy.asarray(dependencies)
        ):
            nouns.append(
                Noun(token.dep_, token.text == chunk.root.text, token)
            )

    return nouns
