# Proximity

Ứng dụng mẫu gồm frontend Next.js, backend FastAPI và cơ sở dữ liệu PostgreSQL.

## Công nghệ

- Frontend: Next.js, React, TypeScript
- Backend: FastAPI, SQLAlchemy
- Cơ sở dữ liệu: PostgreSQL 16

## Chạy dự án

Yêu cầu đã cài Docker và Docker Compose.

1. Tạo tệp cấu hình môi trường từ mẫu:

   ```powershell
   Copy-Item .env.example .env
   ```

2. Build các dịch vụ ở thư mục gốc dự án:

   ```bash
   make build
   ```

3. Khởi chạy dự án

   ```bash
   make up
   ```

4. Dừng dự án

   ```bash
   make down
   ```

5. Mở các địa chỉ:
   - Frontend: http://localhost:3000
   - Backend: http://localhost:8000
   - Tài liệu API: http://localhost:8000/docs

## Cấu trúc thư mục

```text
backend/   API FastAPI
frontend/  Giao diện Next.js
```
