#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 13 Warm-up tasks 1-3"""

import json

GRADES = {
    'A': float(1.00),
    'B': float(0.90),
    'C': float(0.80),
    'D': float(0.70),
    'F': float(0.60),
}


def get_score_summary(filename):
    """This function will do some calculation and return dictionary.
    Args:
        filename(file): this a csv file.
    Returns: a dictionary
    Examples:
        >>> get_score_summary('inspection_results.csv')
        {'BRONX': (156, 0.9762820512820514),
        'BROOKLYN': (417, 0.9745803357314141),
        'STATEN ISLAND': (46, 0.9804347826086955),
        'MANHATTAN': (748, 0.9771390374331531),
        'QUEENS': (414, 0.9719806763285017)}
    """
    fhandler = open(filename, 'r')

    camis = []
    boro_grades = []

    line = fhandler.readline()
    while line != '':
        line = fhandler.readline()
        splited = line.split(',')
        if splited[0] != '':
            if splited[10] != '' and splited[10] != 'P':
                camis.append(splited[0])
                boro_grades.append((splited[1], splited[10]))

    fhandler.close()

    camis_dict = dict(zip(camis, boro_grades))

    m_score, m_count = 0, 0
    q_score, q_count = 0, 0
    bk_score, bk_count = 0, 0
    bx_score, bx_count = 0, 0
    si_score, si_count = 0, 0

    for value in camis_dict.itervalues():
        if 'MANHATTAN' in value:
            m_x = GRADES[value[1]]
            m_count += 1
            m_score += m_x
        elif 'QUEENS' in value:
            q_x = GRADES[value[1]]
            q_count += 1
            q_score += q_x
        elif 'BROOKLYN' in value:
            bk_x = GRADES[value[1]]
            bk_count += 1
            bk_score += bk_x
        elif 'BRONX' in value:
            bx_x = GRADES[value[1]]
            bx_count += 1
            bx_score += bx_x
        elif 'STATEN ISLAND' in value:
            si_x = GRADES[value[1]]
            si_count += 1
            si_score += si_x

    score_summary = {
        'MANHATTAN': (m_count, m_score / m_count),
        'QUEENS': (q_count, q_score / q_count),
        'BROOKLYN': (bk_count, bk_score / bk_count),
        'BRONX': (bx_count, bx_score / bx_count),
        'STATEN ISLAND': (si_count, si_score / si_count),
    }

    return score_summary


def get_market_density(filename):
    """This function will load some data
    Args:
        filename(file): a file
    Return: a dictionary
    Examples:
        >>> get_market_density('green_markets.json')
        {u'Staten Island': 2,
        u'Brooklyn': 48, u'Bronx': 32,
        u'Manhattan': 39,
        u'Queens': 16}
    """
    fhandler = open(filename, 'r')
    j_data = json.load(fhandler)
    res_data = j_data['data']
    fhandler.close()

    bronx, brooklyn, manhattan, queens, staten_island = 0, 0, 0, 0, 0
    for item in res_data:
        if 'Bronx' in item:
            bronx += 1
        elif 'Brooklyn' in item:
            brooklyn += 1
        elif 'Manhattan' in item:
            manhattan += 1
        elif 'Queens' in item:
            queens += 1
        elif 'Staten Island' in item:
            staten_island += 1

    num_market = {
        'STATEN ISLAND': staten_island,
        'BROOKLYN': brooklyn,
        'BRONX': bronx,
        'MANHATTAN': manhattan,
        'QUEENS': queens
    }

    return num_market


def correlate_data(res_filename, j_filename, out_filename):
    """Combining data together and writing into new file.
        Args: File1, File2, File3
        Returns: file3 with data
    """
    score_dict = get_score_summary(res_filename)
    market_dict = get_market_density(j_filename)

    final_dict = {}
    for key, value in score_dict.iteritems():
        final_dict[key] = (value[1], float(market_dict[key]) / float(value[0]))

    filepath = out_filename
    fhandler = open(filepath, 'w')
    json.dump(final_dict, fhandler)
    fhandler.close()
