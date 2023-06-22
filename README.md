# slideshow
Display images in some order.

The program works.py displays a png file. When the user clicks ths
mouse it prints the coordinates.

The image is scaled to the screen width.

Got rid of the image header parsing and instead use magick to determine the size.

TODO:
  put in a loop
    Looking to do multithreading with tkinter. The other
	function would sleep after the image appears and exit mainloop.
---- done ---------------------------------------------------------------------
  randomize
