

season_dummies = {
    'winter': [0, 0, 1],
    'spring': [1, 0, 0],
    'summer': [0, 1, 0],
    'fall': [0, 0, 0]
}

weather_dummies = {
    'clear': [0, 0, 0],
    'mist': [1, 0, 0],
    'rainy': [0, 1, 0],
    'snowy': [0, 0, 1]
}


weekdays_dummies = {
    'saturday': [0, 1, 0, 0, 0, 0],
    'sunday': [0, 0, 1, 0, 0, 0],
    'monday': [1, 0, 0, 0, 0, 0],
    'tuesday': [0, 0, 0, 0, 1, 0],
    'wednesday': [0, 0, 0, 0, 0, 1],
    'thursday': [0, 0, 0, 1, 0, 0],
    'friday': [0, 0, 0, 0, 0, 0]
}


pod_dummies = {
    'evening': [1, 0, 0],
    'morning': [0, 1, 0],
    'night': [0, 0, 1],
    'afternoon': [0, 0, 0],
}
