import requests
import notify2
from bs4 import BeautifulSoup




def target_website(url):
    target_web_page = requests.get(url)
    if target_web_page.status_code != 400:
        return target_web_page.content
    else:
        return 'ERROR'

def soupify_website(website_data, target_class, target_number):
    souped_website = BeautifulSoup(website_data, 'html.parser') 
    souped_target_item = souped_website.find_all('p', class_=str(target_class))
    soup_target_item_number = souped_target_item[int(target_number)]
    return soup_target_item_number

def strip_tags(souped_website):
    for data in souped_website(['style', 'script']):
        data.decompose()
    return ' '.join(souped_website.stripped_strings)


def desktop_notification(title, body):
    notify2.init('newsNotifier')
    notification_title = str(title)
    notification_body = body
    notify = notify2.Notification(notification_title, notification_body)
    notify.add_action("close","Close",None)
    notify.show()


#Entry point of program logic start here
def main():
    #website and classname tag init
    site = 'https://www.cbsnews.com/'
    class_name = 'item__dek'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, class_name, 1)
        #type of soupied must be equal to: <class 'bs4.element.Tag'>
    sentence_without_tags = strip_tags(soupied)

    #desktop notifier
    desktop_notification('CBS notifier', sentence_without_tags)


main()
