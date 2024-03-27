import uiautomator2 as u2
import time

d = u2.connect_usb('RZ8N80DL7KH') # enter your device number by running adb devices
d.app_start("com.instagram.android")

story_icon_id = "com.instagram.android:id/avatar_container" # resource id of the buttons to view stories
num_story_clicks = 5

def watch_and_navigate_story():
    story_xpath = '//*[@resource-id="' + story_icon_id + '"]'
    while True: 
        if d.xpath(story_xpath).exists:
            d.xpath(story_xpath).click()
            break  
        time.sleep(2)  # timeout of 2 seconds after click

   # Click on the right side for story navigation and viewing other stories
    width, height = d.info["displaySizeDpX"], d.info["displaySizeDpY"]  
    for _ in range(num_story_clicks):
        x = width * 0.8  
        y = height / 2 
        d.click(x, y) 
        time.sleep(2) 

while True:
    if story_icon_id in d.dump_hierarchy():  
        watch_and_navigate_story()
    else:
        print("No stories available to view")
