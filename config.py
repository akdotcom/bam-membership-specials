CONFIG = {
  # foursquare server to use. You probably don't need to change this.
  'foursquare_server':'https://foursquare.com',
  # The server name for local_dev mode. Make sure the port matches what you use.
  'local_server': 'http://localhost:8080',
  # Server name for your deployed AppEngine instance
  'prod_server': ''
  # OAuth client ID. Must match what you set at https://foursquare.com/oauth.
  'client_id': '',
  # OAuth client secret. Must match what you set at https://foursquare.com/oauth.
  'client_secret': '',
  # Foursquare push API secret. Must match what you set at https://foursquare.com/oauth.
  'push_secret': '',
  # OAuth callback/redirect URI. Must match what you set at https://foursquare.com/oauth.
  'redirect_uri': '%s/oauth', # (server)
  # Format string to serve URL content out of. Not necessarily required.
  'content_uri': '%s/content?content_id=%s', # (server, content_id)
  # The foursquare API version string to pass. See: https://developer.foursquare.com/overview/versioning
  'api_version': '20120201',
  # A name for the hompage and titles.
  'site_name': '',
  # A description for the home page
  'site_description': '',
  # If true, we use local_server, and log actions instead of POSTing to foursquare
  # Be sure to set this to false when you actually want to deploy.
  'local_dev': True,
  # AppEngine debug mode
  'debug': True,
  # This can either be a path (on this server), or an external URI
  'post_auth_confirmation_uri': '/',
  # Application Level Configuration
  # Feel free to add new config parameters here...
}

# Replace 'None' with the class object of your plugin. It must inherit from the
# provided Plugin class.
# NOTE: You'll need to import your plug-in class doen here, below the definition of CONFIG, if you
# want to use CONFIG inside your plugin class.
PLUGIN_CLASS = None
