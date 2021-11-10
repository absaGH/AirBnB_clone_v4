
Skip to content
Pulls
Issues
Marketplace
Explore
@Yosef-S-A
Yosef-S-A /
AirBnB_clone_v4
Public
forked from coosoti/AirBnB_clone_v4

0
0

    1

Code
Pull requests
Actions
Projects
Wiki
Security
Insights

More
AirBnB_clone_v4/web_dynamic/101-hbnb.py /
@Yosef-S-A
Yosef-S-A task 2, 3, 4, 5, 6
Latest commit 48f3fe0 on Sep 26
History
1 contributor
executable file 50 lines (38 sloc) 1.31 KB
#!/usr/bin/python3
""" Starts a Flash Web Application """
import uuid
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/101-hbnb/', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    cache_id = str(uuid.uuid4())

    return render_template('101-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)



if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

    © 2021 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Docs

    Contact GitHub
    Pricing
    API
    Training
    Blog
    About

Loading complete
