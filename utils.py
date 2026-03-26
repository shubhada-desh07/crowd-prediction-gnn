def get_risk(count, capacity):
    ratio = count / capacity

    if ratio < 0.6:
        return "Safe"
    elif ratio < 0.85:
        return "Moderate"
    else:
        return "High"


def check_alert(count, capacity):
    if count > capacity:
        return "🚨 OVERCROWD ALERT"
    elif count > 0.9 * capacity:
        return "⚠️ WARNING"
    return "OK"


def count_people_per_zone(detections):
    from zones import get_node

    zone_counts = {}

    for (x, y) in detections:
        node = get_node(x, y)

        if node not in zone_counts:
            zone_counts[node] = 0

        zone_counts[node] += 1

    return zone_counts