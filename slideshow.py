#!/usr/bin/env python

"""
Display a png file and report the mouse position on a mouse click.
"""

import argparse
import os
import sys
import tkinter as tk
import subprocess


title_height = 70
margin_x = 20
margin_y = 20

ck_type_header = b'IHDR'

def build_parser():
    """
    Collect command line arguments.
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-i', '--image_filename',
                        default='00dca0b6f6774b846851d5e32eb747aa.png',
                        help='Filename for image. Default: %(default)s')

    parser.add_argument('-d', '--image_dir',
                        default='F:/N/O/SPELLSNO/IMAGES/BIG/00OK',
                        help='Directory for image_filename. Default: %(default)s')

    return parser


def run(cmd):
    """
    Run cmd as a subprocess. Returns stdout.
    """
    process = subprocess.run(cmd, text=True, capture_output=True)
    if process.stderr:
        print(f'Error: stderr={process.stderr}, stdout={process.stdout}')
    return process.stdout


class Application():
    def __init__(self, root, canvas, img, xy):
        """
        xy is an empty list object used to return with width and height.
        """
        self.root = root
        self.width = img.width()
        self.height = img.height()
        self.xy = xy
        canvas.create_image(margin_x, margin_y, anchor=tk.NW, image=img)      
        canvas.bind("<Button-1>", self.callback)


    def callback(self, event):  
        x = event.x - margin_x
        y = event.y - margin_y
        if (x >= 0 and y >= 0
            and x < self.width
            and y < self.height):
            # Return the (x,y) position to the caller.
            self.xy.append(x)
            self.xy.append(y)
            self.root.destroy()


def main(args):
    os.chdir(args.image_dir)
    filename = args.image_filename
    scaled_filename = f'scaled_{args.image_filename}'

    (width, height) = eval(run(['magick', 'identify', '-format', '(%w,%h)', filename]))
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    scale = int(min((screen_width - margin_x * 2) / width,
                    (screen_height - margin_y * 2 - title_height) / height) * 100)
    run(['magick', filename, '-resize', f'{scale}%', scaled_filename])

    # Get w/h of image using imagemagick 

    canvas = tk.Canvas(root, width = screen_width,
                       height = screen_height)
    canvas.pack()      
    # Putting the next line into __init__ causes the image to not appear.
    img = tk.PhotoImage(file=scaled_filename)
    print(img.width(), img.height())
    xy = []
    application = Application(root, canvas, img, xy)
    tk.mainloop()
    (x, y) = xy
    print(x, y)

if __name__ == '__main__':
    sys.exit(main(build_parser().parse_args()))
