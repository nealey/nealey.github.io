Title: Eguile : a scheme preprocessor
Author: Neale Pickett <neale@woozle.org>

If you've ever wished your text preprocessor could do symbolic
derivation, eguile is the tool for you!

eguile is a preprocessor which lets you include Scheme code in your
source files--any source files, not just HTML. With the bundled
ntp-style.scm, you can give web pages a consistent interface with easy
navigation bars, just like this page. Further functionality is limited
only by your imagination and programming ability.

eguile looks like PHP, but with Scheme instead of Perl.  If you're the
sort of person that would enjoy something like this, you probably don't
need any further description.


Downloading it
--------------------------

[eguile.scm](http://woozle.org/~neale/src/eguile/eguile.scm).


Reference
--------------------------

Easy squeezy:

<dl>
  <dt>&lt;?scm scheme-code ?&gt;</dt>
  <dd>Evaluates scheme-code, discarding value of the last expression</dd>

  <dt>&lt;?scm:d scheme-code ?&gt;</dt>
  <dd>Evaluates scheme-code, displaying the value of the last expression</dd>
</dl>

For example:

    <?scm (define (square x) (* x x)) ?>
    2 squared is <?scm:d (square 2) ?>

renders as:

    2 squared is 4


Inspiration
--------------------------

I modeled eguile after ht2html by Barry Warsaw (a far cooler cat than
I). ht2html is a slick package, but it didn't feel enough like
programming to me and seemed more complicated than it needed to be. escm
seemed like a better solution, but felt a little too kludgy, and I
needed to learn Scheme better anyway. So I stole the layout from ht2html
and the syntax from escm.


License
--------------------------

eguile is distributed under the GNU Public License version 2.0 or
later. Please refer to the file COPYING for more information.