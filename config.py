# Name of the blog
blog_name = 'On ideas worth stealing'

# (Optional) slogan
slogan = "A thief's perspective"

# Your name (used for copyright info)
author_name = 'Anh Hai Trinh'

# The hostname this site will primarially serve off (used for Atom feeds)
host = 'blog.onideas.ws'

# Selects the theme to use. Theme names correspond to directories under
# the 'themes' directory, containing templates and static content.
theme = 'default'

# A nested list of sidebar menus, for convenience. If this isn't versatile
# enough, you can edit themes/default/base.html instead.
sidebars = [
  ("Identity", [
    ('github', 'http://github.com/aht'),
    ('twitter', 'http://twitter.com/chickamade'),
  ]),
  ('Inspiration', [
    ('good/bad math', 'http://scienceblogs.com/goodmath/'),
    ('Nick Johnson', 'http://blog.notdot.net/'),
    ('Paul Graham', 'http://paulgraham.com/articles.html'),
    ('research!rsc', 'http://research.swtch.com/'),
    ('xkcd', 'http://www.xkcd.com/'),
  ]),
]

# Number of entries per page in indexes.
posts_per_page = 10

# The mime type to serve HTML files as.
html_mime_type = "text/html; charset=utf-8"

# To use disqus for comments, set this to the 'short name' of the disqus forum
# created for the purpose.
disqus_forum = 'onideas'

# Length (in words) of summaries, by default
summary_length = 100

# If you want to use Google Analytics, enter your 'web property id' here
analytics_id = 'UA-11948966-1'

# If you want to use PubSubHubbub, supply the hub URL to use here.
hubbub_hub_url = 'http://pubsubhubbub.appspot.com/'

# If you want to use Google Site verification, go to 
# https://www.google.com/webmasters/tools/ , add your site, choose the 'upload
# an html file' method, then set the NAME of the file below.
# Note that you do not need to download the file provided - just enter its name
# here.
google_site_verification = 'google4b7548b2151a637a.html'

# Default markup language for entry bodies (defaults to html).
default_markup = 'html'
