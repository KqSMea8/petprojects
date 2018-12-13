
import re
import json
import os
import sys
from faker import Faker

from multiprocessing import Process, Queue

from bs4 import BeautifulSoup
import requests as rq

finst = Faker()

sys.setrecursionlimit(10000)

links = [
    "http://facebook.com",
    "http://twitter.com",
    "http://google.com",
    "http://youtube.com",
    "http://instagram.com",
    "http://linkedin.com",
    "http://wordpress.org",
    "http://pinterest.com",
    "http://wikipedia.org",
    "http://wordpress.com",
    "http://blogspot.com",
    "http://apple.com",
    "http://adobe.com",
    "http://tumblr.com",
    "http://youtu.be",
    "http://amazon.com",
    "http://goo.gl",
    "http://vimeo.com",
    "http://flickr.com",
    "http://microsoft.com",
    "http://yahoo.com",
    "http://godaddy.com",
    "http://qq.com",
    "http://bit.ly",
    "http://vk.com",
    "http://reddit.com",
    "http://w.org",
    "http://baidu.com",
    "http://nytimes.com",
    "http://t.co",
    "http://europa.eu",
    "http://buydomains.com",
    "http://wp.com",
    "http://statcounter.com",
    "http://miitbeian.gov.cn.cn",
    "http://jimdo.com",
    "http://blogger.com",
    "http://github.com",
    "http://weebly.com",
    "http://soundcloud.com",
    "http://mozilla.org",
    "http://bbc.co.uk.uk",
    "http://yandex.ru",
    "http://myspace.com",
    "http://google.de",
    "http://addthis.com",
    "http://nih.gov",
    "http://theguardian.com",
    "http://google.co.jp.jp",
    "http://cnn.com",
    "http://stumbleupon.com",
    "http://gravatar.com",
    "http://digg.com",
    "http://addtoany.com",
    "http://creativecommons.org",
    "http://paypal.com",
    "http://yelp.com",
    "http://imdb.com",
    "http://huffingtonpost.com",
    "http://feedburner.com",
    "http://issuu.com",
    "http://wixsite.com",
    "http://wix.com",
    "http://dropbox.com",
    "http://forbes.com",
    "http://miibeian.gov.cn.cn",
    "http://amazonaws.com",
    "http://google.co.uk.uk",
    "http://washingtonpost.com",
    "http://bluehost.com",
    "http://etsy.com",
    "http://go.com",
    "http://msn.com",
    "http://wsj.com",
    "http://ameblo.jp",
    "http://archive.org",
    "http://slideshare.net",
    "http://e-recht.de.de",
    "http://weibo.com",
    "http://fc.com",
    "http://eventbrite.com",
    "http://parallels.com",
    "http://doubleclick.net",
    "http://mail.ru",
    "http://sourceforge.net",
    "http://amazon.co.uk.uk",
    "http://telegraph.co.uk.uk",
    "http://ebay.com",
    "http://amzn.to",
    "http://livejournal.com",
    "http://free.fr",
    "http://yahoo.co.jp.jp",
    "http://dailymail.co.uk.uk",
    "http://reuters.com",
    "http://taobao.com",
    "http://wikimedia.org",
    "http://amazon.de",
    "http://typepad.com",
    "http://hatena.ne.jp.jp",
    "http://bloomberg.com",
    "http://elegantthemes.com",
    "http://eepurl.com",
    "http://usatoday.com",
    "http://about.com",
    "http://medium.com",
    "http://macromedia.com",
    "http://xing.com",
    "http://bing.com",
    "http://time.com",
    "http://gov.uk.uk",
    "http://google.it",
    "http://cdc.gov",
    "http://tripadvisor.com",
    "http://cpanel.net",
    "http://amazon.co.jp.jp",
    "http://npr.org",
    "http://harvard.edu",
    "http://bbb.org",
    "http://aol.com",
    "http://constantcontact.com",
    "http://latimes.com",
    "http://icio.us",
    "http://list-manage.com.com",
    "http://webs.com",
    "http://opera.com",
    "http://beian.gov.cn.cn",
    "http://vkontakte.ru",
    "http://blogspot.co.uk.uk",
    "http://live.com",
    "http://bandcamp.com",
    "http://apache.org",
    "http://bbc.com",
    "http://businessinsider.com",
    "http://dailymotion.com",
    "http://cpanel.com",
    "http://disqus.com",
    "http://behance.net",
    "http://mit.edu",
    "http://rambler.ru",
    "http://gnu.org",
    "http://sina.com.cn.cn",
    "http://spotify.com",
    "http://joomla.org",
    "http://google.es",
    "http://line.me",
    "http://wired.com",
    "http://github.io",
    "http://stanford.edu",
    "http://googleusercontent.com",
    "http://kickstarter.com",
    "http://guardian.co.uk.uk",
    "http://imgur.com",
    "http://google.fr",
    "http://goodreads.com",
    "http://nasa.gov",
    "http://rakuten.co.jp.jp",
    "http://surveymonkey.com",
    "http://delicious.com",
    "http://independent.co.uk.uk",
    "http://whatsapp.com",
    "http://one.com",
    "http://photobucket.com",
    "http://ted.com",
    "http://themeforest.net",
    "http://homestead.com",
    "http://google.ca",
    "http://cnet.com",
    "http://und.de",
    "http://deviantart.com",
    "http://scribd.com",
    "http://jiathis.com",
    "http://domainname.de",
    "http://ca.gov",
    "http://shopify.com",
    "http://plesk.com",
    "http://wiley.com",
    "http://who.int",
    "http://un.org",
    "http://buzzfeed.com",
    "http://theatlantic.com",
    "http://barnesandnoble.com",
    "http://sakura.ne.jp.jp",
    "http://pbs.org",
    "http://nationalgeographic.com",
    "http://getpocket.com",
    "http://blogspot.com.es.es",
    "http://nature.com",
    "http://networksolutions.com",
    "http://webmd.com",
    "http://foxnews.com",
    "http://cbsnews.com",
    "http://techcrunch.com",
    "http://booking.com",
    "http://php.net",
    "http://berkeley.edu",
    "http://cloudfront.net",
    "http://sciencedirect.com",
    "http://ibm.com",
    "http://a.net",
    "http://nbcnews.com",
    "http://skype.com",
    "http://mashable.com",
    "http://cornell.edu",
    "http://naver.com",
    "http://domainretailing.com",
    "http://usda.gov",
    "http://wp.me",
    "http://springer.com",
    "http://whitehouse.gov",
    "http://squarespace.com",
    "http://phoca.cz",
    "http://change.org",
    "http://cbc.ca",
    "http://ft.com",
    "http://epa.gov",
    "http://secureserver.net",
    "http://enable-javascript.com.com",
    "http://meetup.com",
    "http://noaa.gov",
    "http://cnbc.com",
    "http://nps.gov",
    "http://phpbb.com",
    "http://wikia.com",
    "http://usnews.com",
    "http://google.nl",
    "http://myshopify.com",
    "http://mapquest.com",
    "http://trustpilot.com",
    "http://domainactive.co",
    "http://uol.com.br.br",
    "http://foursquare.com",
    "http://ow.ly",
    "http://google.com.br.br",
    "http://telegram.me",
    "http://sohu.com",
    "http://loc.gov",
    "http://economist.com",
    "http://fda.gov",
    "http://irs.gov",
    "http://themegrill.com",
    "http://wufoo.com",
    "http://geocities.jp",
    "http://bigcartel.com",
    "http://livedoor.jp",
    "http://chicagotribune.com",
    "http://dribbble.com",
    "http://hp.com",
    "http://doi.org",
    "http://prnewswire.com",
    "http://ed.gov",
    "http://ok.ru",
    "http://newyorker.com",
    "http://abc.net.au.au",
    "http://bizjournals.com",
    "http://slate.com",
    "http://houzz.com",
    "http://umblr.com",
    "http://fb.com",
    "http://vice.com",
    "http://xinhuanet.com",
    "http://engadget.com",
    "http://nifty.com",
    "http://t.me",
    "http://marriott.com",
    "http://clickbank.net",
    "http://globo.com",
    "http://list-manage.com.com",
    "http://histats.com",
    "http://state.gov",
    "http://cbslocal.com",
    "http://unesco.org",
    "http://google.com.au.au",
    "http://umich.edu",
    "http://hostnet.nl",
    "http://google.pl",
    "http://house.gov",
    "http://youku.com",
    "http://theverge.com",
    "http://ocn.ne.jp.jp",
    "http://storify.com",
    "http://sogou.com",
    "http://goo.ne.jp.jp",
    "http://fortune.com",
    "http://wunderground.com",
    "http://aboutcookies.org",
    "http://rs.net",
    "http://columbia.edu",
    "http://namejet.com",
    "http://gofundme.com",
    "http://oracle.com",
    "http://yale.edu",
    "http://psychologytoday.com",
    "http://ifeng.com",
    "http://washington.edu",
    "http://indiatimes.com",
    "http://samsung.com",
    "http://upenn.edu",
    "http://athemes.com",
    "http://and.com",
    "http://studiopress.com",
    "http://hilton.com",
    "http://debian.org",
    "http://wikihow.com",
    "http://fbcdn.net",
    "http://fb.me",
    "http://senate.gov",
    "http://fastcompany.com",
    "http://mailchimp.com",
    "http://alibaba.com",
    "http://youronlinechoices.com",
    "http://android.com",
    "http://researchgate.net",
    "http://ustream.tv",
    "http://dedecms.com",
    "http://zdnet.com",
    "http://home.pl",
    "http://exblog.jp",
    "http://cryoutcreations.eu",
    "http://entrepreneur.com",
    "http://drupal.org",
    "http://sagepub.com",
    "http://tripadvisor.co.uk.uk",
    "http://businesswire.com",
    "http://shinystat.com",
    "http://umn.edu",
    "http://jugem.jp",
    "http://hbr.org",
    "http://sciencemag.org",
    "http://ftc.gov",
    "http://google.co.in.in",
    "http://wisc.edu",
    "http://ucla.edu",
    "http://inc.com",
    "http://psu.edu",
    "http://loopia.se",
    "http://visma.com",
    "http://dreamhost.com",
    "http://mijndomein.nl",
    "http://loopia.com",
    "http://ox.ac.uk.uk",
    "http://scientificamerican.com",
    "http://utexas.edu",
    "http://stackoverflow.com",
    "http://and.fr",
    "http://sedo.com",
    "http://mozilla.com",
    "http://worldbank.org",
    "http://hubspot.com",
    "http://census.gov",
    "http://arstechnica.com",
    "http://mysql.com",
    "http://si.edu",
    "http://allaboutcookies.org",
    "http://usgs.gov",
    "http://intel.com",
    "http://amazon.fr",
    "http://shop-pro.jp.jp",
    "http://tandfonline.com",
    "http://aliyun.com",
    "http://office.com",
    "http://alexa.com",
    "http://zendesk.com",
    "http://nhk.or.jp.jp",
    "http://colorlib.com",
    "http://accuweather.com",
    "http://cisco.com",
    "http://google.ru",
    "http://cam.ac.uk.uk",
    "http://hibu.com",
    "http://hollywoodreporter.com",
    "http://admin.ch",
    "http://example.com",
    "http://hhs.gov",
    "http://twitch.tv",
    "http://networkadvertising.org",
    "http://nyu.edu",
    "http://teamviewer.com",
    "http://nazwa.pl",
    "http://variety.com",
    "http://netflix.com",
    "http://box.com",
    "http://prestashop.com",
    "http://bls.gov",
    "http://bmj.com",
    "http://uchicago.edu",
    "http://wsimg.com",
    "http://nhs.uk.uk",
    "http://eventbrite.co.uk.uk",
    "http://opensource.org",
    "http://zenfolio.com",
    "http://blogspot.jp",
    "http://usc.edu",
    "http://va.gov",
    "http://cmu.edu",
    "http://oecd.org",
    "http://ieee.org",
    "http://mlb.com",
    "http://ename.com.cn.cn",
    "http://usa.gov",
    "http://steampowered.com",
    "http://google.ch",
    "http://redcross.org",
    "http://bund.de",
    "http://thehill.com",
    "http://dictionary.com",
    "http://hostgator.com",
    "http://icann.org",
    "http://dot.gov",
    "http://adweek.com",
    "http://fao.org",
    "http://sun.com",
    "http://iubenda.com",
    "http://gesetze-im-internet.de-internet.de",
    "http://tmall.com",
    "http://today.com",
    "http://nginx.org",
    "http://xiti.com",
    "http://venturebeat.com",
    "http://snapchat.com",
    "http://ietf.org",
    "http://symantec.com",
    "http://mhlw.go.jp.jp",
    "http://duke.edu",
    "http://japanpost.jp",
    "http://giphy.com",
    "http://netscape.com",
    "http://justgiving.com",
    "http://sec.gov",
    "http://illinois.edu",
    "http://att.com",
    "http://squareup.com",
    "http://aboutads.info",
    "http://gpo.gov",
    "http://tucowsdomains.com",
    "http://domainnameshop.com",
    "http://plos.org",
    "http://elsevier.com",
    "http://biomedcentral.com",
    "http://reference.com",
    "http://oup.com",
    "http://ssa.gov",
    "http://libsyn.com",
    "http://windowsphone.com",
    "http://ny.gov",
    "http://bigcommerce.com",
    "http://oreilly.com",
    "http://domeneshop.no",
    "http://googleapis.com",
    "http://artisteer.com",
    "http://arxiv.org",
    "http://thenextweb.com",
    "http://google.be",
    "http://gotowebinar.com",
    "http://deloitte.com",
    "http://blackberry.com",
    "http://wschools.com",
    "http://dol.gov",
    "http://python.org",
    "http://siteorigin.com",
    "http://ewebdevelopment.com",
    "http://moz.com",
    "http://warnerbros.com",
    "http://justice.gov",
    "http://quantcast.com",
    "http://dhs.gov",
    "http://java.com",
    "http://fcc.gov",
    "http://congress.gov",
    "http://g.co",
    "http://playstation.com",
    "http://iso.org",
    "http://opencart.com",
    "http://eff.org",
    "http://ucl.ac.uk.uk",
    "http://moodle.org",
    "http://web.de",
    "http://unsplash.com",
    "http://msdn.com",
    "http://nist.gov",
    "http://unicef.org",
    "http://mlit.go.jp.jp",
    "http://canada.ca",
    "http://bitbucket.org",
    "http://azurewebsites.net",
    "http://nginx.com",
    "http://dmca.com",
    "http://etracker.de",
    "http://mynavi.jp",
    "http://aarp.org",
    "http://gartner.com",
    "http://starwoodhotels.com",
    "http://typeform.com",
    "http://acm.org",
    "http://sedoparking.com",
    "http://ticketmaster.com",
]

