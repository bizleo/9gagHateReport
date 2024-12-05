def parse_count(count_str):
    """
    Converts a count string like '5.8K' to an integer.
    """
    count_str = count_str.strip().upper()
    if 'K' in count_str:
        return int(float(count_str.replace('K', '')) * 1000)
    elif 'M' in count_str:
        return int(float(count_str.replace('M', '')) * 1_000_000)
    else:
        return int(count_str)