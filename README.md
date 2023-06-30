# slideshow
Display images in some order.

The program works.py displays a png file. When the user clicks ths
mouse it prints the coordinates.

The image is scaled to the screen width.

Got rid of the image header parsing and instead use magick to determine the size.

TODO:

use the async stuff to code a new version of slideshow.py
The async process will display a random image
When the sleep time completes, start another process to display a random image
and then leave the formerly sleeping process
May use events to load the next image while sleeping.
Use event to indicate the the sleep has expired.

load image in p1
start p2 to load another image
in p2 wait for event
in p1 when sleep expires trigger event and leave function
in p2 start p3 to load a 3rd image
in p3 wait for event
in p2 when sleep expires trigger event and leave function

in pi start pi+1 to load ith image
in pi+1 wait for event
in pi when sleep expires trigger event and leave function


--old--
  mainloop is a tcl thing.
  tkinter is here:
    c:/Users/Tom Ekberg/AppData/Local/Programs/Python/Python310/Lib/tkinter/

  get threading to work
    When parallel closes out and tries to root.destroy() it fails because
	that can only be done in the main thread.
	Need to look at doing my own main loop.
    Need to try and have parallel tell the main thread to stop.
	  Pass application to parallel. When time has expired,
	  call application.callback with an event x/y=0
  put in a loop
    Looking to do multithreading with tkinter. The other
	function would sleep after the image appears and exit mainloop.
---- done ---------------------------------------------------------------------
  Look at this
    https://github.com/insolor/async-tkinter-loop
  randomize


Create A Virtualenv And Install Dependencies
--------------------------------------------

Run these commands::
  python -m venv ss-env
  source ss-env/scripts/activate
  pip install pip -U # Latest pip
  pip install -r requirements.txt
