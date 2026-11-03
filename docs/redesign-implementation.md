# CarbonCap — approved design implementation

Reference: `design/concepts/v2/01-discover.png` through `04-portfolio.png`. User approved these images and requested removal of prototype/demo wording. Keep the four separate task-focused views and all original data and local persistence. HTML stays self-contained and offline.

## Design system

- Background: pure white #ffffff. Forest ink #075335; secondary text #818b88; green primary #238454; pale green #e7f4e6; sky panel #e1efff; fine border #d6e4de.
- Buttons: forest green, subtle lighter bottom-right shading as in the concept, white text, capsule radius 999px, 52–58px tall; outline and pale green secondary variants. Press scale .98, restrained hover elevation.
- Cards: white, radius 28–32px, soft diffuse shadow 0 8px 24px rgba(23,65,45,.10). Images inset 14px, radius 22–24px, no tint. Light blue only in summary/follow panels.
- Embed Noto Sans Thai variable font from `design/assets/fonts/NotoSansThai.ttf`. Keep OFL.txt in private repo. Body 18–20px, line-height 1.55; desktop page title 54–64px/1.18 weight 750; card title 26–30px/1.35 weight 700; main values 36–44px; chrome 17–19px; attribution 13–14px.
- Container width ~1440px, 4%/56px horizontal padding at 1513px. Header 80px with brand left and two capsule nav items right. Hero row about 260px, text left and illustration right. Avoid dense statistics and extra frames.
- Project selection: separate hero; heading/filter row; 3 equal image cards, 24px gaps. Each card has 16px inset image, name, province/status row, credits/price row, full-width CTA. Pending uses blue status and follow hint.
- Project detail: back control, title/province/crop/area and status, compact farm art right; full-width pill tabbar. Satellite tab shows wide image rounded/shadow, floating RGB/NDVI/carbon controls and metadata; AI tab shows estimate/status/evidence, not an extra dashboard. Bottom availability/price and primary CTA. Use the actual GEE images and manifest dates.
- Purchase: back control, title and compact farmer art; two-step progress; left white project/quantity panel, right sky summary panel. Minus/input/plus form a soft green pill. Show integer quantity and live total. Review must precede final recording. Keep a cancel path.
- Portfolio: title left, total credits and paid amount in open whitespace, small globe right. Holding image rows left; pale blue followed-project panel right; transaction table below. Reset and explore actions at bottom. Empty state uses same visual system.
- Mobile <=760px: 20px gutters, header/navigation fit, h1 32–36px, compact illustration, cards/purchase/portfolio stack, controls wrap, map remains readable, minimum 44px touch targets, no horizontal overflow. Transactions become readable stacked rows. Respect reduced motion.
- Icons: consistent 2px rounded SVG strokes, 20–24px; leaf is filled green, arrows outlined. No emoji substitutes.

## Approved copy changes from concepts

Nav: สำรวจโครงการ / พอร์ตของฉัน. Discover: สำรวจโครงการเกษตร / เลือกโครงการ แล้วดูภาพดาวเทียมและข้อมูลคาร์บอน / เลือกโครงการของคุณ / ค้นหาโครงการ / ทั้งหมด / ดูโครงการ. Status: พร้อมซื้อ / กำลังประเมิน. Remove words ทดลอง, จำลอง, ต้นแบบ, prototype and demo from visible app copy; internal storage key is unchanged.

Detail tabs: ภาพดาวเทียม / ประเมินคาร์บอน. Layers: RGB / NDVI / คาร์บอน. CTA ซื้อคาร์บอนเครดิต; pending ติดตามโครงการ. AI action ประเมินคาร์บอน. Keep concise factual method text in evidence area: NDVI ไม่ได้วัดคาร์บอนโดยตรง; ผลประเมินต้องผ่านการตรวจรับรองก่อนออกเครดิต. Do not imply live model execution or real issuance.

Purchase: ซื้อคาร์บอนเครดิต / เลือกจำนวน แล้วตรวจทานรายการ / เลือกจำนวน / ตรวจทาน / สรุปรายการ / รวมมูลค่า / ตรวจทานรายการ / บันทึกเข้าพอร์ต / ยกเลิก. Show a concise factual payment line at review: ระบบยังไม่รับชำระเงิน · รายการที่บันทึกไม่ใช่ใบรับรองเครดิต. Success: บันทึกเข้าพอร์ตแล้ว / ดูพอร์ตของฉัน. No payment processor or actual certification is introduced.

Portfolio: พอร์ตของฉัน / เครดิตในพอร์ต / มูลค่าที่บันทึก / การถือครอง / โครงการที่ติดตาม / ประวัติรายการ / ล้างข้อมูลพอร์ต / สำรวจโครงการ. Footer: ข้อมูลบันทึกในเบราว์เซอร์ของคุณ. Never say payment is completed or offsets retired. Avoid long global disclaimers and repeated notices.

## Assets and immutable data

- Standalone imagegen assets: `design/assets/farmer.png`, `farm.png`, `globe.png`, transparent outside their silhouettes. Use these in page headers; no CSS illustration reconstruction.
- GEE sources: `.build-inputs/gee/manifest.json`, six original RGB/NDVI PNGs, preserved byte-for-byte. Project image cards use original RGB data, never generated concept map crops.
- Keep project IDs, areas, prices, availability limits, carbon estimate ranges and analysis cancellation behavior.
- Local storage remains `carboncap.demo.v1`, `{v:1,purchases:[{id,qty,unitPrice,at,ref}],following:[id]}`. Existing records must load without loss.
- Carbon estimates and local order records retain existing behavior. Only naming and organization change; no claims of live external services.

## Acceptance

Open -> project selection only -> choose project -> satellite/AI tabs -> quantity/review -> record -> portfolio. Search/filter/reset, RGB/NDVI/carbon layers, asynchronous estimate, pending follow/unfollow, integer/max quantity checks, double-confirm guard, reload persistence, cancelled reviews, reset confirmation and reduced-motion all work. GEE photos/date/NDVI attribution remain. Build passes existing static checks, contains no external runtime resources, all image/font data embedded. Compare all four views with approved images and verify mobile overflow and controls before publish.
