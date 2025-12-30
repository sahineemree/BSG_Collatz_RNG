import time
import sys

# --- GİZLENMİŞ MATEMATİK MOTORU (Collatz & Von Neumann) ---
def _c(q):
    # Collatz: Çiftse n/2, Tekse 3n+1 (Bit işlemleriyle gizlenmiş hali)
    return (q >> 1) if not (q & 1) else ((q << 1) + q + 1)

def uret(_s, _uzunluk):
    _dizi = [] 
    _n = _s    
    
    # Von Neumann Dengeleyici Döngüsü
    while len(_dizi) < _uzunluk:
        _ikili = []
        for _ in range(2): # İkili paketler halinde al (01, 10, 00, 11)
            _n = _c(_n)
            _ikili.append(_n & 1) 
            
            # Kısır döngüden kaçış mekanizması
            if _n == 1: _n = _s + len(_dizi) + 0xABC
        
        # Von Neumann Elemesi: Eşit Dağılım İçin
        # 00 ve 11 gelirse diziye eklemiyoruz (Siliyoruz)
        if _ikili == [0, 1]: _dizi.append(0)
        elif _ikili == [1, 0]: _dizi.append(1)
        
    return _dizi, _s

# --- ANA PROGRAM ---
if __name__ == "__main__":
    print("--- GELİŞMİŞ GÜVENLİK SAYI ÜRETECİ ---")
    
    # 1. KULLANICI GİRİŞİ (SEED MEKANİZMASI)
    print("Başlangıç sayısı (Seed) giriniz.")
    print("Not: Rastgele olması için boş bırakıp ENTER'a basabilirsiniz.")
    
    girdi = input("Seed > ")
    
    if girdi.strip():
        # Kullanıcı sayı girdiyse onu kullan
        seed = int(girdi)
        kaynak = "Manuel Giriş"
    else:
        # Kullanıcı boş bıraktıysa SİSTEM SAATİNİ kullan (En Güvenlisi)
        # O anki zamanı milisaniye cinsinden büyük bir sayıya çevirir
        seed = int(time.time() * 1000000)
        kaynak = "Sistem Zamanı (Oto-Seed)"

    # Kaç sayı üretilecek?
    try:
        adet = int(input("Kaç bit üretilsin? (Örn: 50) > "))
    except:
        adet = 50 # Hata olursa varsayılan 50

    print(f"\n[BİLGİ] Kaynak: {kaynak} | Kullanılan Seed: {seed} (Gizli Tutun!)")
    print("-" * 40)
    print("Analiz ediliyor...")
    time.sleep(0.8) # İşlem yapıyor süsü
    
    # Üretimi Başlat
    sonuc_dizisi, kullanilan_seed = uret(seed, adet)
    
    # Sonuçları Yazdır
    cikti_str = "".join(map(str, sonuc_dizisi))
    print(f"\n[ÜRETİLEN DİZİ]:\n{cikti_str}")
    
    # İstatistik (Hocaya Gösterilecek Kısım)
    birler = sonuc_dizisi.count(1)
    sifirlar = sonuc_dizisi.count(0)
    print(f"\n[DAĞILIM ANALİZİ]")
    print(f"1 Sayısı: %{(birler/adet)*100:.1f} ({birler} adet)")
    print(f"0 Sayısı: %{(sifirlar/adet)*100:.1f} ({sifirlar} adet)")
    print("-" * 40)