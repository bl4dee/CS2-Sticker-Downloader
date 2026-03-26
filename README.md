# CS2 Stickers Downloader

A Python tool to download all Counter-Strike 2 stickers in high quality PNG format. This tool provides two methods to download and organize the complete collection of CS2 stickers.

## Features

-  Download all CS2 stickers (1000+ files)
-  Two download methods: Direct GitHub repository or organized API
-  Automatic organization by tournaments, collections, and types
-  Smart downloading (skips existing files)
-  Rate limiting to be respectful to servers

## Installation

### Prerequisites
- Python 3.7 or higher

### Setup
1. Clone this repository:
```bash
git clone https://github.com/bl4dee/CS2-Sticker-Downloader.git
cd CS2-Sticker-Downloader
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python cs2_stickers_downloader.py
```

Choose from three options:
1. **Direct GitHub Repository** - Downloads from the image tracker repository
2. **CSGO API** - Downloads using the API with better organization
3. **Both methods** - Downloads using both approaches

## Output Structure

The tool organizes stickers into logical folders:

```
cs2_stickers/
├── tournaments/
│   ├── Katowice_2014/
│   ├── Paris_2023/
│   └── ...
├── collections/
│   ├── Community_Sticker_Capsule_1/
│   ├── CS20_Sticker_Capsule/
│   └── ...
└── types/
    ├── team/
    ├── player/
    └── ...
```

## Download Methods

### Method 1: Direct GitHub Repository
- Explores the entire GitHub repository structure
- Downloads every PNG file found
- More comprehensive but slower
- Uses: [counter-strike-image-tracker](https://github.com/ByMykel/counter-strike-image-tracker)

### Method 2: CSGO API
- Uses structured API data with metadata
- Better organization by collections and tournaments
- Faster and more reliable
- Uses: [CSGO-API](https://github.com/ByMykel/CSGO-API)

## Credits & Data Sources

This tool relies on:

- **Counter-Strike Image Tracker**: [ByMykel/counter-strike-image-tracker](https://github.com/ByMykel/counter-strike-image-tracker)
- **CSGO API**: [ByMykel/CSGO-API](https://github.com/ByMykel/CSGO-API)

Special thanks to ByMykel for maintaining these comprehensive resources!

## Contributing

**Contributions welcome!**

Ideas for contributions:
- Support for other CS2 assets (skins, cases, etc.)
- GUI interface
- Download progress improvements

## Troubleshooting

### Common Issues

**Download fails or times out:**
- Turn off VPN & wait a couple minutes 
- The script will resume from where it left off if restarted

**API rate limiting:**
- The script includes delays to prevent rate limiting
- If you encounter issues, wait a few minutes and retry
