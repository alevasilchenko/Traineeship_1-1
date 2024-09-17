def calculate_and_display_average_price(data):
    if len(data) and 'Close' in data:
        result = round(data['Close'].mean(), 2)
        return result
