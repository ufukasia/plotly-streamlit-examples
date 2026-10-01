# Plotly Laboratuvarı — Etkileşimli Görselleştirme (Streamlit)

Veri Görselleştirme dersinin 7. haftası için hazırlanmış, Plotly ile etkileşimli grafikleri adım adım gösteren tek sayfalık bir Streamlit uygulaması. Sekmeler sınıfta soldan sağa ilerlenecek şekilde, dosya adı gibi etiketlenmiştir (bu adlarda ayrı dosyalar yoktur; tüm içerik `app.py` içindedir).

## Sekmeler

| Sekme | Konu |
|---|---|
| `01_fark.py` | Statik grafik ile etkileşimli grafik arasındaki fark |
| `02_express.py` | Plotly Express ile hızlı giriş (Gapminder hareketli kabarcık grafiği) |
| `03_mimari.py` | Figür mimarisi: Plotly Express, Graph Objects ve figür ağacı |
| `04_secim.py` | Seçim olayları: kutu/lasso ile seçilen noktaların diğer özetleri güncellemesi |
| `05_zaman.py` | Zaman serisinde hover, range slider ve anotasyon |
| `06_hiyerarsi.py` | Treemap ve sunburst ile hiyerarşik veri |
| `07_dashboard.py` | Grafikten web bileşenine: küçük bir dashboard ve Dash callback mantığına giriş |

Örneklerde Plotly'nin yerleşik `gapminder` ve `iris` veri setleri ile kod içinde üretilen örnek veriler kullanılır.

## Kurulum ve çalıştırma

```bash
pip install -r requirements.txt
streamlit run app.py
```

Windows PowerShell'de uygulamayı 8517 portunda başlatmak için hazır betik:

```powershell
.\run_hafta7_plotly_lab.ps1            # varsayılan port 8517
.\run_hafta7_plotly_lab.ps1 -Port 8600 # farklı port
```

## Dosyalar

| Dosya | Açıklama |
|---|---|
| `app.py` | Uygulama |
| `hafta7_plotly_lab.py` | `app.py` ile aynı içerikte kopya |
| `run_hafta7_plotly_lab.ps1` | PowerShell başlatma betiği |
| `requirements.txt` | Bağımlılıklar: `streamlit`, `plotly`, `pandas`, `numpy` |

## Lisans

GNU General Public License v3.0. Ayrıntılar için [LICENSE](LICENSE) dosyasına bakın.

## İletişim

Dr. Öğr. Üyesi Ufuk Asil, Ostim Teknik Üniversitesi.
