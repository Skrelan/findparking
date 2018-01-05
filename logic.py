def find_parking(user, store):
    result = []
    for key, parking in store.items():
        if not parking.taken:
            dist = user.location.distance(parking.location.lat,
                                          parking.location.lng)
            if dist <= user.radius:
                # use min heap and pop on it
                result.append({
                    "Name": key,
                    "Distance": str(dist)[:4],
                    "Location": {
                        "lat": parking.location.lat,
                        "lng": parking.location.lng
                    }
                })
                result = sorted(
                    result,
                    key=lambda k: k['Distance'])  # WE can improve on this
    return result
