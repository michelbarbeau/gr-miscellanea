#!/usr/bin/env python
# Sound card audio to file example
# Author: Michel Barbeau
# Version: February 15, 2016
from gnuradio import blocks
from gnuradio import gr
from gnuradio import audio


class Model(gr.top_block):

   def __init__(self):
      gr.top_block.__init__(self)

      # Create an audio source (a software abstraction of the sound card, assumed
      # to be the default audion input source), sample rate is 48000 sps
      source = audio.source(48000, "")
      # Create a file sink (sample data format is 32-bit float)
      sink = blocks.file_sink(gr.sizeof_float, "mysamples.dat")
      # Connect source and sink
      self.connect(source, sink)

if __name__ == '__main__': 
   try:
      Model().run()
   except KeyboardInterrupt:
      pass
