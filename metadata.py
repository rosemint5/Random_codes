import os
import datetime
import hashlib
import PIL.Image
from PIL.ExifTags import TAGS, GPSTAGS
import filetype
import pandas as pd
rows = []
cols = []
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      file_path = os.path.join(root, name)
      file_stat= os.stat(name)
      c_time = os.path.getctime(name)
      m_time = os.path.getmtime(name)
      checksum_md5 = hashlib.md5(open(name,'rb').read()).hexdigest()
      checksum_sha1 = hashlib.sha1(open(name,'rb').read()).hexdigest()
      kind = filetype.guess(name)
      if kind is None:
         fname, type = os.path.splitext(name)
         typem = None
      else:
         type = kind.extension
         typem = kind.mime
      if 'image' in str(typem):
         exif_table = {}
         gps_info = None
         img = PIL.Image.open(name)
         exif_data = img._getexif()
         if exif_data:
            for tag, value in exif_data.items():
               tags = TAGS.get(tag, tag)
               exif_table[tags] = value
               if tags == 'GPSInfo':
                  gps_info = {}
                  for key in exif_table['GPSInfo'].keys():
                     decode = GPSTAGS.get(key,key)
                     gps_info[decode] = exif_table['GPSInfo'][key]
                  print(gps_info)
         else:
            print('Brak exif')
      else:
         gps_info = None
      print(os.path.join(root, name),
               "Rozmiar pliku w bajtach:", file_stat.st_size,
               'Data utworzenia pliku:', datetime.datetime.fromtimestamp(c_time),
               "Data ostatniego dostępu:", datetime.datetime.fromtimestamp(m_time),
               'Suma kontrolna SHA1:', checksum_sha1,
               'Suma kontrolna MD5:', checksum_md5,
               'Typ pliku:', type)
      rows.append([file_path,file_stat.st_size, datetime.datetime.fromtimestamp(c_time), 
                     datetime.datetime.fromtimestamp(m_time), checksum_md5, checksum_sha1,type, gps_info])

   for name in dirs:
      dir_path = os.path.join(root, name)
      print(os.path.join(root, name),
            "Rozmiar folderu w bajtach:", file_stat.st_size,
               'Data utworzenia folderu:', datetime.datetime.fromtimestamp(c_time),
                 "Data ostatniego folderu:", datetime.datetime.fromtimestamp(m_time))
      rows.append([dir_path, file_stat.st_size, datetime.datetime.fromtimestamp(c_time), 
                     datetime.datetime.fromtimestamp(m_time), None, None, None, None])
      

      

def prezentacja(rows):
   df = pd.DataFrame(rows, columns=['Name', 'Size in bytes', 'Creation Time', 'Last Modified', 
                                 'MD5 Checksum', 'SHA1 Checksum', 'Extension', 'Exif data (Geolocation)'])
   df.to_csv('raport.csv', index=False)

prezentacja(rows)

checksum_md5 = hashlib.md5(open('raport.csv','rb').read()).hexdigest()
checksum_sha1 = hashlib.sha1(open('raport.csv','rb').read()).hexdigest()

f = open("checksums.txt", "w")
f.write('MD5: ')
f.write(checksum_md5)
f.write('\n')
f.write('SHA1: ')
f.write(checksum_sha1)
f.close()