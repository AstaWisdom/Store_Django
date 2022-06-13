import uuid


def generate_referral_link():
    referral_link = str(uuid.uuid4()).replace("-", "")
    return referral_link[:12]


