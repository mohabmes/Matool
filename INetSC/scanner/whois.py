import pythonwhois


def get_whois(url, data=None):
    domain = pythonwhois.get_whois(url)

    if data is not None:
        server_data = {
            'id': domain['id'][0],
            'creation_date' : domain['creation_date'][0],
            'expiration_date' : domain['expiration_date'][0],
            'updated_date' : domain['updated_date'][0],
            'registrar' : domain['registrar'],
            'whois_server': domain['whois_server'],
            'nameservers' : domain['nameservers'],
            'emails' : domain['emails'],
            'contacts' : domain['contacts']
        }
        return server_data
    else:
        return domain['raw'][0]
