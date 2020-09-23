# pip install osmapi

# Read from OpenStreetMap
'''
    import osmapi
    api = osmapi.OsmApi()
    print(api.NodeGet(123))
    # {u'changeset': 532907, u'uid': 14298,
    # u'timestamp': u'2007-09-29T09:19:17Z',
    # u'lon': 10.790009299999999, u'visible': True,
    # u'version': 1, u'user': u'Mede',
    # u'lat': 59.9503044, u'tag': {}, u'id': 123}
'''

# Constructor
'''
import osmapi
api = osmapi.OsmApi(api="https://api06.dev.openstreetmap.org", username = "you", password = "***")
api = osmapi.OsmApi(username = "you", passwordfile = "/etc/mypasswords")
api = osmapi.OsmApi(passwordfile = "/etc/mypasswords") # if only the passwordfile is specified, the credentials on the first line of the file will be used
'''

# Write to OpenStreetMap
'''
import osmapi
api = osmapi.OsmApi(api="https://api06.dev.openstreetmap.org", username = u"metaodi", password = u"*******")
api.ChangesetCreate({u"comment": u"My first test"})
print(api.NodeCreate({u"lon":1, u"lat":1, u"tag": {}}))
# {u'changeset': 532907, u'lon': 1, u'version': 1, u'lat': 1, u'tag': {}, u'id': 164684}
api.ChangesetClose()
'''