output = Queue()

meta_data = list()

def process_links(links, output):
    print("[PID: {}] Started processing links ...".format(os.getpid()))

    for link in links:
        print("PID[{}]: Scraping meta for {} ...".format(os.getpid(), link))

        try:
            resp = rq.get(link, timeout=5)

            if resp.status_code != 200:
                continue

            bsp = BeautifulSoup(resp.text, "html.parser")

            title = ""

            # title
            found = bsp.find("title")

            if found is not None:
                contents = found.contents
                if len(contents) > 0:
                    title = contents[0]

            output.put({"link": link, "title": title})
            
        except Exception as e:
            print("[PID: {}] Exception for link ({}): {}".format(os.getpid(), link, e))

    print("[PID: {}] DONEEEEEEEEEEEEEEEEE !!!!!!!!!!!!!!!!!!!!!!!!".format(os.getpid()))

processes = []

start_index = 0

NO_PROCS = 8
LINKS_SEGMENT_COUNT = len(links) // NO_PROCS

for i in range(NO_PROCS):
    proc_links = links[start_index:start_index+LINKS_SEGMENT_COUNT]
    p = Process(target=process_links, args=(proc_links, output))
    processes.append(p)
    start_index += LINKS_SEGMENT_COUNT

for p in processes:
    p.start()

while True:
    running = any(p.is_alive() for p in processes)

    if not output.empty():
        data = output.get()
        print("MAIN DEQUEUE: {}".format(data))
        meta_data.append(data)

    if not running:
        break

pf = open("output2.json", "w")
pf.write(json.dumps(meta_data))
pf.close()
