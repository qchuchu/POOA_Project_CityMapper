def url_here_weather_api():
    base = 'https://weather.api.here.com/weather/1.0/report.xml'
    app_id = "?app_id=" + app.config['APP_ID']
    app_code = "&app_code=" + app.config['APP_CODE']
    product = "&product=observation"
    name = "&name=Paris"
    return base + app_id + app_code + product + name