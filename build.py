# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""
from cryptography import x509

from tools.core import Configuration
from ca.core import CertificateAuthority
from server.core import Server
import print_pems as ppems  #a été ajouté pour l'impression

RESOURCES_DIR = "resources/"
CA_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "ca-private-key.pem"
CA_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "ca-public-key.pem"
SERVER_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "server-private-key.pem"
SERVER_CSR_FILENAME = RESOURCES_DIR + "server-csr.pem"
SERVER_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "server-public-key.pem"
CA_PASSWORD = "mot_#de_passe_152_"
SERVER_PASSWORD = "mot_#de_passe_152_"

CA_CONFIGURATION = Configuration("FR", "Territoire de Belfort", "Belfort", "Illouz_Laurent_Simon_CA", "localhost")
SERVER_CONFIGURATION = Configuration("FR", "Territoire de Belfort", "Belfort", "Illouz_Laurent_Simon_SER", "localhost")

# Création de l'autorité de certification
certificate_authority = CertificateAuthority(CA_CONFIGURATION, CA_PASSWORD, CA_PRIVATE_KEY_FILENAME, CA_PUBLIC_KEY_FILENAME)
    # regardez en haut et ca/core.py


# Création du server
server =Server(SERVER_CONFIGURATION, SERVER_PASSWORD, SERVER_PRIVATE_KEY_FILENAME, SERVER_CSR_FILENAME)
    # regardez en haut et server/core.py

# Signature du certificat par l'autorité de certification
signed_certificate = certificate_authority.sign(server._csr, SERVER_PUBLIC_KEY_FILENAME)

#impression des certificats à compléter regardez #print_pems

print("CA public key :")
ppems.print_perms(CA_PUBLIC_KEY_FILENAME)
ppems.print_Server_public_key()



print("finished ...")
