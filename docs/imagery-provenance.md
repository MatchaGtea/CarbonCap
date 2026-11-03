# ที่มาของภาพดาวเทียม (Imagery Provenance)

เอกสารนี้อธิบายที่มาและการประมวลผลภาพดาวเทียมที่ใช้ใน CarbonCap ภาพ RGB/NDVI เป็น**ข้อมูลจริง** แต่การแสดงขอบเขตโครงการเป็นเพียงตัวอย่างจำลอง

## แหล่งข้อมูล

- **ชุดข้อมูล:** [COPERNICUS/S2_SR_HARMONIZED](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED) (Sentinel-2 Surface Reflectance, Band Harmonization)
- **ผู้ให้ข้อมูล:** European Union / ESA / Copernicus
- **แพลตฟอร์มการประมวลผล:** Google Earth Engine
- **แบนด์ RGB:** B4, B3, B2 — **NIR:** B8 — ความละเอียดต้นทาง 10 เมตร/พิกเซล

## ช่วงเวลาและการกรอง

- ช่วงที่ร้องขอ: `2026-01-01` (รวม) ถึง `2026-04-01` (ไม่รวม)
- Cloud/shadow/snow mask: ไม่รวมคลาส SCL `0, 1, 3, 8, 9, 10, 11`
- จำกัด scene ที่มี `CLOUDY_PIXEL_PERCENTAGE <= 40`
- สร้างคอมโพสิตด้วย **median surface reflectance**
- **NDVI** คำนวณจากคอมโพสิต median: `(B8 - B4) / (B8 + B4)` — เป็นดัชนีพืชพรรณ **ไม่ใช่การวัดคาร์บอน**

## สถิติต่อโครงการ

| โครงการ | จำนวนฉาก | ช่วงวันที่สังเกต | NDVI เฉลี่ย |
| --- | --- | --- | --- |
| แม่ริม (mae-rim) | 57 | 2026-01-03 – 2026-03-29 | 0.4617 |
| ท่าใหม่ (tha-mai) | 58 | 2026-01-02 – 2026-03-31 | 0.5953 |
| ปากช่อง (pak-chong) | 18 | 2026-01-05 – 2026-03-31 | 0.4418 |

แฮชจริง (sha256) ขอบเขต (bounds) จุดศูนย์กลาง และรายการ scene ID ฉบับเต็มอยู่ใน [docs/gee-manifest.json](gee-manifest.json)

## การส่งออก (Export)

- CRS: `EPSG:4326`
- ขนาด: **1024 × 704 พิกเซล** (PNG)
- ภาพส่งออกแล้วอาจถูกปรับขนาดเมื่อแสดงผล (display resampling) — **ไม่ได้เพิ่มความละเอียดการวัด** เมื่อเทียบกับต้นทาง 10 เมตร

## ข้อจำกัดและคำชี้แจง

- ภาพที่ส่งออกมีขอบเขตจำกัด (finite extent) ของพื้นที่ตัวอย่าง
- ขอบเขตโครงการที่แสดงเป็นการจำลองเพื่อการสาธิต **ไม่ได้อ้างกรรมสิทธิ์ที่ดินใด ๆ**
- ภาพอ้างอิงจากข้อมูล Copernicus/ESA จริง แต่เอกสารนี้**ไม่มี** project ID ของ Cloud, ข้อมูลประจำตัว (credentials) หรือการเชื่อมต่อแบบ live กับ Earth Engine
- ดูคู่มือการแสดงผลและวิเคราะห์เพิ่มเติมได้ที่เอกสาร Google: [Earth Engine visualization](https://developers.google.com/earth-engine/guides/image_visualization)
