from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def match_experts(business_description, expert_profiles):
    """
    Match business needs with expert profiles using embeddings.
    expert_profiles: List of dicts with 'id', 'bio', 'skills'
    """
    business_embedding = model.encode(business_description)
    expert_embeddings = [
        model.encode(f"{p['bio']} {' '.join(p['skills'])}")
        for p in expert_profiles
    ]
    similarities = util.cos_sim(business_embedding, expert_embeddings)[0]
    return [
        {'profile': profile, 'score': float(score)}
        for profile, score in sorted(
            zip(expert_profiles, similarities), key=lambda x: x[1], reverse=True
        )
    ]