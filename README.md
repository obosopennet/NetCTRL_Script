# NetCTRL_Script

Dette scriptet henter hostname fra en tall fil og matcher det mot Netbox for å hente IP, deretter sender konfigurasjon til flere type switcher basert på device-type fra Netbox. Konfigurasjonen er fra en jinja2 template.

## Oppsett

Følg disse trinnene for å sette opp og kjøre scriptet:

1. Klon GitHub-repositoriet: `git clone https://github.com/user/repo.git`
2. Gå inn i mappen: `cd repo`
3. Opprett et virtuelt miljø: `python -m venv env`
4. Aktiver virtuelt miljø: `source env/bin/activate`
5. Installer avhengighetene: `python setup.py install`

## Bruk

For å kjøre scriptet, kan du bruke følgende kommando:

```bash
python main.py -h
