def catalog_coverage(recommendations: list, n_items: int) -> float:
    """
    Returns the fraction of catalog items that were recommended.
    """
    # Write code here
    if n_items == 0:
        return 0.0
    distinct = set()
    [distinct.add(x) for recommendation in recommendations for x in recommendation]
        
    return len(distinct)/n_items