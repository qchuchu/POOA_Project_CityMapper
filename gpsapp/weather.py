import requests

class Weather:

"""This class returns the current weather conditions in Paris"""

    def __init__(self):
        pass


    def get_weather(self):
        base = 'https://weather.cit.api.here.com/weather/1.0/report.json?product=observation&'
        city = 'name=Paris'
        app_id = "&app_id=" + 'djGZJjsUab93vV3VqBKA'
        # app_id = "&app_id=" + app.config['APP_ID']
        app_code = "&app_code=" + 'u3bReKn8wIAuZl74j1iyGA'
        # app_code = "&app_code=" + app.config['APP_CODE']
        url = base + city + app_id + app_code
        print(url)
        resp = requests.get(url)
        data = resp.json()
        sky_desc = data['observations']['location'][0]['observation'][0]['iconName']
        picture_link = data['observations']['location'][0]['observation'][0]['iconLink']
        temperature = data['observations']['location'][0]['observation'][0]['temperature']
        windspeed = data['observations']['location'][0]['observation'][0]['windSpeed']
#As the sky descriptions are very precise and we only need basic ones, we group them in 9 categories
        if sky_desc in ['night_clear','night_clearing_skies','night_mostly_clear','night_passing_clouds','night_scattered_clouds','night_partly_cloudy','cw_no_report_icon']:
            sky_desc = 'clear'
        elif sky_desc in ['increasing_cloudiness','breaks_of_sun_late','afternoon_clouds','morning_clouds','partly_sunny','high_level_clouds','decreasing_cloudiness','clearing_skies','high_clouds','ice_fog','more_clouds_than_sun','broken_clouds','hazy_sunshine','haze','smoke','low_level_haze','fog','dense_fog','night_haze','night_smoke','night_low_level_haze','mostly_cloudy','cloudy','overcast','low_clouds','night_decreasing_cloudiness','night_high_level_clouds','night_high_clouds','increasing_cloudiness','night_afternoon_clouds','night_morning_clouds','night_broken_clouds','night_mostly_cloudy']:
            sky_desc = 'cloudy'
        elif sky_desc in ['hail','icy_mix','light_freezing_rain','freezing_rain']:
            sky_desc ='hail'
        elif sky_desc in ['rain_early','heavy_rain_early','scattered_showers','a_few_showers','light_showers','passing_showers','rain_showers','showers','sleet','light_mixture_of_precip','mixture_of_precip','heavy_mixture_of_precip','snow_changing_to_rain','an_icy_mix_changing_to_rain','snow_rain_mix','scattered_flurries','flurries_early','flurries_late','night_scattered_showers','night_a_few_showers','night_light_showers','night_passing_showers','night_rain_showers','night_sprinkles','night_showers','heavy_rain','lots_of_rain','tons_of_rain','heavy_rain_early','heavy_rain_late','flash_floods','flood','drizzle','sprinkles','light_rain','sprinkles_early','light_rain_early','sprinkles_late','light_rain_late','rain','numerous_showers','showery','showers_early','rain_early','showers_late','rain_late']:
            sky_desc = 'rainy'
        elif sky_desc in ['snow_changing_to_an_icy_mix','an_icy_mix_changing_to_snow','rain_changing_to_snow','rain_changing_to_an_icy_mix','light_icy_mix_early','icy_mix_early','light_icy_mix_late','icy_mix_late','snow_flurries','light_snow_showers','snow_showers','light_snow','snow_showers_early','light_snow_early','snow_showers_late','light_snow_late','snow','moderate_snow','snow_early','snow_late','heavy_snow','heavy_snow_early','heavy_snow_late','snowstorm','blizzard']:
            sky_desc = 'snowy'
        elif sky_desc == 'hurricane':
            sky_desc = 'hurricane'
        elif sky_desc in ['sunny','clear','mostly_sunny','mostly_clear','passing_clounds','more_sun_than_clouds','scattered_clouds','partly_cloudy','a_mixture_of_sun_and_clouds','early_fog_followed_by_sunny_skies','early_fog','light_fog']:
            sky_desc = 'sunny'
        else :
            sky_desc = 'tornado'
        print ([sky_desc, picture_link, temperature, windspeed])

#meteo = Weather()
#meteo.get_weather()








