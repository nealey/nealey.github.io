#! /bin/sh

case "$HTTP_USER_AGENT" in
    *MIDP*)
        TINY=1
        NOCAL=1
        ;;
    *Mobile*)
        NOCAL=1
        ;;
esac

weather () {
    curl -s 'http://rss.wunderground.com/auto/rss_full/NM/Los_Alamos.xml?units=metric' | \
        awk -F ' [-:] ' '
(/Current Conditions/) { 
  print "<p class=\"weather\"><a href=\"http://m.wund.com/cgi-bin/findweather/getForecast?brand=mobile&query=87544\">" $2 "</a></p>"; 
} 

(c == 2) {
  print "<p class=\"weather\">" $0 "</p>"; 
  exit; 
} 

(/CDATA/) {
  c++;
}'

}

section () {
    echo "<h2><a href=\"$2\">$1</a></h2>"
    echo "<ul>"
    [ "$TINY" ] && pfx="http://news.google.com/gwt/x?u="
    curl -s "$3" | \
        awk -F '>' -v RS='<' -v m=${4:-5} -v pfx="$pfx" '
(/^item[> ]/) {
  a++;
}

(/^title/) {
  title=$2;
}

(a && a<m+1 && /^link/) {
  l=$2;
  sub(/.*url=/, "", l);
  print "<li><a href=\"" pfx l "\">" title "</a></li>";
}'

    echo "</ul>"
}

cat <<EOF
Content-type: text/html; charset=utf-8
Refresh: 500

<!DOCTYPE html>
<html>
  <head>
    <title>Houyhnhnm</title>
    <style type="text/css">
h1 { 
  font-size: large; 
  font-weight: bold;
  text-align: center;
}
h2 {
  font-size: large;
  font-weight: normal;
  font-style: italic;
}
.calendar {
  height: 300px;
  float: right;
}
    </style>
    <link rel="icon" type="image/png" href="portal.png">
    <meta name="viewport" content="width=device-width" />
  </head>
  <body>
EOF

if ! [ "$NOCAL" ]; then
    printf '<iframe class="calendar" src="%s"></iframe>\n' \
        'https://www.google.com/calendar/embed?title=Calendar&showTitle=0&showDate=0&showPrint=0&showTz=0&mode=AGENDA&height=350&wkst=1&bgcolor=%23FFFFFF&src=2cdrf19kah6jkonhom8evck38c%40group.calendar.google.com&color=%23333333&src=s531giqfiotabht4qrn59tjf9g%40group.calendar.google.com&color=%231B887A&src=dartcatcher%40gmail.com&color=%23125A12&src=laderbydames%40gmail.com&color=%2323164E&src=uulosalamos.org_gu7e0s8dsh1tn8iktt468tk95k%40group.calendar.google.com&color=%232F6309&src=en.usa%23holiday%40group.v.calendar.google.com&color=%238D6F47&ctz=America%2FDenver'
fi

if [ "$TINY" ]; then
    echo '<form action="http://www.google.com/"><input name="q" size="12"><input type="submit" value="G">'
    echo '</form>'
fi

weather

section LA \
    'http://ladailypost.com/' \
    'http://www.ladailypost.com/rss.xml'
section "Ars Technica" \
    'http://m.arstechnica.com/' \
    'http://feeds.arstechnica.com/arstechnica/index?format=xml'
section NPR \
    'http://thin.npr.org/t.php?tid=1001' \
    'http://www.npr.org/rss/rss.php?id=1001'
section CSM \
    'http://www.csmonitor.com/textedition' \
    'http://rss.csmonitor.com/feeds/csm'
section AJE \
    'http://m.aljazeera.net' \
    'http://www.aljazeera.com/Services/Rss/?PostingId=2007731105943979989'
cat <<EOF
  </body>
</html>
EOF
