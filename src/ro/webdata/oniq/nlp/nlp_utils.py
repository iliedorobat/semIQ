from typing import Union
from spacy.tokens import Doc, Span
import warnings


def get_cardinals(chunk):
    """
    Get the list of cardinals in a chunk

    :param chunk: The target chunk
    :return: The list of cardinals
    """
    return list([token for token in chunk if token.tag_ == "CD"])


def get_preposition(sentence: Span, chunk: Span):
    first_index = chunk[0].i
    prev_word = sentence[first_index - 1] if first_index > 0 else None

    if prev_word is not None and prev_word.dep_ == "prep":
        return prev_word

    return None


def get_prev_chunk(chunks: [Span], chunk: Span):
    warnings.warn("The method is not used anymore", DeprecationWarning)

    chunk_index = chunks.index(chunk)
    if chunk_index > 0:
        return chunks[chunk_index - 1]
    return None


def get_wh_adverbs(document: Union[Doc, Span]):
    """
    Get the list of WH-adverbs (tag = 'WRB'):\n
    - when, where, why\n
    - whence, whereby, wherein, whereupon\n
    - how\n

    Resources:\n
    - https://grammar.collinsdictionary.com/easy-learning/wh-words\n
    - https://www.ling.upenn.edu/hist-corpora/annotation/pos-wh.htm

    :param document: The parsed document
    :return: The list of WH-adverbs
    """
    return list([token for token in document if token.tag_ == 'WRB'])


def get_wh_determiner(document: Union[Doc, Span]):
    """
    Get the list of WH-determiners (tag = 'WDT'):\n
    - what, which, whose\n

    Resources:\n
    - https://grammar.collinsdictionary.com/easy-learning/wh-words\n
    - https://www.ling.upenn.edu/hist-corpora/annotation/pos-wh.htm

    :param document: The parsed document
    :return: The list of WH-determiners
    """
    return list([token for token in document if token.tag_ == 'WDT'])


def get_wh_pronouns(document: Union[Doc, Span]):
    """
    Get the list of WH-pronouns (tag in ['WP', 'WP$'])\n
    - who, whose, which, what\n

    Resources:\n
    - https://grammar.collinsdictionary.com/easy-learning/wh-words\n
    - https://www.ling.upenn.edu/hist-corpora/annotation/pos-wh.htm

    :param document: The parsed document
    :return: The list of WH-pronouns
    """
    return list([token for token in document if token.tag_ in ['WP', 'WP$']])


def get_wh_words(document: Union[Doc, Span]):
    """
    Get the list of WH-words\n
    - when, where, why\n
    - whence, whereby, wherein, whereupon\n
    - how\n
    - what, which, whose\n
    - who, whose, which, what\n

    Resources:\n
    - https://grammar.collinsdictionary.com/easy-learning/wh-words\n
    - https://www.ling.upenn.edu/hist-corpora/annotation/pos-wh.htm

    :param document: The parsed document
    :return: The list of WH-words
    """
    return list([token for token in document if token.tag_ in ['WRB', 'WDT', 'WP', 'WP$']])


def retokenize(document: Union[Doc, Span], sentence: Span):
    """
    Integrate the named entities into the document and retokenize it

    :param document: The parsed document
    :param sentence: The target sentence
    :return: Nothing
    """

    for named_entity in sentence.ents:
        with document.retokenize() as retokenizer:
            retokenizer.merge(named_entity)
