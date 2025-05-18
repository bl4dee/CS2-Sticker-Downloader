import os
import requests
import json
from urllib.parse import urljoin
import time
from pathlib import Path

class CS2StickersDownloader:
    def __init__(self, download_dir="cs2_stickers"):
        self.base_url = "https://api.github.com/repos/ByMykel/counter-strike-image-tracker/contents/static/panorama/images/econ/stickers"
        self.raw_base_url = "https://raw.githubusercontent.com/ByMykel/counter-strike-image-tracker/main/static/panorama/images/econ/stickers"
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(exist_ok=True)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'CS2-Stickers-Downloader/1.0'
        })
        
    def get_directory_contents(self, path=""):
        """Get contents of a directory from GitHub API"""
        url = f"{self.base_url}/{path}" if path else self.base_url
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching directory {path}: {e}")
            return []
    
    def download_file(self, file_path, local_path):
        """Download a single file"""
        url = f"{self.raw_base_url}/{file_path}"
        try:
            response = self.session.get(url, stream=True)
            response.raise_for_status()
            
            # Create directory if it doesn't exist
            local_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Download the file
            with open(local_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            
            print(f"Downloaded: {local_path}")
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {file_path}: {e}")
            return False
    
    def explore_directory(self, path="", current_local_dir=None):
        """Recursively explore directories and download PNG files"""
        if current_local_dir is None:
            current_local_dir = self.download_dir
        
        print(f"Exploring: {path if path else 'root directory'}")
        contents = self.get_directory_contents(path)
        
        png_files = []
        subdirectories = []
        
        for item in contents:
            if item['type'] == 'file' and item['name'].endswith('.png'):
                png_files.append(item)
            elif item['type'] == 'dir':
                subdirectories.append(item)
        
        # Download PNG files in current directory
        for file_item in png_files:
            file_path = file_item['path'].replace('static/panorama/images/econ/stickers/', '')
            local_path = current_local_dir / file_item['name']
            
            # Skip if file already exists
            if local_path.exists():
                print(f"Skipping (already exists): {local_path}")
                continue
            
            self.download_file(file_path, local_path)
            
            # Be nice to GitHub's API
            time.sleep(0.1)
        
        # Recursively explore subdirectories
        for dir_item in subdirectories:
            subdir_path = dir_item['path'].replace('static/panorama/images/econ/stickers/', '')
            local_subdir = current_local_dir / dir_item['name']
            self.explore_directory(subdir_path, local_subdir)
    
    def download_all_stickers(self):
        """Download all stickers from the repository"""
        print("Starting CS2 stickers download...")
        print(f"Downloading to: {self.download_dir.absolute()}")
        
        try:
            self.explore_directory()
            print("\n✅ Download completed successfully!")
            print(f"All stickers saved to: {self.download_dir.absolute()}")
        except Exception as e:
            print(f"\n❌ Download failed: {e}")
    
    def get_download_stats(self):
        """Get statistics about downloaded files"""
        if not self.download_dir.exists():
            return {"total_files": 0, "total_size": 0}
        
        png_files = list(self.download_dir.rglob("*.png"))
        total_size = sum(f.stat().st_size for f in png_files)
        
        return {
            "total_files": len(png_files),
            "total_size": total_size,
            "total_size_mb": round(total_size / (1024 * 1024), 2)
        }

# Alternative method using the CSGO API for a more organized approach
class CS2StickersAPIDownloader:
    def __init__(self, download_dir="cs2_stickers_api"):
        self.api_url = "https://raw.githubusercontent.com/ByMykel/CSGO-API/main/public/api/en/stickers.json"
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(exist_ok=True)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'CS2-Stickers-API-Downloader/1.0'
        })
    
    def download_from_api(self):
        """Download stickers using the API endpoint"""
        print("Fetching sticker data from API...")
        
        try:
            # Get the stickers data
            response = self.session.get(self.api_url)
            response.raise_for_status()
            stickers_data = response.json()
            
            print(f"Found {len(stickers_data)} stickers to download")
            
            # Organize by collections/types
            collections = {}
            
            for sticker in stickers_data:
                # Determine collection/folder name
                collection_name = "unknown"
                
                if 'tournament_event' in sticker and sticker['tournament_event']:
                    collection_name = f"tournaments/{sticker['tournament_event'].replace(' ', '_')}"
                elif 'crates' in sticker and sticker['crates']:
                    crate_name = sticker['crates'][0]['name'].replace(' ', '_').replace('|', '')
                    collection_name = f"collections/{crate_name}"
                elif 'type' in sticker:
                    collection_name = f"types/{sticker['type'].lower()}"
                
                if collection_name not in collections:
                    collections[collection_name] = []
                collections[collection_name].append(sticker)
            
            # Download stickers organized by collection
            total_downloaded = 0
            for collection, stickers in collections.items():
                collection_dir = self.download_dir / collection
                collection_dir.mkdir(parents=True, exist_ok=True)
                
                print(f"\nDownloading {len(stickers)} stickers to {collection}...")
                
                for sticker in stickers:
                    if 'image' not in sticker:
                        continue
                    
                    # Clean filename
                    filename = sticker['name'].replace('Sticker | ', '').replace('/', '_').replace('\\', '_')
                    filename = f"{filename}.png"
                    local_path = collection_dir / filename
                    
                    # Skip if exists
                    if local_path.exists():
                        continue
                    
                    # Download
                    try:
                        img_response = self.session.get(sticker['image'], stream=True)
                        img_response.raise_for_status()
                        
                        with open(local_path, 'wb') as f:
                            for chunk in img_response.iter_content(chunk_size=8192):
                                if chunk:
                                    f.write(chunk)
                        
                        print(f"  ✓ {filename}")
                        total_downloaded += 1
                        time.sleep(0.1)  # Be nice to the server
                        
                    except Exception as e:
                        print(f"  ✗ Failed to download {filename}: {e}")
            
            print(f"\n✅ Successfully downloaded {total_downloaded} stickers!")
            print(f"Files saved to: {self.download_dir.absolute()}")
            
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    print("CS2 Stickers Downloader")
    print("=" * 50)
    print("Choose download method:")
    print("1. Direct from GitHub repository (explores all folders)")
    print("2. Using CSGO API (organized by collections)")
    print("3. Download both ways")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        downloader = CS2StickersDownloader()
        downloader.download_all_stickers()
        stats = downloader.get_download_stats()
        print(f"\nStats: {stats['total_files']} files, {stats['total_size_mb']} MB")
        
    elif choice == "2":
        downloader = CS2StickersAPIDownloader()
        downloader.download_from_api()
        
    elif choice == "3":
        print("\n--- Method 1: Direct GitHub ---")
        downloader1 = CS2StickersDownloader()
        downloader1.download_all_stickers()
        
        print("\n--- Method 2: API Organized ---")
        downloader2 = CS2StickersAPIDownloader()
        downloader2.download_from_api()
        
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()