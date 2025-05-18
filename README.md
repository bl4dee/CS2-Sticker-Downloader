# CS2 Stickers Downloader

A Python tool to download all Counter-Strike 2 (CS2) stickers in high quality PNG format. This tool provides two methods to download and organize the complete collection of CS2 stickers.

## Features

-  Download all CS2 stickers (1000+ files)
-  Two download methods: Direct GitHub repository or organized API
-  Automatic organization by tournaments, collections, and types
-  Smart downloading (skips existing files)
-  Rate limiting to be respectful to servers

## Installation

### Prerequisites
- Python 3.7 or higher
- `requests` library

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

This tool relies on these excellent projects:

- **Counter-Strike Image Tracker**: [ByMykel/counter-strike-image-tracker](https://github.com/ByMykel/counter-strike-image-tracker)
- **CSGO API**: [ByMykel/CSGO-API](https://github.com/ByMykel/CSGO-API)

Special thanks to ByMykel for maintaining these comprehensive resources!

## Legal Notice

⚖️ **Important**: This tool downloads publicly accessible images for personal use only.

- **Copyright**: All CS2 stickers remain the intellectual property of Valve Corporation and respective creators
- **Personal Use Only**: Downloaded images are for personal collection and educational purposes
- **No Commercial Use**: Do not use these images for commercial purposes without proper licensing
- **Public APIs**: This tool only accesses publicly available APIs and images
- **No Reverse Engineering**: No unauthorized access or data extraction is performed
- **Respectful Usage**: Rate limiting ensures we don't overwhelm source servers

**Disclaimer**: This project is not affiliated with Valve Corporation. Counter-Strike and CS2 are trademarks of Valve Corporation.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Troubleshooting

### Common Issues

**Download fails or times out:**
- Check your internet connection
- The script will resume from where it left off if restarted

**Permission errors:**
- Make sure you have write permissions in the download directory
- Try running from a different location

**API rate limiting:**
- The script includes delays to prevent rate limiting
- If you encounter issues, wait a few minutes and retry

### Getting Help

If you encounter issues:
1. Check the [Issues](https://github.com/bl4dee/cs2-stickers-downloader/issues) page
2. Create a new issue with:
   - Your operating system
   - Python version
   - Error message (if any)
   - Steps to reproduce

## Frequently Asked Questions

**Q: Is this legal?**
A: Yes, this tool only downloads publicly accessible images using public APIs for personal use.

**Q: Will this get me banned from Steam?**
A: No, this tool doesn't interact with Steam or your account in any way.

**Q: How much storage space do I need?**
A: Approximately 500MB-1GB depending on which method you choose.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is not affiliated with Valve Corporation. Counter-Strike and CS2 are trademarks of Valve Corporation. Downloaded images remain the property of their respective owners.
