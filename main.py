import os
from PIL import Image

def convert_webp_to_png(input_dir="input_images", output_dir="output_images"):
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
    
    if not files:
        print(f"Không tìm thấy file nào trong thư mục '{input_dir}'.")
        return

    success_count = 0
    for filename in files:
        if filename.lower().endswith(".webp"):
            input_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(output_dir, output_filename)

            try:
                with Image.open(input_path) as img:
                    img.load() 
                    img.save(output_path, format="PNG")
                print(f"Thành công: {filename} -> {output_filename}")
                success_count += 1
            except Exception as e:
                print(f"Lỗi khi chuyển đổi {filename}: {e}")

    print(f"\nĐã hoàn tất chuyển đổi {success_count} file.")

if __name__ == "__main__":
    convert_webp_to_png()
