import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
import config  # Import the config file

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=config.CLIENT_ID,
    client_secret=config.CLIENT_SECRET,
    redirect_uri=config.REDIRECT_URI,
    scope='playlist-read-private playlist-modify-private playlist-modify-public'
))

def copy_discover_weekly():
    # Get the Discover Weekly playlist details
    dw_playlist = sp.playlist(config.DISCOVER_WEEKLY_ID)
    tracks = dw_playlist['tracks']['items']

    # Create a new playlist with the current date as the title
    user_id = sp.me()['id']
    current_date = datetime.now().strftime('%Y-%m-%d')
    new_playlist_name = f'Discover Weekly - {current_date}'
    new_playlist = sp.user_playlist_create(user_id, new_playlist_name, public=False)
    
    # Extract track URIs and add to the new playlist
    track_uris = [item['track']['uri'] for item in tracks]
    sp.playlist_add_items(new_playlist['id'], track_uris)

    print(f'Copied Discover Weekly to a new playlist: {new_playlist_name}')

# Run the function
if __name__ == '__main__':
    copy_discover_weekly()
