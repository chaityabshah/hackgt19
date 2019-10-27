import requests
import json
def get_auth():
    headers = {
        'Authorization': 'Basic NjllNWViZTg1N2Y1NGNlZDkwOGZhYjcxYzdkMTFkMzM6YWJkNzExYjM0MjViNDMzZTg3NWFlNmRkOTA5Y2ZlNTE=',
    }
    data = {
        'grant_type': 'client_credentials'
    }

    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    return json.loads(response.text)

def get_music_features(auth_atts, song_id):
    headers = {
        'Authorization': auth_atts['token_type'] + ' ' + auth_atts['access_token'],
    }
    #response = requests.get('https://api.spotify.com/v1/tracks/21kOVEG3bDCVphKhXL8XmQ', headers=headers)
    response = requests.get('https://api.spotify.com/v1/audio-features/' + song_id, headers=headers)
    return json.loads(response.text)

def get_music_features_bulk(auth_atts, song_ids):
    headers = {
        'Authorization': auth_atts['token_type'] + ' ' + auth_atts['access_token'],
    }
    params = {
        'ids': song_ids,
    }
    response = requests.get('https://api.spotify.com/v1/audio-features/', headers=headers, params=params)
    return json.loads(response.text)

def get_album_from_id_bulk(auth_atts, song_ids):
    headers = {
        'Authorization': auth_atts['token_type'] + ' ' + auth_atts['access_token'],
    }
    params = {
        'ids': song_ids,
    }
    response = requests.get('https://api.spotify.com/v1/tracks/', headers=headers, params=params)
    response = json.loads(response.text)
    return [song['album']['uri'].split(':')[2] for song in response['tracks']]

def get_artist_from_id_bulk(auth_atts, song_ids):
    headers = {
        'Authorization': auth_atts['token_type'] + ' ' + auth_atts['access_token'],
    }
    params = {
        'ids': song_ids,
    }
    response = requests.get('https://api.spotify.com/v1/tracks/', headers=headers, params=params)
    response = json.loads(response.text)
    return [song['album']['artists'][0]['uri'].split(':')[2] for song in response['tracks']]

def get_song_genres(auth_atts, song_ids):
    album_ids = ','.join(get_artist_from_id_bulk(auth_atts, song_ids))
    headers = {
        'Authorization': auth_atts['token_type'] + ' ' + auth_atts['access_token'],
    }
    params = {
        'ids': album_ids,
    }
    response = requests.get('https://api.spotify.com/v1/artists/', headers=headers, params=params)
    response = json.loads(response.text)
    return ([artist['genres'][0] for artist in response['artists'] if artist['genres']])

if __name__ == '__main__':
    a = get_auth()
    # print (get_music_features(a, '21kOVEG3bDCVphKhXL8XmQ'))
    #print (get_music_features_bulk(a, '4JpKVNYnVcJ8tuMKjAj50A,2NRANZE9UCmPAS5XVbXL40,24JygzOLM0EmRQeGtFcIcG'))
    print (get_music_features_bulk(a, '5ZnOG96081GKWdYzICCzIu,2xizRhme7pYeITbH1NLLGt,2YpeDb67231RjR0MgVLzsG'))
    #print (get_artist_from_id_bulk(a, '5ZnOG96081GKWdYzICCzIu,2xizRhme7pYeITbH1NLLGt,2YpeDb67231RjR0MgVLzsG'))
    #divinity, tchaik, otr
    #print (get_song_genres(a, '5ZnOG96081GKWdYzICCzIu,2xizRhme7pYeITbH1NLLGt,2YpeDb67231RjR0MgVLzsG'))
