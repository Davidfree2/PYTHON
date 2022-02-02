#use chmod +x <filename> on this file to make it executable
#also you can remove .py from this file after using chmod +x
#then move this file into your ~/.local/bin 

#example... chmod +x stockCLI.py 
#example... mv ~/.local/bin

#from there you'll be able to access stock.py from terminal anywhere simply by typing... stock <stockname>
#example... stock aapl 
#will show apples stock information

#after that you can remove this comment text above (DO NOT REMOVE #!/usr/bin/python3)

#thanks for giving this a try :)

#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import sys



#-----------------------START OF HELPING FUNCTIONS-------------

def target_website(url):
    target_web_page = requests.get(url)
    if target_web_page.status_code != 400:
        return target_web_page.content
    else:
        return 'ERROR'

def soupify_website(website_data, tag, target_class=None):
    if target_class:
        souped_website = BeautifulSoup(website_data, 'html.parser') 
        souped_target_item = souped_website.find_all(str(tag), class_=str(target_class))
        soup_target_item_number = souped_target_item
        return soup_target_item_number
    else:
        souped_website = BeautifulSoup(website_data, 'html.parser') 
        souped_target_item = souped_website.find_all(str(tag))
        soup_target_item_number = souped_target_item
        return soup_target_item_number


def strip_tags(souped_website):
    for data in souped_website(['style', 'script']):
        data.decompose()
        print(data)
    return ' '.join(souped_website.stripped_strings)

def stock_name(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'D(ib) Fz(18px)'
    tag = 'h1'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[0])
    return f'{sentence_without_tags}'

def stock_price(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Fw(b) Fz(36px) Mb(-4px) D(ib)'
    tag = 'fin-streamer'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[0])
    return f'PRICE: {sentence_without_tags}'

def stock_gain_percent(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Fw(500) Pstart(8px) Fz(24px)'
    tag = 'fin-streamer'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[1])
    return f' / {sentence_without_tags}%'

def stock_gain_dollars(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Fw(500) Pstart(8px) Fz(24px)'
    tag = 'fin-streamer'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[0])
    return f'GAIN: {sentence_without_tags}$'

def previous_close(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Ta(end) Fw(600) Lh(14px)'
    tag = 'td'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[0])
    #return f'previous close {sentence_without_tags[15:21]}'
    return f'previous close: {sentence_without_tags}'

def stock_open(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Ta(end) Fw(600) Lh(14px)'
    tag = 'td'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[1])
    #return f'open {sentence_without_tags[27:33]}'
    return f'open: {sentence_without_tags}'

def bid(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Ta(end) Fw(600) Lh(14px)'
    tag = 'td'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[2])
    #return f'day range {sentence_without_tags[81:96]}'
    return f'bid: {sentence_without_tags}'

def ask(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Ta(end) Fw(600) Lh(14px)'
    tag = 'td'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[3])
    #return f'day range {sentence_without_tags[81:96]}'
    return f'ask: {sentence_without_tags}'

def day_range(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Ta(end) Fw(600) Lh(14px)'
    tag = 'td'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[4])
    #return f'day range {sentence_without_tags[81:96]}'
    return f'day range: {sentence_without_tags}'

def week_range(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Ta(end) Fw(600) Lh(14px)'
    tag = 'td'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[5])
    #return f'52week range {sentence_without_tags[111:126]}'
    return f'52week range: {sentence_without_tags}'

def volume(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Ta(end) Fw(600) Lh(14px)'
    tag = 'td'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[6])
    #return f'volume average {sentence_without_tags[134:144]}'
    return f'volume: {sentence_without_tags}'

def volume_average(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Ta(end) Fw(600) Lh(14px)'
    tag = 'td'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[7])
    #return f'volume average {sentence_without_tags[134:144]}'
    return f'volume average: {sentence_without_tags}'

def market_cap(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Ta(end) Fw(600) Lh(14px)'
    tag = 'td'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[8])
    #return f'market cap {sentence_without_tags[179:185]}'
    return f'market cap: {sentence_without_tags}'

