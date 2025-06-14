import os
from rembg import remove
from PIL import Image
from io import BytesIO

# Bước 1: Lấy danh sách các ảnh trong thư mục hiện hành
current_dir = os.getcwd()
saved_dir = os.path.join(current_dir, "Saved")
os.makedirs(saved_dir, exist_ok=True)

# Lọc các file jpg và png
image_files = [f for f in os.listdir(current_dir)
               if f.lower().endswith(('.png', '.jpg', '.jpeg')) and os.path.isfile(os.path.join(current_dir, f))]

total = len(image_files)
if total == 0:
    print("Không tìm thấy ảnh trong thư mục hiện tại.")
else:
    for index, filename in enumerate(image_files):
        input_path = os.path.join(current_dir, filename)
        output_path = os.path.join(saved_dir, filename)

        if os.path.exists(output_path):
            print(f"Bỏ qua {filename} (đã tồn tại trong 'Saved').")
            continue

        try:
            with open(input_path, 'rb') as input_file:
                input_data = input_file.read()
                output_data = remove(input_data)

            # Chuyển byte output thành ảnh để lưu
            image = Image.open(BytesIO(output_data)).convert("RGBA")
            image.save(output_path)

            percent = round((index + 1) / total * 100)
            print(f"[{percent}%] - Đã xử lý: {filename}")

        except Exception as e:
            print(f"Lỗi với {filename}: {e}")
