"""Utility: bundle repo into a ZIP for sharing."""
import shutil
import os




def pack_repo(output_path: str = "ai_trader_release.zip"):
base = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
shutil.make_archive(output_path.replace('.zip',''), 'zip', base)
print("Repo packaged at", output_path)




if __name__ == "__main__":
pack_repo()
