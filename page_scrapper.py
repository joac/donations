from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

import io
from PIL import Image

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36")

driver = webdriver.PhantomJS(desired_capabilities=dcap)
time.sleep(1)
driver.set_window_size(1024, 768)
urls = [
        "http://www.telam.com.ar/notas/201506/110512-a-diez-dias-de-los-comicios-portenos-descubren-filtraciones-de-seguridad-en-el-sistema-de-voto-electronico.html" ,
        "http://www.lanacion.com.ar/1807647-allanaron-la-casa-de-un-programador-que-detecto-fallas-en-el-sistema-de-voto-electronico" ,
        "http://www.clarin.com/policiales/Voto-electronico-allanaron-domicilio-irregularidades_0_1387661308.html" ,
        "http://www.telam.com.ar/notas/201507/111442-allanamiento-voto-electronico.html" ,
        "http://www.pagina12.com.ar/diario/elpais/1-276405-2015-07-05.html" ,
        "http://www.lavaca.org/notas/boleta-electronica-oficialismos-y-empresas-una-formula-ganadora/" ,
        "https://youtu.be/u63SjqgDyYk?t=13m22s" ,
        "http://pillku.org/article/vulnerabilidades-tecnicas-desinformacion-y-allanam/" ,
        "http://radiocut.fm/audiocut/jose-masson-voto-electronico-caba/" ,
        "https://www.eff.org/es/deeplinks/2015/07/buenos-aires-censuro-y-allano-reportaron-falencias-del-voto-electronico" ,
        "https://netzpolitik.org/2015/hinweis-auf-sicherheitsluecke-in-argentinischem-wahlsystem-fuehrt-zu-hausdurchsuchung/" ,
        "http://www.spiegel.de/netzwelt/netzpolitik/razzia-nach-hinweis-auf-sicherheitsluecke-in-wahlcomputern-a-1042657.html" ,
        "http://arstechnica.co.uk/tech-policy/2015/07/police-raid-programmer-who-reported-flaw-in-argentinian-e-voting-system/" ,
        "http://slashdot.org/story/296317" ,
        "http://boingboing.net/2015/07/08/argentine-police-raid-programm.html" ,
        "https://www.techdirt.com/articles/20150707/06204631571/argentina-rewards-programmer-who-exposed-e-voting-vulnerabilities-with-complimentary-home-police-raid.shtml" ,
        "http://www.techworm.net/2015/07/argentinian-programmer-rewarded-with-a-home-raid-for-exposing-e-voting-vulnerabilities.html" ,
        "http://piratetimes.net/illegal-and-insecure-evoting-carried-out-in-argentina/" ,
        "http://opendatacordoba.org/blog/sobre-los-allanamientos-con-motivos-de-las-vulnerabilidades-en-el-sistema-de-voto-electronico/" ,
        "http://www.facttic.org.ar/noticias/sobre-el-voto-electr-nico-en-la-caba" ,
        "http://www.vialibre.org.ar/2015/07/04/allanamiento-al-domicilio-de-quienes-reportaron-fallas-de-seguridad-en-los-sistemas-de-msa/" ,
]

thumb_size = 300, 300

for idx, url in enumerate(urls):
    driver.get(url)
    screen = driver.get_screenshot_as_png()
    print(screen)
    white = Image.new("RGBA", (1024, 768), 'white' )
    im = Image.open(io.BytesIO(screen))
    im = im.crop((0,0, 1024,768))
    im = Image.alpha_composite(white, im)
    im.thumbnail(thumb_size)
    im.save('thumb_%d.png' % idx, "JPEG")
