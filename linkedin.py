

from linkedin_api import Linkedin

from collections import Counter


# Authenticate using any Linkedin account credentials
api = Linkedin('patrick.orourke160893@gmail.com', 'Kurbosonic1993!')


# GET a profile
profile = api.get_profile('patrickorourke2')
#print(profile["locationName"])


#profile = api.get_profile('weifuru')
#print(profile["locationName"])

#print(profile["profile_id"])

# GET a profiles contact info
#contact_info = api.get_profile_contact_info('ACoAABYhHdgBit7zp7KWlsbypellTyd7HTUtmRM')



connections = api.get_profile_connections('ACoAABYhHdgBit7zp7KWlsbypellTyd7HTUtmRM')


#print(connections)


#print(type(connections))
countries = []

for i in connections:
    #print(i["urn_id"])
  #  profile = api.get_profile(i["urn_id"])
  #  if "locationName" in profile.keys():
   #     print(profile["locationName"])

    if "locationName" in (api.get_profile(i["urn_id"])).keys():
        if profile["locationName"] == "Japan":
            print(profile["locationName"])
            #countries.append(profile["locationName"])



print(Counter(countries))

    #countries.append(profile)
  #  countries.append(profile["locationName"])

#print(countries)
