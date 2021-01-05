import json
import facebook


def main():
    token = {"EAACrNo0LyvwBAELaZBFXs7wAasRndbJB2hajnHWrSHzoZChf6ZBcu64ua9tMh7YZA2V7fUZBNYOAKCibpYiMK4U4bddbw2qEi4I63DklSAcCfdsj4l8yzRA0FNEU0Pi4toI6aZCIkcfHDNzTEVHBKpgigFq691T6II4hZAZAlk2v4NQauDn7PyL8ZAXrRC1AW7CtcUUMT847MRDg9BeRZBUAb7EwisbRr2qkAEVPvj1fEk5gZDZD"}
    graph = facebook.GraphAPI(token)

    fields = ['name, email, id']

    profile =  graph.get_object('me', fields=fields)

    print(json.dumps(profile, indent=4))


if __name__ == '__main__':
    main()
    

def page():
    token = {'EAACrNo0LyvwBAELaZBFXs7wAasRndbJB2hajnHWrSHzoZChf6ZBcu64ua9tMh7YZA2V7fUZBNYOAKCibpYiMK4U4bddbw2qEi4I63DklSAcCfdsj4l8yzRA0FNEU0Pi4toI6aZCIkcfHDNzTEVHBKpgigFq691T6II4hZAZAlk2v4NQauDn7PyL8ZAXrRC1AW7CtcUUMT847MRDg9BeRZBUAb7EwisbRr2qkAEVPvj1fEk5gZDZD'}

    graph = facebook.GraphAPI(token)

    fields = ['id, name,  category, engagement, fan_count, new_like_count, posts.limit(5)']
    fields = ','.join(fields)

    page = graph.get_object('WOSPStaszic', fields=fields)

    print(json.dumps(page, indent=4))

if __name__ == '__main__':
    page()    