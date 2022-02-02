Termial stocks! Just run python3 stockCLI.py <stockticker> to show stocks from the terminal.
Example from command line------------
python3 stockCLI.py aapl #this will show apples current stock
python3 stockCLI.py ford #this will show fords current stock

you can also run this as an executable file anywhere in your system by:

1.use chmod +x <filename> on this file to make it executable
2.also you can remove .py from this file after using chmod +x
3.then move this file into your ~/.local/bin 

example... chmod +x stockCLI.py 
example... mv ~/.local/bin

from there you'll be able to access stock.py from terminal anywhere simply by typing... stockCLI <stockname>
example... stockCLI aapl 
will show apples stock information

after that you can remove the comment text in stockCLI.py but DO NOT REMOVE #!/usr/bin/python3

thanks for giving this a try :)
shoot me a message. let me know what you think
