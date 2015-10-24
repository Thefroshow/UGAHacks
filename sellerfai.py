#Richard Saney
#Josh Harper
#Alex Hunt

#[endpoint] => http://research.api.sellerlabs.com/
#[key] => 1445656217|slapi|c546db3b045236ccad072dea3d86317b

import urllib2

endpoint = "http://research.api.sellerlabs.com/"
key = 1445656217|slapi|c546db3b045236ccad072dea3d86317b
response = urllib2.urlopen('http://python.org/')
html = response.read()
