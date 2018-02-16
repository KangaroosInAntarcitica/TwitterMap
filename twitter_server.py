from twitter_parser import *

from flask import Flask, render_template, request, redirect
import folium


def create_popup(people):
    """
    Creates a html popup, to link with a folium marker
    :param people: list with info about multiple people from twitter
    :return: (str) - html code
    """
    result = '<div class="popupC"> <div class="popupC2">'
    for data in people:
        result += render_template('popup.html', data=data, str=str)

    return result + '</div> </div>'


def create_map(account, count):
    """
    Creates a map of people for account (person and friends)
    :param account; :param count - twitter user & number of friends
    :return: html code for map
    """
    # get all the info (user & his friends)
    person = parse_account(get_info(TW_URL, account, count))[0]
    friends = get_info(TW_FRIENDS, account, count)["users"]
    friends = [*map(parse_account, friends)]

    # create a dict, so that we can output multiple people in one place
    # first item in array stands for important (has requested person in it)
    people_dict = {person['geocode']: [1, person]}
    for item in friends:
        item = item[0]
        if item['geocode'] in people_dict:
            people_dict[item['geocode']].append(item)
        else:
            people_dict[item['geocode']] = [0, item]

    # add map
    new_map = folium.Map(location=[0, 0], zoom_start=1, tiles='Stamen Terrain')

    # add markers to map if the geocode is not (None, None)
    for key, value in people_dict.items():
        if key[0] == None or key[1] == None:
            continue

        folium.Marker([key[0], key[1]],
                      popup=create_popup(value[1:]),
                      icon=folium.Icon(
                          color='lightred' if value[0] else 'lightblue',
                          icon='fa-child', prefix='fa'
                      )
                      ).add_to(new_map)

    return new_map.get_root().render()


app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/twittermap')

@app.route('/twittermap')
def twitter_map():
    """
    Gets all the required information and returns the start page or map with
    people locations depending on input
    """
    # get arguments from url
    account = request.args.get('q')
    count = request.args.get('count')

    if account and count:
        # create map and add custom styles to html or display error
        try:
            new_map = create_map(account, count)
            new_map += render_template('styles.html')
            return new_map
        except urllib.error.HTTPError:
            return render_template('error.html', error='User was not found.')

    else:
        # render start page
        return render_template('index.html')


app.run(debug=True)