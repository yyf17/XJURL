import qrcode

base_url = "https://github.com/yyf17/XJURL/blob/main"

for i in range(1, 21):
    chapter = f"chapter{i:02d}"
    
    colab_url = f"{base_url}/Colab/{chapter}.ipynb"
    ref_url = f"{base_url}/Ref/{chapter}/ref{i:02d}.md"
    video_url = f"{base_url}/Video/{chapter}/v{i}.mp4"
    
    qr_colab = qrcode.make(colab_url)
    qr_colab.save(f"QR/{chapter}/Colab{i:02d}.png")
    
    qr_ref = qrcode.make(ref_url)
    qr_ref.save(f"QR/{chapter}/Ref{i:02d}.png")
    
    qr_video = qrcode.make(video_url)
    qr_video.save(f"QR/{chapter}/Video{i:02d}.png")

print("QR codes generated successfully!")
