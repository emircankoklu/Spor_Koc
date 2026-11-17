import os
from pathlib import Path
import pyzipper

source_dir = Path("SonFitcode")
out_zip = Path("fitcode_jüri") / "FitCode_Kaynak_Kodlari_Guvenlikli.zip"
password = b"FitCode2026!Juri"

exclude_dirs = {
    ".venv", ".venv-1", "venv", ".git", "__pycache__", ".idea", 
    "chrome-screenshots-profile", "profile2-tabu", "profile-week2-tabu", 
    "profile-week2-gallery", "profile2-gallery", "profile2-home", "profile2-route"
}
exclude_exts = {".pyc", ".tmp", ".log"}

count = 0
with pyzipper.AESZipFile(
    out_zip,
    "w",
    compression=pyzipper.ZIP_DEFLATED,
    encryption=pyzipper.WZ_AES
) as zf:
    zf.setpassword(password)
    
    for root, dirs, files in os.walk(source_dir):
        # filter out ignored directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith("profile")]
        
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in exclude_exts or file.endswith(".exe") or file.endswith(".zip"):
                continue
            
            full_path = Path(root) / file
            rel_path = full_path.relative_to(source_dir)
            
            try:
                zf.write(full_path, arcname=f"FitCode_Source/{rel_path}")
                count += 1
            except Exception as e:
                print(f"Error adding {rel_path}: {e}")

print(f"Successfully packaged {count} source files into {out_zip} ({out_zip.stat().st_size} bytes)")

