# Wie wir uns Geschwindigkeitsstatistiken a la Cloudflare als CSV besorgen

Dieses Repo beinhaltet ein Python-Skript, as zusammen mit speed-cloudflare-cli und cron csv-Dateien schreibt, um die Geschwindigkeit eines Internetzugangs zu monitoren. Das ganze ist eventuell nützlich, um dem eigenen ISP aufs Dach zu steigen, weil der nicht die Bandbreite liefert, die im Vertrag vereinbart wurde.

## Was wir brauchen

- Linux (vermutlich gehen auch Unix-artige Systeme und WSL, hab ich aber nicht probiert)
- python 3
- cron
- node / npm

## Wie wir was bekommen

1. das Repo hier klonen.
2. npm install --global speed-cloudflare-cli
3. mit `$ which speed-cloudflare-cli` schauen, wo das Skript ist
4. gegebenenfalls den Pfad zum Script in cloudflare-csv-helper.py als CLOUDFLARE_CLI_PATH anpassen.
5 csv-header schreiben: `python3 cloudflare_csv_helper.py header > ~/cloudflare.csv`
6. cronjob einrichten: `5-59/15 * * * * cloudflare_csv_helper.py >> ~/cloudflare.csv` in `crontab -e` vermerken
7. das gibt alle Viertelstunde, startend um 5 nach voll, einen Test, der dann in die CSV wandert.

> Wer andere Zeitsettings braucht, https://crontab.guru/#5-59/15_*_*_*_* hat euren Rücken.

## Noch was

Inspiriert ist das hier von https://github.com/HenrikBengtsson/speedtest-cli-extras. Dadurch kommen auch die start und stop Spalten in der Ausgabe zustande, die nicht aus speed-cloudflare-cli selbst stammen.

Wieso ist das hier nicht bash? Weil ich das nicht kann.

## Uffbasse!

- Messungen am besten (in der Netzwerktopologie) nahe am oder sogar im Router durchführen
- Messungen am besten mit einer Kabelverbindung (wie in LAN-Kabel) durchführen
- Messungen am besten mit einem Gerät durchführen, das mehr Bandbreite als der Internetzugang kann
- Der Spaß hier funktioniert für mich auf meinem RaspberryPi mit Raspian. Andere Geräte habe ich nicht getestet.

# How to: statistics on your internet connection speed. Automated. In CSV.

Let's use some python and speed-cloudflare-cli together with cron to create csv-data on broadband connection speed over time. May come in handy if you want to get into a fight with your ISP.

## What you need:

- Linux (most likely Unix, macOS or windows with WSL are fine - but untested)
- python 3
- cron
- node / npm

## Wie wir was bekommen

1. clone this repo
2. npm install --global speed-cloudflare-cli
3. find path to speed-cloudflare-cli `$ which speed-cloudflare-cli`
4. check in cloudflare-csv-helper.py if CLOUDFLARE_CLI_PATH is correct for you.
5 write csv-header (adjust paths as needed): `python3 cloudflare_csv_helper.py header > ~/cloudflare.csv`
6. setup cronjob (I recommend absolute paths here.) : Add `5-59/15 * * * * cloudflare_csv_helper.py >> ~/cloudflare.csv` in `crontab -e`
7. Now you should get a new line in the csv every 15 minutes, starting at 5. (see https://crontab.guru/#5-59/15_*_*_*_* for reference if you need something else)


## Here be dragons!

- Try measuring as near to the router/moden as possible
- Best results measuring with a wired connection
- Have enough bandwidth on the measuring device (e.g. don't expect good results measuering a 400 / 25 VDSL2 connection via Fast Ethernet)
- I put this together on Raspian. It may or may not work on other devices.
