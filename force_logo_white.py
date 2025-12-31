from PIL import Image
import os

input_path = 'reports/figures/project_logo.png'
output_path = 'reports/figures/logo_final.jpg'

try:
    if os.path.exists(input_path):
        print(f"Processing {input_path}...")
        img = Image.open(input_path)
        img = img.convert("RGBA")
        
        # إنشاء خلفية بيضاء صريحة
        background = Image.new("RGB", img.size, (255, 255, 255))
        
        # دمج الصورة مع الخلفية البيضاء باستخدام القناة ألفا
        background.paste(img, mask=img.split()[3]) # 3 is the alpha channel
        
        # حفظ كملف JPG (لا يدعم الشفافية)
        background.save(output_path, 'JPEG', quality=95)
        print(f"Success! Saved as {output_path}")
    else:
        print(f"Error: File not found at {input_path}")
except Exception as e:
    print(f"An error occurred: {e}")
