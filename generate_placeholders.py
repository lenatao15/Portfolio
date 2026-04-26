from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder(filename, text, color):
    # Create a 800x600 image with a solid color
    img = Image.new('RGB', (800, 600), color=color)
    d = ImageDraw.Draw(img)
    
    # Add some subtle pattern (lines)
    for i in range(0, 800, 40):
        d.line([(i, 0), (i+200, 600)], fill=(255, 255, 255, 30), width=2)

    # Note: Using default font since we don't know paths to specific ones
    # In a real environment, we'd use a nice TTF font.
    d.text((400, 300), text, fill="white", anchor="mm", align="center")
    
    img.save(f'media/projects/{filename}')

os.makedirs('media/projects', exist_ok=True)

projects = [
    ("chatbot.png", "CHATBOT\nPROJECT", (37, 99, 235)),
    ("n8n.png", "n8n AGENT\nWORKFLOW", (245, 158, 11)),
    ("langchain.png", "LANGCHAIN\nAGENT", (16, 185, 129)),
    ("google_ai.png", "GOOGLE AI\nSTUDIO", (220, 38, 38)),
    ("ml.png", "MACHINE\nLEARNING", (139, 92, 246)),
    ("skillswap.png", "CAMPUS\nSKILLSWAP", (20, 184, 166))
]

for filename, text, color in projects:
    create_placeholder(filename, text, color)
    print(f"Generated {filename}")