def beta(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Ta(end) Fw(600) Lh(14px)'
    tag = 'td'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[9])
    #return f'market cap {sentence_without_tags[179:185]}'
    return f'beta: {sentence_without_tags}'

def pe_ratio(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Ta(end) Fw(600) Lh(14px)'
    tag = 'td'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[10])
    #return f'market cap {sentence_without_tags[179:185]}'
    return f'pe ratio: {sentence_without_tags}'

def eps(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Ta(end) Fw(600) Lh(14px)'
    tag = 'td'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[11])
    #return f'market cap {sentence_without_tags[179:185]}'
    return f'eps: {sentence_without_tags}'

def earnings_date(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Ta(end) Fw(600) Lh(14px)'
    tag = 'td'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[12])
    #return f'market cap {sentence_without_tags[179:185]}'
    return f'earnings date: {sentence_without_tags}'

def forward_dividend(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Ta(end) Fw(600) Lh(14px)'
    tag = 'td'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[13])
    #return f'market cap {sentence_without_tags[179:185]}'
    return f'forward dividend rate: {sentence_without_tags}'

def ex_dividend_date(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Ta(end) Fw(600) Lh(14px)'
    tag = 'td'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[14])
    #return f'market cap {sentence_without_tags[179:185]}'
    return f'expected dividened date: {sentence_without_tags}'

def one_year_target(stock):
    site = str('https://finance.yahoo.com/quote/' + stock.upper())
    class_name = 'Ta(end) Fw(600) Lh(14px)'
    tag = 'td'

    #website tag
    website = target_website(site)
    soupied = soupify_website(website, tag, class_name)
    sentence_without_tags = strip_tags(soupied[15])
    #return f'market cap {sentence_without_tags[179:185]}'
    return f'1 year target: {sentence_without_tags}'

#-----------------------END OF HELPING FUNCTIONS-------------



#-----------------------MAIN ENTRY FUNCTION-------------------

def main(stock):
    try:
        my_stock_name = stock_name(stock)
        my_stock_price = stock_price(stock)
        my_stock_gain_percent = stock_gain_percent(stock)
        my_stock_gain_dollars = stock_gain_dollars(stock)
        my_previous_close = previous_close(stock)
        my_bid = bid(stock)
        my_ask = ask(stock)
        my_stock_open = stock_open(stock)
        my_day_range = day_range(stock)
        my_week_range = week_range(stock)
        my_volume = volume(stock)
        my_volume_average = volume_average(stock)
        my_market_cap = market_cap(stock)
        my_one_year_target = one_year_target(stock)
        myex_dividened_date = ex_dividend_date(stock)
        my_forward_dividend = forward_dividend(stock)
        my_earnings_date = earnings_date(stock)
        my_eps = eps(stock)
        my_pe_ratio = pe_ratio(stock)
        my_beta = beta(stock)
        print(f'''
    -------------{my_stock_name}-------------
    
    {my_stock_price}
    {my_stock_gain_dollars}{my_stock_gain_percent}
    
    {my_market_cap}
    {my_earnings_date}
    
    {myex_dividened_date}
    {my_forward_dividend}
    
    {my_previous_close}
    {my_stock_open}
    
    {my_bid}
    {my_ask}
    
    {my_day_range}
    {my_week_range}
    
    {my_volume}
    {my_volume_average}
    
    {my_eps}
    {my_pe_ratio}
    
    {my_one_year_target}
    {my_beta}
        ''')
    except:
        print('''
    ERROR

    PLEASE TYPE VALID STOCK NAME BY USING--------------
    stock <ticker>

    EXAMPLE OF USAGE: stock ford
    EXAMPLE OF USAGE: stock nkla

    EXAMPLE OF STOCKS: aapl, ford, nkla, f, amd, tsla, pfe
                ''')


your_cli_entry = str(sys.argv[1])

main(your_cli_entry)


