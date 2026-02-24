def rank_candidates(candidates):
    return sorted(candidates, key=lambda x: x["similarity"], reverse=True)