# Random Wikipedia Sayfası

Kod, size seçilen makaleinin adını söyler. Eğer o makaleyi açmak isterseniz "e" yaparak o sayfayı açar. Eğer farklı bir makale açılmasını isterseniz "h" derseniz ve farklı bir  makale seçilir.

2 tür kod yazılmıştır:

- Makale ismi wikipedia sayfasından alınmıştır.

- Makale ismi wikipedia sayfasının title'ından alınmıştır.


Örnek Çıktı
-------------

![image](https://user-images.githubusercontent.com/81961593/216441112-81255f82-b9f8-46c4-9efe-c90a5a475358.png)

Try Except Nedeni
-----

Kodda bulunan try except kısmının nedeni, web scrabing yaparken bazen programın wikipdia tarafından engellenmesidir. Bu kod engelleme işlemi olduğunda programın 5 saniye sayfaya istek atmasını engeller. Bu şekilde 5 saniye sonra tekrar sayfaya erişilebilir.

```python
try:
  ...
except AttributeError:
  time.sleep(5)
```

