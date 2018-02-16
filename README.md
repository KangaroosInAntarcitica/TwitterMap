# Twitter Map

   ### The app could be found and tries on [PythonAnywhere.com](http://kangaroosinantarctica.pythonanywhere.com)

   It uses another github repositry - *[twitter_api](https://github.com/anrom7/twitter_api) by [anrom7](https://github.com/anrom7/twitter_api).   
   (Copyright (c) 2007 Leah Culver, MIT license)
   
   
   The program finds a person and all friends of a [Twitter](https://twitter.com/twitter) user and then displays it all on map.   
   
   The code, that is used to parse twitter api can be found in the [twitter_parser.py](https://github.com/KangaroosInAntarcitica/TwitterMap/blob/master/twitter_parser.py) file
(which uses oauth.py and twurl.py to get info from twitter).   
   It then reads the requested json file and gets all the useful information from it (like user name, screen_name, location, followers...)   
   It also gets the geocode for location specified by twitter user (or sets it to (None, None) if nothing found)   
   
   The file [twitter_server.py](https://github.com/KangaroosInAntarcitica/TwitterMap/blob/master/twitter_server.py) displays the user
and his friends on a map (using geocode coordinates), together with some information from his account and link to his account.   

   ### Examples:   

![twitter map](https://github.com/KangaroosInAntarcitica/TwitterMap/blob/master/__temp__/example1.PNG)
![twitter map](https://github.com/KangaroosInAntarcitica/TwitterMap/blob/master/__temp__/example2.PNG)
![twitter map](https://github.com/KangaroosInAntarcitica/TwitterMap/blob/master/__temp__/example3.PNG)
