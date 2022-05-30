from typing import Tuple, Dict

# from . import ag_news, dbpedia, imdb, ohsu_med, r8, r52, sogou_news, trec6, twenty_news, yahoo_answers, yelp_polarity

from . import ag_news, dbpedia, sogou_news

def get_label_map(dataset: str) -> Tuple[Dict[str, int], Dict[int, str]]:
    if dataset == 'AG_NEWS':
        classes = ag_news.classes
    elif dataset == 'DBpedia':
        classes = dbpedia.classes
    # elif dataset == 'IMDB':
    #     classes = imdb.classes
    # elif dataset == 'OHSUMED':
    #     classes = ohsu_med.classes
    # elif dataset == 'R8':
    #     classes = r8.classes
    # elif dataset == 'R52':
    #     classes = r52.classes
    elif dataset == 'SogouNews':
        classes = sogou_news.classes
    # if dataset == 'TREC6':
    #     classes = trec6.classes
    # elif dataset == 'TwentyNews':
    #     classes = twenty_news.classes
    # elif dataset == 'YahooAnswers':
    #     classes = yahoo_answers.classes
    # elif dataset == 'YelpReviewPolarity':
    #     classes = yelp_polarity.classes
    else:
        raise Exception("Dataset not supported: ", dataset)

    label_map = {k: v for v, k in enumerate(classes)}
    rev_label_map = {v: k for k, v in label_map.items()}

    return label_map, rev_label_map
