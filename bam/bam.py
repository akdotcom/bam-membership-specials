# coding: utf-8
import logging
from abstract_app import AbstractApp

SPECIALS = {
      "46cb0dedf964a5202a4a1fe3" : { "name" : "Alchemy Restaurant", "special" : "10% off total bill" },
      "4db328bf93a017099dbdb946" : { "name" : "A la Crepe Cafe", "special" : "Members recieve 20% off the total bill" },
      "4a59109ef964a52093b81fe3" : { "name" : "Aqualis Grill", "special" : "Complimentary dessert" },
      "4a22b709f964a520827d1fe3" : { "name" : "AOC Bistro", "special" : "Complimentary glass of wine" },
      "41e46880f964a520e11e1fe3" : { "name" : "Bacchus", "special" : "$25 prix—fixe dinner menu including three courses" },
      "4a81a364f964a5201bf71fe3" : { "name" : "Bark Hot Dogs", "special" : "Complimentary glass of wine or any Six Point Draft Ale on tap" },
      "4ac3e617f964a520599d20e3" : { "name" : "Bati", "special" : "10% of total bill" },
      "4b8ed35ef964a520693933e3" : { "name" : "Benchmark Restaurant", "special" : "Complimentary dessert" },
      "4acbe4fbf964a52040c820e3" : { "name" : "Caffe e Vino", "special" : "$25 prix-fixe dinner (includes four courses) or 10% off total bill" },
      "49c55b73f964a520fb561fe3" : { "name" : "Chez Lola", "special" : "Complimentary glass of wine with dinner" },
      "439591fcf964a5208c2b1fe3" : { "name" : "Chez Oskar", "special" : "$22 prix-fixe menu (includes two courses and a glass of wine) " },
      "4a4f8105f964a52060af1fe3" : { "name" : "Der Schwarze Kölner", "special" : "1 free Kölsch with meal" },
      "4a947f02f964a520ce2120e3" : { "name" : "Deniz Turkish and Mediterranean Restaurant", "special" : "Complimentary dessert with meal" },
      "45850853f964a5209f3f1fe3" : { "name" : "Flatbush Farm", "special" : "Complimentary glass of wine with purchase of entrée" },
      "4bc3c7fcb492d13ac44ea960" : { "name" : "Fornino", "special" : "Complimentary glass of wine" },
      "422b9980f964a520d21f1fe3" : { "name" : "ICI", "special" : "Complimentary dessert" },
      "3fd66200f964a5207cf11ee3" : { "name" : "Junior's Restaurant", "special" : "Complimentary slice of plain cheesecake with lunch or dinner entrée" },
      "4a6bc0caf964a520d7cf1fe3" : { "name" : "Linger Café & Lounge", "special" : "10% off checks of $25 or more." },
      "4a6ce87df964a52004d21fe3" : { "name" : "Lunetta", "special" : "Complimentary glass of wine" },
      "4594df9af964a52063401fe3" : { "name" : "Melt", "special" : "Juicy, grass-fed burgers, innovative cocktails, fine wine, and happy hour specials" },
      "43261680f964a520b6271fe3" : { "name" : "Miriam Resturant", "special" : "10% off total bill" },
      "45548f85f964a5200f3d1fe3" : { "name" : "Mullanes Bar & Grill", "special" : "10% off total bill (not combined with any other offer)" },
      "44fc6a24f964a52084381fe3" : { "name" : "Olea Mediterranean Taverna", "special" : "Complimentary glass of wine with meal" },
      "3fd66200f964a5207beb1ee3" : { "name" : "Ozzies's Coffee & Tea", "special" : "10% off total bill" },
      "49bca8d2f964a52044541fe3" : { "name" : "Pequeña", "special" : "Complimentary homemade chips and pico de gallo" },
      "4c243968b7b8a593543d3ce8" : { "name" : "Pequeña", "special" : "Complimentary homemade chips and pico de gallo" },
      "458d10b5f964a52001401fe3" : { "name" : "The Smoke Joint", "special" : "Complimentary iced tea or limonade with purchase of entrée" },
      "41abb800f964a520551e1fe3" : { "name" : "Stonehome Wine Bar", "special" : "Complimentary glass of Prosecco" },
      "4aa5af70f964a520294920e3" : { "name" : "Stone Park Cafe", "special" : "10% off total bill" },
      "4e622a6fb0fb188e8d907d81" : { "name" : "Tillie's of Brooklyn", "special" : "Complimentary coffee and cookies" },
      "4a3e86c5f964a520ffa21fe3" : { "name" : "The Chocolate Room", "special" : "10% off total bill" },
      "49e14fdbf964a520ba611fe3" : { "name" : "The Chocolate Room", "special" : "10% off total bill" },
      "4adcc0a7f964a520702f21e3" : { "name" : "The Vanderbilt", "special" : "Complimentary glass of wine" },
    }

class BamMembershipSpecials(AbstractApp):

  def checkinTaskQueue(self, client, checkin_json):
    venue_id = checkin_json['venue']['id']
    if venue_id not in SPECIALS:
      return

    message = SPECIALS[venue_id]["special"]
    params = { 'text' : message}
    if CONFIG['local_dev']:
      logging.info(params)
      return
    client.checkins.reply(checkin_json['id'], params)

