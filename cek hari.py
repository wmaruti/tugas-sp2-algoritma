from datetime import date
 
d1 = date(1900, 1, 1)
 
hari = [
  'senin',
  'selasa',
  'rabu',
  'kamis',
  'jum`at',
  'sabtu',
  'minggu'
]
 

def main():
  tgl = input("masukkan tanggal : ")
  bln = input("masukkan bulan : ")
  thn = input("masukkan tahun : ")
  d0 = date(thn,bln,tgl) 
  beda = d0 - d1
  print beda.days
  harike = (beda.days) % 7
  print ""
  print hari[harike]
  pass
 
if __name__ == '__main__':
  main()
