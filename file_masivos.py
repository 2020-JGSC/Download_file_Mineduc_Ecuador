import os

import requests

from time import time

from multiprocessing.pool import ThreadPool

def url_response(url):

    path, url = url

    r = requests.get(url, stream = True)

    with open(path, 'wb') as f:

        for ch in r:

            f.write(ch)

urls = [
#("Texto para estudiantes 1 EGB", "http://educacion.gob.ec/wp-content/plugins/download-monitor/download.php?id=2450&force=1"),
#("Comprensión y expresión oral y escrita 1 EGB", "http://www.educacion.gob.ec/wp-content/uploads/downloads/2016/09/CUADERNO_1.pdf"),
#("Relaciones lógico matemáticas 1 EGB", "http://www.educacion.gob.ec/wp-content/uploads/downloads/2016/09/CUADERNO_2.pdf"),
#("Descubrimiento y comprensión del Medio Natural y Cultural – Identidad Y Autonomía – Convivencia 1 EGB", "http://www.educacion.gob.ec/wp-content/uploads/downloads/2016/09/CUADERNO_3.pdf")


#("Libro Matemáticas 2 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1tLPYb7TUdwXNZRjO7iKmQDC93Q-CS56P"),
#("Libro Lengua y literatura 2 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1VzltlcI0v41YX-IdMxydKp7rDfFwD1-e"),
#("Libro Ciencias Sociales 2 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1L4G4PrvMclhULJ6k8bES9xnb3YfH7eOx"),
#("Libro Ciencias Naturales 2 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1QvIpU1sZ6aTaCRuiMMtg7oEy3-XI2DmF"),
#("Libro Entorno Natural y Social 2 EGB", "http://educacion.gob.ec/wp-content/plugins/download-monitor/download.php?id=2449&force=1"),
#("Libro Inglés 2 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=17WgIr3wAgf7GNB9i7-d_G636Dj5DGEOT")


#("Libro Matemática 3 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1xe6Box3Ke78XEiS4drUtoxz5Jy5hjqSs"),
#("Libro Lengua y literatura 3 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1fB3fNzDG7hjuC4wz-pifjI_qYxH8Nw0Q"),
#("Libro Ciencias Naturales 3 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1xsmr2g9ojEDLmrotEbMngoMfhzQjvHs3"),
#("Libro Ciencias Sociales 3 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=105CPMK9ccEmXWwZPVKB7OJLSBqFxyfeO"),
#("Libro Entorno Natural y Social 3 EGB", "http://educacion.gob.ec/wp-content/plugins/download-monitor/download.php?id=2446&force=1"),
#("Libro Inglés 3 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1_pA6TMacteVA2IeoBei194PTJj9RTawq"),


#("Libro Ciencias Sociales 4 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=16z7vRZMO-OF0dk8wZtSBBvj0WgoEJC4J"),
#("Libro Ciencias Naturales 4 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1po5W7E3EfQoZlL0U5cMDtFmdlF1yWDho"),
#("Libro Matemáticas 4 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1po5W7E3EfQoZlL0U5cMDtFmdlF1yWDho"),
#("Libro Inglés 4 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1coSplIZqtaVrBSSV3GLturWkrU3ZO_m7"),
#("Libro Lengua y Literatura 4 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=15qd0l_qd9ya4KRmo5Mz-6XDmf07vD01e"),


#("Libro Ciencias Naturales 5 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1-1EmBxR1CmaS2otdCJt_B5y2TzKiEQfc"),
#("Libro Ciencias Sociales 5 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=15I9GBebVef3O2Z30CENlKAEkIM1c8GXI"),
#("Libro Matemáticas 5 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1VJQ16_PxUBRJe37t4xZuCQh6Ull5okY-"),
#("Libro Inglés 5 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1coSplIZqtaVrBSSV3GLturWkrU3ZO_m7"),
#("Libro Lengua y Literatura 5 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1JY6bP72_p6w7pLd0sYmLnfI2JnTlH4Zg"),


#("Libro Ciencias Sociales 6 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1JzkSAa7zBuOWZeqfFBPVirFIWj45idbH"),
#("Libro Matemáticas 6 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1UDOnsxwDx7bzAReZEqES2gXD5GCozvqy"),
#("Libro Lengua y Literatura 6 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1a-9qLahJ9aaL6fhngyyVumMWbVzjFxJJ"),
#("Libro Ciencias Naturales 6 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1QrS7NFV0ij3JflT2SK27ABOxXNPrmifW"),
#("Libro Inglés 6 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1coSplIZqtaVrBSSV3GLturWkrU3ZO_m7"),

#("Libro Ciencias Sociales 7 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1h5zViK-NiQkMu23NvzRRCigm1g14uJG9"),
#("Libro Matemáticas 7 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1li7xcr1lBicWl87pNsUWr74jKn71NujW"),
#("Libro Lengua y Literatura 7 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1B1nSJH2GoHmhjcCtx1-8aXpb106xtUpE"),
#("Libro Ciencias Naturales 7 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1oyWFupsi-WiEbV9agL9JOzyhlwjWgsOY")


#("Libro Ciencias Sociales 8 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1wOGkJcjoogdqTabsEP8lgZy-z8EUZbXd"),
#("Libro Ciencias Naturales 8 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1_JPSYDafotend3F9oYG2o4VOFNgxGBOj"),
#("Libro Matemática 8 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1hlOWAnI7nAHquAdkfhIpebRhYCdqStQB"),
#("Libro Lengua y Literatura 8 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1nhIpwEf7j3M8fb8JjAlSs7niR_6OLFsz"),
#("Libro Inglés 8 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1cTN-OmtqiedlHU0jDh6Z9n0HFp9qhg6j"),


#("Libro Ciencias Sociales 9 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1keQExvg6K4-k2l2ccPg7DAnMPSX05piq"),
#("Libro Ciencias Naturales 9 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1yoV7tIOntwzSzkArokTuFmCmHaDLv471"),
#("Libro Matemática 9 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1C8zUo63aQ0xAX-DM9byjFy92ZUZJAKE0"),
#("Libro Lengua y Literatura 9 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1CdLqiPx_KygK7-l8QX82-GLcdnB8z_XC"),
#("Libro Inglés 9 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1Cu_uHy9JS4iuU8tVifZs5iGrY2u_4lvU"),


#("Libro Ciencias Sociales 9 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1keQExvg6K4-k2l2ccPg7DAnMPSX05piq"),
#("Libro Ciencias Naturales 9 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1yoV7tIOntwzSzkArokTuFmCmHaDLv471"),
#("Libro Matemática 9 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1C8zUo63aQ0xAX-DM9byjFy92ZUZJAKE0"),
#("Libro Lengua y Literatura 9 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1CdLqiPx_KygK7-l8QX82-GLcdnB8z_XC"),
#("Libro Inglés 9 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1Cu_uHy9JS4iuU8tVifZs5iGrY2u_4lvU"),


#("Libro Ciencias Sociales 10 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1AFiUpmvYRUDlvcuKk1jRccjNiKSTP2nU"),
#("Libro Ciencias Naturales 10 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=19oyUYb1_jvEdURdYMZthCbFZ-rqK-YvB"),
#("Libro Matemática 10 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1BhLQ5NsZAUJ3_XPVm1uaGNopMBHln0dC"),
#("Libro Lengua y Literatura 10 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1ThClX4jaf2vPPe_f7ouQPupEeqa5hv8I"),
#("Libro Inglés 10 EGB", "http://drive.google.com/uc?export=download&confirm=no_antivirus&id=1VIvzn4rNML8dsEiurm3CyFEVMeuTkEzj"),


#("Emprendimiento y gestión 1 BGU", "https://drive.google.com/uc?id=0B-JyZ7WJiu5tU0J1RURQMUlIUlk&export=download"),
#("Matemáticas 1 BGU", "https://drive.google.com/uc?id=188RK5R00ifvBAtm2vIbwgWBNOV9Tzupf&export=download"),
#("Educación para la ciudadanía 1 BGU", "https://drive.google.com/uc?id=1XIQO2MWHGFP4_FhSC7DcHCKl-VAemhAI&export=download"),
#("Biología 1 BGU", "http://drive.google.com/uc?id=1pfWrFBj9EkHQVBVmIT1M-MdPyNCMfhIG&export=download"),
#("Química 1 BGU", "http://drive.google.com/uc?id=1a3texhQkOH0Rw4vaj3rQ69g41G9utKo6&export=download"),
#("Historia 1 BGU", "http://drive.google.com/uc?id=1i1wOGmxjPi3zzdtP32BuhfBWaXX_k3_k&export=download"),
#("Filosofía 1 BGU", "http://drive.google.com/uc?id=1dNRdx0i3VGu4qj4T4MJ1azDWkDgGDMJ5&export=download"),
#("Física 1 BGU", "http://drive.google.com/uc?id=1JxJx9EbvdMc3XYginmvZAxtCroxCfHUW&export=download"),
#("Lengua y literatura 1 BGU", "http://drive.google.com/uc?id=1DbNRb_JpegpG1CFEtwKrYikrLs1V1sJo&export=download"),
#("Ingles Student Book A2.2 1 BGU", "http://drive.google.com/uc?id=19TlYl2ifD_UBo5pvx2_xA86mAf6iOKc2&export=download"),



("Emprendimiento y gestión 2 BGU", "http://drive.google.com/uc?id=0Bz_4VE_C8UYmX1RoUmgyTHFDTFE&export=download"),
("Matemáticas 2 BGU", "http://drive.google.com/uc?id=17VcEof3X_KN9Ug__VshUoUFKXUguq7ZV&export=download"),
("Educación para la ciudadanía 2 BGU", "http://drive.google.com/uc?id=1xo6d3JDHzx7h3Y2u5hJ0Yf2XjTRBxGM4&export=download"),
("Biología 2 BGU", "http://drive.google.com/uc?id=1I57uBs7eIenxKVquMZKHJa4AUmYHVRCd&export=download"),
("Química 2 BGU", "http://drive.google.com/uc?id=1TZhnGLJCeDMI7GTmLCoYvwxWQ1t-jKwB&export=download"),
("Historia 2 BGU", "http://drive.google.com/uc?id=102FKYFbRoeDpMXHxFBuY7SCEXrE9aqE4&export=download"),
("Filosofía 2 BGU", "http://drive.google.com/uc?id=1HuYIXSug3izFuq0GOb477CncLg-25jjB&export=download"),
("Física 2 BGU", "http://drive.google.com/uc?id=1xkft9NgitVVqqewe44ACh62_sfi54gji&export=download"),
("Lengua y literatura 2 BGU", "http://drive.google.com/uc?id=1NdBlCdLG8V6HnoyGGM50IiNfUnAJKWer&export=download"),
("Ingles Student Book B1.1 2 BGU", "http://drive.google.com/uc?id=179thV1N6ZUCagpXB3v7tX1azNb0ChU7P&export=download"),



("Sociología 3 BGU", "http://drive.google.com/uc?id=0Bz_4VE_C8UYmUzBpRG5KSU9Tem8&export=download"),
("Matemáticas 3 BGU", "https://drive.google.com/uc?id=1vvlm7IaA1Wmn5vd_HyCt7A__HC2uXsI4&export=download"),
("Educación para la ciudadanía 2 BGU", "http://drive.google.com/uc?id=1xo6d3JDHzx7h3Y2u5hJ0Yf2XjTRBxGM4&export=download"),
("Biología 3 BGU", "http://drive.google.com/uc?id=1VeeKPoKu0wybliK0jw964EreCSRNdEqB&export=download"),
("Química 3 BGU", "http://drive.google.com/uc?id=1aIDN-ws6ZGwEh6xw2zd6N_D2cZP-29H3&export=download"),
("Historia 3 BGU", "http://drive.google.com/uc?id=1X5f5gvuaxCDQ6k7F7r9ztICmIzq2ysXi&export=download"),
("Lectura crítica 3 BGU", "http://drive.google.com/uc?id=0Bz_4VE_C8UYmcDRwVzE1YkVzb2s&export=download"),
("Física 3 BGU", "http://drive.google.com/uc?id=1Vp4mcagF3gqlTmihetuiJMcwNto1ttEZ&export=download"),
("Lengua y literatura 3 BGU", "http://drive.google.com/uc?id=1bGzY4H1-rtGHCS6GFuk9yNmdzqf9rNF_&export=download"),
("Ingles Student Book B1.2 3 BGU", "http://drive.google.com/uc?id=1g8Mih4WWdqpMUp0jaUP2a05evStaojva&export=download"),
("Mundo contemporáneo 3 BGU", "http://drive.google.com/uc?id=0Bz_4VE_C8UYmQ2ZYZ3JhazVEVWs&export=download")

]

start = time()
for x in urls:

    url_response (x)
ThreadPool(9).imap_unordered(url_response, urls)

print(f"Time to download: {time() - start}")
