Title: The Setup / Neale Pickett
Time-stamp: <2016-06-03 10:47:45 neale>

After reading [Russ Cox's setup](http://russ.cox.usesthis.com/)
I thought it might be interesting to write up my own.



Who are you, and what do you do?
--------------------------------

I am a system programmer and computer forensics researcher at Los
Alamos National Laboratory.

Mostly I hack around the periphery of free software projects,
occasionally tossing patches to projects that capture my interest.
A partial portfolio is on my [source code page](http://woozle.org/neale/src/).

I also do computer security training for middle and high school kids,
college students, and professionals.
You can read about that at [dirtbags](http://dirtbags.net/).

My hobbies include being a (laid back) disc jockey,
and fiddling around with microcontrollers.
I'm active in the local maker community.

I try to minimize energy use,
and to minimize how many mysterious devices are in the house.
These goals used to be at odds with one another,
but recently the two seem to go hand in hand.


My Home Computer
--------

I use a Thinkpad X220 that is usually hooked up to a docking station
and external monitor. Connected to the dock is a Happy Hacking Lite 2
keyboard and Logitech M310 mouse, a Logitech webcam, some old
Sennheiser headphones, and a pair of inexpensive Amazon speakers.

I run Arch Linux with the Gnome 3 desktop,
which is the first Linux desktop environment I actually like.
I think this is mostly because it doesn't try to do many tricks.

I use emacs shell-mode for most command-line work, and
a comint-mode derivative I created for SSH.
I don't usually run any sort of terminal emulator:
everything is `TERM=dumb` inside my emacs SSH sessions.

My other main program is Google Chrome,
with the Flash plugin disabled.
Occasionally I will run Gimp, Inkscape, or Mixxx.


The Family's Computers
-----------------

My wife uses a Chromebook from 2016, which she loves, and my daughter
mostly uses her mobile phone and our 7-inch tablet.  There's a 2011
Chromebook in the house that gets used occasionally, too,
mostly for Google Docs.

Sometimes my wife logs into my laptop, to run Chrome on a bigger screen.

My daughter has an X220 that she used to play Minecraft on,
but it doesn't get much use since Minecraft PE added most of the features she liked.


Other Home Network-Connected Devices
-------------------

I brought in a Google OnHub wireless router in an effort to demystify
the router for my family. It worked.

We also got a couple of Nest thermostats to test the claim that they
pay for themselves. This would probably be true if we had air
conditioning in the house, but we haven't saved enough on heating yet.
But it is handy that they turn the heat off when you leave the house,
and several times we have twiddled the temperature while out of town,
usually to pre-heat the house when we're arriving late on a cold night.

We have a Brother laser printer that connects wirelessly and speakes Google Cloud Print.
I can no longer print natively from Linux,
but it turns out I don't really want to print things from Linux much anymore.
Google Cloud Print lets you submit a PDF through a web form,
so it's not a big problem.

We also have a Chromecast that's mostly used for Netflix,
and a hacked Wii with a few movies on a connect USB hard drive.
Our television is *not* a "smart TV" and I really hope we can avoid ever having to bring such a thing in to the house, they seem slow and buggy, not to mention the ads.

Our car is an all-electric Tesla Model S, which is offset by a small
solar array on the roof.  The car has an ext4-formatted USB flash
drive plugged in, with our entire music collection.


Mobile Computing
-----------------------

The family shares a Nexus 7 tablet.
My wife and daughter use Nexus 5x phones,
and I use a Nexus 6.
My wife and I wear Pebble smartwatches.



What would be your dream setup?
-------------------------------

I'm pretty happy with what I have now,
although I wish I had time to get Acme working for me as nicely as Emacs,
since I am not an Emacs fan.
The thing holding me back is Acme's reliance on special fonts that have not kept pace with Unicode's expansion,
although I need to take another look at the "use system fonts" setup it can do.

It bothers me that X11 is such a horrible mess,
but now that I'm not maintaining my own window manager,
it's less of a concern.
I'm looking forward to Gnome working under Wayland:
Wayland's compositing architecture is the Right Thing,
especially in light of the fact that modern desktops like Gnome
already hack around X11 to get (slow) compositing.

I'd like to get my daughter off her X220 and onto a Chromebook,
because I feel like desktop system administration is a skill she will never need as an adult.
But it's not enough of a concern to make me actually do anything about it.