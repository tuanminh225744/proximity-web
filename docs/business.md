- Là 1 hệ thống giúp tìm những nhà hàng ở trong 1 phạm vi cách người dùng n km.
- Phục vụ mục đích tìm kiếm trong phạm vi

- Yêu cầu chức năng chính:
  - Lọc thông tin nhà hàng theo yêu cầu
  - Tìm kiếm nhà hàng trong phạm
  - Lựa chọn bán kính tìm kiếm
  - Sắp xếp kết quả tìm kiếm
  - Xem thông tin chi tiết của nhà hàng được tìm ra
  - Tạo, sửa, xóa thông tin nhà hàng
  - Xác thực, phân quyền, validate input, chống SQL injection, rate limit, log
  - Chỉ đường đến nhà hàng
  - Hiển thị kết quả trên bản

- Yêu cầu phi chức năng:
  - Hiệu năng (GET /locations/nearby, tải 500 req/s):
  - P95 < 200 ms, P99 < 500 ms
  - Sai số khoảng cách ≤ 1% so với bán kính yêu cầu
  - Thay đổi dữ liệu nhà hàng hiển thị trong kết quả tìm kiếm trong ≤ 60 giây
  - Không lưu vị trí người dùng (DB, log, cache)
  - Quy mô 100k nhà hàng
  - Phạm vi địa lý 100km
  - Phạm vi bán kính 0.5km ~ 10km
  - Độ sẵn sàng 99,5%
  - Giới hạn kết quả trả về 20 kết quả (phân trang)

- Phạm vi chia thành 3 phase:
  - Phase 1: Hoàn thành MPV
    - Tìm nhà hàng trong bán kính
    - Chọn bán kính tìm kiếm
    - Sắp xếp kêt quả
    - Xem chi tiết nhà hàng
    - Hiển thị kết quả trên bản đồ
    - CRUD cho nhà hàng (quyền admin)
    - Chỉ đường (tạo link mở google map)

  - Phase 2:
    - Phân quyền, login
    - Rate limit, log
    - Cache kết quả (60s)
    - Phân trang

  - Phase 3: (nếu rảnh)
    - Load balance
    - Chia microservice tìm kiếm nhà hàng
    - Tạo replica DB phục vụ
