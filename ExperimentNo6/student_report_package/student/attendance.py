def check_eligibility(attended, total):
    perc = (attended / total) * 100
    return perc >= 75, perc
