Title: Firebot: IRC Automaton

FireBot is a winner!

Firebot is an IRC bot combining the functionality of a Linkbot, an
Infobot, and a Clickolinko, which is this cool thing Emad El-Haraty and
I came up with to make short URLs out of stuff posted into the channel,
for people with text browsers that wrap URLs.

Note that, in addition to interacting with FireBot within a channel, you
can also communicate directly with FireBot via `/msg` commands. Just in
case you need a little one-on-one action and don't want spew your
playtime around some channel with other folks watching. That can be *so*
distracting. Some commands still require you to preface them with
FireBot's name. Example:

    /msg firebot firebot: literal ...


Downloading
-----------

You can download a [tarball snapshot of the latest release](http://woozle.org/~neale/g.cgi/firebot/snapshot/firebot-master.tar.gz), or use cogito:

    git clone http://woozle.org/~neale/projects/firebot


LinkBot Features
----------------

Firebot can link channels across networks.  It is present in all
channels and the same functions can be accessed on either side.
Everything said on one channel is relayed to the others.

It is possible to link multiple channels on multiple servers, including
multiple channels on a single server.



ClickLinko (UrlBot)
-------------------

Whenever FireBot sees a URL in the channel, he makes a note of it and
creates a shorter URL out of it.



InfoBot
-------

As an InfoBot, FireBot listens in the channel for anything of the form
"x is y", and then stores that little tidbit.  Later, when someone asks
a question about x ("what is x?", "who is x?", "wtf is x?"), FireBot
answers with the factoid he gathered.

<dl>
<dt>firebot, **x**</dt>
<dd>look up a factoid for **x**</dd>

<dt>firebot, **x** is **y**</dt>
<dd>store **y** as a factiod about **x**</dd>

<dt>firebot, **x** is also **y**</dt>
<dd>store **y** as another factoid about **x**</dd>

<dt>firebot, append **x** &lt;= **y**</dt>
<dd>store **y** as another factoid about **x**.  You'd use this for things where **x** has the word "is" in it, or other things that you can't store with the preceding commands.</dd>

<dt>no, firebot, **x** is **y**</dt>
<dd>store **y** as the only factoid about **x**, even if **x** already has factoids</dd>

<dt>firebot, literal **x**</dt>
<dd>display all factoids about **x**</dd>

<dt>firebot, lock **x**</dt>
<dd>do not learn any more factoids about **x**</dd>

<dt>firebot, unlock **x**</dt>
<dd>resume learning factoids about **x**</dd>

<dt>firebot, forget **x**</dt>
<dd>forget all factoids about **x**</dd>

<dt>firebot, forget **x** from **y**</dt>
<dd>forget a single entry (**x**) that is listed in **y**; **x** can be a single word, it does not need to be the whole entry</dd>

<dt>firebot, shut up</td>
<dd>make the bot only respond to factoids when addressed specifically</dd>

<dt>firebot, be chatty</td>
<dd>make the bot respond to factoids even when not addressed</dd>

</dl>

In addition, the following tricks can be used within factiods:

* Any factoid beginning with `\\` (a backslash) is displayed directly.
  That is, instead of saying "<firebot> x is y", FireBot just says
  "<firebot> y". 
* Any factoid beginning with <code>:</code> (a colon) is
  displayed an action.  That is, instead of saying "<firebot> x is y",
  FireBot says "* firebot y" 
* You may put `%(sender)s` in the factoid to print the name of the
  person who asked about the factoid (when sent to a user in a private
  message, it's the recipient of the message)



Utilities
---------

<dl>

<dt>firebot, later tell **whom** **what**</dt>
<dd>The next time **whom** says something in the channel, deliver the message **what** publically.</dd>

<dt>firebot, in **time** say **what**</dt>
<dd>after **time** (eg. "15 seconds", "2 hours", "5 days"), announce **what** in the channel</dd>

<dt>seen **whom**</dt>
<dd>Report the last thing said in the channel by **whom**, and how long ago it was said.</dd>

<dt>dict **word**</dt>
<dd>look **word** up in the dictionary</dd>

<dt>quote **symbol**</dt>
<dd>get a stock quote for **symbol**</dd>

<dt>pollen **zip**</dt>
<dd>report pollen forecast for US zip code **zip**</dd>

<dt>cdecl explain **jibberish**</dt>
<dd>explain the C declaration **jibberish** (eg. "cdecl explain struct bar *(*foo)[](int)")</dd>

<dt>cdecl declare **english**</dt>
<dd>give the C declaration for **english** (eg. "cdecl declare foo as pointer to array of function (int) returning pointer to struct bar")</dd>

<dt>how many **x** in **y** **z**</dt>
<dd>determine the number of **x** items that are contained in **y** amount of **z** items (eg. how many miles in 1 light year)</dd>

<dt>how much is **amt** **source** in **dest**</dt>
<dd>do a currency conversion from **source** to **dest**.  Both must be three-letter currency codes. (eg. "how much is 100 USD in EUR")</dd>

<dt>calc **expr**</dt>
<dd>calculate **expr** (eg. "calc 2 * 5")</dd>

</dl>


Toys
----

<dl>

<dt>8ball, **question**</dt>
<dd>consult the magic 8-ball regarding **question**</dd>

<dt>**nickname**++</dt>
<dd>add a whuffie point for **nickname**</dd>

<dt>**nickname**--</dt>
<dd>remove a whuffie point for **nickname**</dd>

<dt>whuffie for **nickname**</dt>
<dd>check the whuffie for **nickname**</dd>

</dl>