# Rhyder - Một con bot đa chức năng đơn giản viết với Discord.py Release:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)

## Gói cần thiết
- **Python**: 3.10+ - tải tại đây: https://www.python.org/downloads/
- **Microsoft Visual Studio** - tải tại đây: https://visualstudio.microsoft.com/downloads/
- **JDK 17+** - tải tại đây: https://www.oracle.com/java/technologies/downloads/

## Giới thiệu dự án
- Dự án này là một con bot Discord được viết bằng Python. 
- Sử dụng `Wavelink` làm server để giao tiếp với Youtube - Spotify - Soundcloud để lấy nhạc cho con bot.
- Sử dụng `Google Gemini` để biến chú bot thành một chat bot giao tiếp trong server Discord.
- Sử dụng `Wikipedia API` để tra cứu các từ khóa.
- Sử dụng `Google Translate API` để phiên dịch câu nói tiếng Việt của bạn sang tiếng Anh  

## Hướng dẫn sử dụng
- Hãy có một tài khoản Discord trước tiên và truy cập https://discord.com/developers/applications để tạo và lấy cho mình `API Key` của con Bot theo hướng dẫn của Discord (Phải mời con bot vào server mình nhé). Tạo một file tên `.env` rồi dán `API Key` mà bạn được cung cấp bởi Discord vào chỗ các ký tự "XXX" như screenshot dưới.
*Hãy nhớ tùy chỉnh cho con bot trong trang Developer Portal có tất cả `intents` được bật lên.*

- Truy cập https://aistudio.google.com/ để lấy cho mình `API Key` theo hướng dẫn của Google. Rồi tạo một file `.env` rồi dán `API Key` mà bạn được cung cấp bởi Google rồi dán vào thay thế vị trí các ký tự "XXX" như screenshot sau:

![TokenScreenshot](https://github.com/Coder-Blue/rhyder-discord.py-bot/blob/main/screenshots/SC9.png?raw=true)

- Tiếp theo hãy chạy file tên `start.bat` để mở server Lavalink. Và nó sẽ có màn hình nếu chạy thành công như sau:
![LavaLinkScreenshot](https://github.com/Coder-Blue/rhyder-discord.py-bot/blob/main/screenshots/SC0.png?raw=true)

- Và bạn hãy `cd` vào thư mục repository mà bạn đã clone và sử dụng lệnh sau:
```bash
  pip install -r .\requirements.txt
```

```bash
  python bot.py
```

![BotScreenshot](https://github.com/Coder-Blue/rhyder-discord.py-bot/blob/main/screenshots/SC1.png?raw=true)

- Nếu đã setup thành công thì lệnh trên thì sẽ xuất hiện màn hình sau:
![SuccessScreenshot](https://github.com/Coder-Blue/rhyder-discord.py-bot/blob/main/screenshots/SC2.png?raw=true)


- Nếu bot đã thực hiện đầy đủ với các bước trên thì có thể trải nghiệm các tính năng sau:

### Các lệnh ví dụ của bot
![HelpScreenshot](https://github.com/Coder-Blue/rhyder-discord.py-bot/blob/main/screenshots/SC5.png?raw=true)

### Mở nhạc
![MusicScreenshot](https://github.com/Coder-Blue/rhyder-discord.py-bot/blob/main/screenshots/SC3.png?raw=true)
![MusicBOTScreenshot](https://github.com/Coder-Blue/rhyder-discord.py-bot/blob/main/screenshots/SC4.png?raw=true)

### Chat AI
![AIChatScreenshot](https://github.com/Coder-Blue/rhyder-discord.py-bot/blob/main/screenshots/SC6.png?raw=true)

### Wikipedia
![WikiScreenshot](https://github.com/Coder-Blue/rhyder-discord.py-bot/blob/main/screenshots/SC7.png?raw=true)

### Google Translate
![TransScreenshot](https://github.com/Coder-Blue/rhyder-discord.py-bot/blob/main/screenshots/SC8.png?raw=true)

## Kết thúc chương trình
- Khi không muốn sử dụng thì bạn có thể sử dụng nút `Close` hoặc `Alt + F4` vào màn hình terminal `python` đang chạy của bạn.
- Và bạn phải sử dụng tổ hợp phím `Ctrl + C` vào màn hình terminal `Lavalink` và gõ `y` và `Enter` để tắt server Lavalink đang chạy của bạn.

## Tổng kết
- Bạn có thể sử dụng mặc định hoặc thực hiện một số tùy chỉnh nếu bạn muốn thay đổi bằng ngôn ngữ Python, chi tiết tài liệu tham khảo là: https://discordpy.readthedocs.io/en/stable/ và https://github.com/PythonistaGuild/Wavelink.

- Đây là dự án mã nguồn mở nên thoải mái thay đổi và cải tiến, nhưng hãy trích tác giả gốc `Noah Trần` như một sự tri ân.

## Hỗ trợ
- Bạn có thể nhận được sự hỗ trợ bằng các cách sau:

Tham gia máy chủ Discord của tôi: https://discord.gg/5Nmwm24dWV

Liên hệ qua Email: trananhquan1009@gmail.com

Liên hệ qua Facebook: Noah Trần