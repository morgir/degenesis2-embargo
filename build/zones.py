# Wspólne mapowanie zasięgów broni na strefy (0.7.0)
ZONE = {"1": "Zwarcie", "2": "Zwarcie", "3": "Zwarcie",
        "5/20": "Blisko", "10/20": "Blisko", "10/40": "Blisko", "10/30": "Blisko",
        "15/60": "Daleko", "20/80": "Daleko", "30/80": "Daleko", "30/100": "Daleko+", "30/120": "Daleko+"}
def zone(r):
    return ZONE.get(str(r), r)
