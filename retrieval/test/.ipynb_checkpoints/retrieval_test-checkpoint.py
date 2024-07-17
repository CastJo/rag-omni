# -*- coding: utf-8 -*-

import requests


def retrieval_test():
    url = 'http://{0}:{1}/api/rag/retrieval'.format("127.0.0.1", "5001")
    params = {'question': "国务院对于地方政府性债务管理的意见", 'top_k': 3}
    # params = {'question': "国务院对于地方政府专项债券发行有何意见", 'top_k': 3}
    r = requests.get(url, params=params)
    print(r.text)


if __name__ == '__main__':
    retrieval_test()


