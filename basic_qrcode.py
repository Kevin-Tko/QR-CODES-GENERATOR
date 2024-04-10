import segno
from segno import helpers

links = ['https://github.com/Kevin-Tko?tab=repositories',
         'https://www.linkedin.com/in/kevin-njogu-aci-72565087/']
dark = ['darkred', 'purple']
data_light = ['yellow', 'lavender']
images = ['github_qrcode.png', 'linkedin_qrcode.png'] #naming images

for i in range(2):
    qrcode = segno.make(links[i],
                        error='h',#Error correction level
                        mask=7)
    qrcode.save(images[i],
                scale=6, #change size/ scale of the qr code
                border=2, # defining the quiet zone of a qr code
                light='white', # changing the background color of the QR code
                dark= dark[i], # changing the colors of the black modules of the QR code
                data_dark='darkorange',
                data_light= data_light[i]
                )

qrcode1=helpers.make_email(to='kelvnjogu@gmail.com',
                           cc='njogutheanalyst@gmail.com',
                           subject=f'Hi Kevin,\n\nI just scanned your QR code.\n\nIt\'s epic man.')
qrcode1.save('email_sender.png',
            scale=5, #change size/ scale of the qr code
            border=2, # defining the quiet zone of a qr code
            light='white', # changing the background color of the QR code
            dark='lime', # changing the colors of the black modules of the QR code
            data_dark='gold',
            data_light='lavender'
            )
